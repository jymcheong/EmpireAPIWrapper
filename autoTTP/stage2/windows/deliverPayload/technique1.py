"""This module requires TARGET_HOST as input"""
import os

print(os.environ["TARGET_HOST"])

# set env variable eg. new session ID
os.environ["TARGET_SESSION"] = "xyz"
os.environ["TTP_RESULT"] = "some result for decision making " + os.environ["TARGET_HOST"]
