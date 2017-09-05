""" 
Relative path import gets complicated when we want things to 
run both at technique & procedural script (many folders above) layers, 
so I used symbolic link which seems to work but it's ugly
"""
from EmpireAPIWrapper import empireAPI

def run(API, host_name, need_privilege=False, time_out_sec = 180):
    """
    Returns agent name when found, else empty string
    :param API: empire API wrapper object
    :param host_name: target's host name
    :param need_privilege: set to true if need privileged agent
    :param time_out_sec: time out in seconds
    :returns: str (empty string if can't find)
    """
    time_out = time_out_sec
    agent_name = ""
    while time_out > 0:
        agent_name = API.agent_get_name(host_name, need_privilege)        
        if len(agent_name) > 0:
            break
        time_out -= 1
    return agent_name


# for unit testing of each technique
if __name__ == '__main__':
    API = empireAPI('empirec2', uname='empireadmin', passwd='Password123')
    print(run(API, 'pec-WIN10PRO64'))
    print(run(API, 'pec-WIN10PRO64', True))
    
