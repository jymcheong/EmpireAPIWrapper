"""This module demonstrates procedure scripting based on import"""
import importlib
import os

try:
    os.environ["TARGET_HOST"] = "1.1.1.1"
    import stage2.windows.deliverPayload.technique1 # technique1.py uses the environment variable
    print(os.environ["TTP_RESULT"]) # technique script can return results
    
    os.environ["TARGET_HOST"] = "2.2.2.2"
    importlib.reload(stage2.windows.deliverPayload.technique1) # reload if any changes to env variable
    print(os.environ["TTP_RESULT"])

except Exception as e:
    pass
