""" This module demonstrates procedure scripting
    We aim to make procedure agnostic to techniques which could
    be implemented with Empire, Metasploit or whatever pen-test framework that
    supports APIs
"""
import stage2.deliver_payload.windows.technique1
import stage2.deliver_payload.windows.technique2 
# autocomplete class is generated from empire source 
# rightfully this is used inside technique's run function


try:
    # every technique script implements a run function
    stage2.deliver_payload.windows.technique1.run("1.1.1.1")
    print(stage2.deliver_payload.windows.technique1.run("2.2.2.2"))
    
    # technique 2 is a folder module vs technique 1 which is a script
    stage2.deliver_payload.windows.technique2.something('a','b')
except Exception as e:
    pass
