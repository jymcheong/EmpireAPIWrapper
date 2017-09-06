"""
Return None if not admin. Otherwise it returns str value of either: Domain or Local
For local user, check if s/he is in local administrator
For domain user, it is possible that s/he is in both local &/or domain administrator group 
"""
from EmpireAPIWrapper import empireAPI
from empire_settings import EMPIRE_SERVER, EMPIRE_PWD, EMPIRE_USER


def run(API, agent_name):
    """
    Returns admin type, otherwise None
    :param API: EmpireAPIWrapper object
    :param agent_name: name of agent
    :return type: str
    """
    agent_details = API.agent_info(agent_name)['agents'][0]
    # either local/domain user, still check if user is in local administrators
    opt = {'Agent': agent_name, 'command': 'net localgroup Administrators'}
    r = API.agent_run_shell_cmd(agent_name, opt)
    if 'taskID' not in r:
        raise ValueError('No taskID')
    r = API.agent_get_results(agent_name, r['taskID'])    
    # first case, for local user strip the hostname from hostname\username
    # domain user will not be affected
    if agent_details['hostname'] in agent_details['username']: 
        target_username = agent_details['username'].replace(agent_details['hostname']+'\\', "")
        if target_username in r:
            return "Local"
    else: # 2nd case, for a domain user, we return the higher privilege group ie. Domain
        pass # todo 
    return None

if __name__ == '__main__':
    API = empireAPI(EMPIRE_SERVER, uname=EMPIRE_USER, passwd=EMPIRE_PWD)
    # run(API, 'fuck') # exception if no agent of that name
    run(API, 'V1MTCZG7')