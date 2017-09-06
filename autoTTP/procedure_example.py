""" This module demonstrates procedure scripting
    We aim to make procedure agnostic to techniques which could
    be implemented with Empire, Metasploit or whatever pen-test framework that
    supports APIs
"""
from EmpireAPIWrapper import empireAPI
from empire_settings import *
import stage2.deliver_payload.windows.technique1
import stage2.deliver_payload.windows.technique2 
from stage2.external_c2 import empire_wait_for_agent

try:
    # use a common API context instead of creating new ones within Empire techniques
    API = empireAPI(EMPIRE_SERVER, uname=EMPIRE_USER, passwd=EMPIRE_PWD)

    # every technique script implements a run function
    # technique scripts encapsulate technique specific details
    stage2.deliver_payload.windows.technique1.run("1.1.1.1")
    print(stage2.deliver_payload.windows.technique1.run("2.2.2.2"))

    # dummy technique 2 is a folder module vs technique 1 which is a script
    stage2.deliver_payload.windows.technique2.something('a','b')
    
    # wait for privilege agent
    AGENTNAME = empire_wait_for_agent.run(API,'WIN-7JKBJEGBO38', True)
    print(AGENTNAME) # blank means no agent found

    # wait for non-privilege agent
    AGENTNAME = empire_wait_for_agent.run(API,'WIN-7JKBJEGBO38', False)
    print(AGENTNAME) # blank means no agent found    
    
except Exception as e:
    print("Oops: " + str(e))
