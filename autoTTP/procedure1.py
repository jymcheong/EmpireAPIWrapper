"""This module demonstrates procedure scripting based on import"""
import stage2.windows.deliverPayload.technique1 # technique1.py uses the environment variable

try:
    stage2.windows.deliverPayload.technique1.run("1.1.1.1")
    print(stage2.windows.deliverPayload.technique1.run("2.2.2.2"))

except Exception as e:
    pass
