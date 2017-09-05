""" This module demonstrates procedure scripting
    We aim to make procedure agnostic to techniques which could
    be implemented with Empire, Metasploit or whatever pen-test framework that
    supports APIs
"""
from EmpireAPIWrapper import empireAPI
import stage2.deliver_payload.windows.technique1
import stage2.deliver_payload.windows.technique2 
from stage2.external_c2 import empire_wait_for_agent

try:
    # use a common API context instead of creating new ones within Empire techniques
    API = empireAPI('empirec2', uname='empireadmin', passwd='Password123')

    AGENTNAME = empire_wait_for_agent.run(API,'pec-WIN10PRO64', False)
    print(AGENTNAME) # blank means no agent found

    # every technique script implements a run function
    # technique scripts encapsulate technique specific details
    stage2.deliver_payload.windows.technique1.run("1.1.1.1")
    print(stage2.deliver_payload.windows.technique1.run("2.2.2.2"))
    
    # technique 2 is a folder module vs technique 1 which is a script
    stage2.deliver_payload.windows.technique2.something('a','b')
except Exception as e:
    print("Oops: " + str(e))
