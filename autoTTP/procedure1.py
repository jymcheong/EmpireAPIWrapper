"""This module demonstrates procedure scripting"""
import stage2.deliverPayload.windows.technique1
import stage2.deliverPayload.windows.technique2

try:
    # every technique script implements a run function
    stage2.deliverPayload.windows.technique1.run("1.1.1.1")
    print(stage2.deliverPayload.windows.technique1.run("2.2.2.2"))
    
    # technique 2 is a folder module vs technique 1 which is a script
    stage2.deliverPayload.windows.technique2.something('a','b')
    
except Exception as e:
    pass
