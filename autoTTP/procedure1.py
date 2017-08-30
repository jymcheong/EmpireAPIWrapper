"""This module demonstrates procedure scripting"""
import stage2.windows.deliverPayload.technique1
import stage2.windows.deliverPayload.technique2

try:
    # every technique script implements a run function
    stage2.windows.deliverPayload.technique1.run("1.1.1.1")
    print(stage2.windows.deliverPayload.technique1.run("2.2.2.2"))
    stage2.windows.deliverPayload.technique2.something('a','b')
    
except Exception as e:
    pass
