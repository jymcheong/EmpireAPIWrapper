"""
Return None if not admin. Otherwise it returns str value of either: Domain or Local
For local user, check if s/he is in local administrator
For domain user, it is possible that s/he is in both local &/or domain administrator group
but we return the higher of the two types 
"""
from EmpireAPIWrapper import empireAPI
from empire_settings import EMPIRE_SERVER, EMPIRE_PWD, EMPIRE_USER
from empire_autocomplete import situational_awareness

def run(API, agent_name):
    """
    Returns admin type, otherwise None
    :param API: EmpireAPIWrapper object
    :param agent_name: name of agent
    :return type: str
    """
    agent_details = API.agent_info(agent_name)['agents'][0]
    # either local/domain user, still check if user is in local administrators
    opts = {'Agent': agent_name, 'command': 'net localgroup Administrators'}
    r = API.agent_run_shell_cmd(agent_name, opts)
    r = API.agent_get_results(agent_name, r['taskID'])    
    if r is None:
        raise ValueError('fail to run "net localgroup Administrator", check empire console')
    # first case: for a local user (will always be host\username), check if s/he is local admin group
    if agent_details['hostname'] in agent_details['username']: 
        target_username = agent_details['username'].replace(agent_details['hostname']+'\\', "")
        if target_username in r:
            return "Local"
    else: # 2nd case, for a domain user, we return the higher privilege group ie. Domain
        target_username = agent_details['username'].split('\\')[1]
        opts = situational_awareness.network_powerview_get_group.options
        r = API.module_exec(situational_awareness.network_powerview_get_group.path, \
                            {opts.username: target_username,
                             opts.required_agent: agent_name})
        r = API.agent_get_results(agent_name, r['taskID'])
        if 'Admin' in r: # there are other types of admin eg. Enterprise, Schema Admin...
            return 'Domain'
    return None

if __name__ == '__main__':
    API = empireAPI(EMPIRE_SERVER, uname=EMPIRE_USER, passwd=EMPIRE_PWD)
    # run(API, 'fuck') # exception if no agent of that name
    run(API, '59RXB1TY')