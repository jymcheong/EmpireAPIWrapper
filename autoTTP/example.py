"""This is a sample/test script for EmpireAPIWrapper
   Illustrate some of the typical things we do with Empire 
   eg. get listeners, agents, exec shellcmd or modules, get taskid, task results
"""
from EmpireAPIWrapper import empireAPI
from empire_settings import *
import empire_autocomplete

if __name__ == "__main__":
                                    # change to your IP/host & (token or credentials)
    API = empireAPI(EMPIRE_SERVER, uname=EMPIRE_USER, passwd=EMPIRE_PWD)
    AGENT = API.agents()
    if 'agents' not in AGENT: # quit if no agents to work with
        exit

    AGENT_NAME = API.agent_get_name('pec-WIN10PRO64', True)
    # this agent method is necessary we will want to target the correct host
    # procedure-script only provides hostname or IP address; not agentName, which is dynamic
    print('agent name: ' + AGENT_NAME)
    
    try:
        # shell command example
        DATA = {'Agent': AGENT_NAME, 'command': 'date'} # date is a rather slow command
        TASKID = API.agent_run_shell_cmd(AGENT_NAME, DATA)['taskID']
        print('new taskID = ' + str(TASKID))
        print(API.agent_get_results(AGENT_NAME, TASKID))

        # module execution Job example
        opts = empire_autocomplete.situational_awareness.host_antivirusproduct.options
        OPTIONS = {opts.required_agent: AGENT_NAME} # ie. gather from module's "info"
        TASKID = API.module_exec(empire_autocomplete.situational_awareness.host_antivirusproduct.path, \
                                OPTIONS)['taskID']
        print('new taskID = ' + str(TASKID))
        print(API.agent_get_results(AGENT_NAME, TASKID))

        # module exception example (needs admin rights but session is non-elevated)
        TASKID = API.module_exec(empire_autocomplete.situational_awareness.host_computerdetails.path, OPTIONS)['taskID']
        print('new taskID = ' + str(TASKID))
        print(API.agent_get_results(AGENT_NAME, TASKID))

    except Exception as e:
        print('Error: ' + str(e))
    