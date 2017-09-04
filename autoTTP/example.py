"""This is a sample/test script for EmpireAPIWrapper
   Illustrate some of the typical things we do with Empire 
   eg. get listeners, agents, exec shellcmd or modules, get taskid, task results
"""
from EmpireAPIWrapper import empireAPI
import empire_autocomplete

if __name__ == "__main__":
                                    # change to your IP/host & (token or credentials)
    API = empireAPI('empirec2', uname='empireadmin', passwd='Password123')
    LIS = API.listeners()
    AGENT = API.agents()
    if 'agents' not in AGENT: # quit if no agents to work with
        exit

    AGENT_NAME = AGENT['agents'][0]['name']
    # this agent method is necessary we will want to target the correct host
    # procedure-script only provides hostname or IP address; not agentName, which is dynamic
    print('agent name: ' + API.agent_get_name('pec-WIN10PRO64'))
    
    try:
        # shell command example
        DATA = {'Agent': AGENT_NAME, 'command': 'date'} # date is a rather slow command
        TASKID = API.agent_run_shell_cmd(AGENT_NAME, DATA)['taskID']
        print('new taskID = ' + str(TASKID))
        print(API.agent_get_results(AGENT_NAME, TASKID))

        # module execution Job example
        OPTIONS = {empire_autocomplete.situational_awareness.host_antivirusproduct.options.required_agent: AGENT_NAME} # ie. gather from module's "info"
        TASKID = API.module_exec(empire_autocomplete.situational_awareness.host_antivirusproduct.path, \
                                OPTIONS)['taskID']
        print('new taskID = ' + str(TASKID))
        print(API.agent_get_results(AGENT_NAME, TASKID))

        # module exception example (needs admin rights but session is non-elevated)
        API.module_exec(empire_autocomplete.situational_awareness.host_computerdetails.path, OPTIONS)

    except Exception as e:
        print('Error: ' + str(e))
    