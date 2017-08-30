"""This is a sample technique script using EmpireAPIWrapper"""
from EmpireAPIWrapper import empireAPI


if __name__ == "__main__":
                                    # change to your IP/host & (token or credentials)
    API = empireAPI('empirec2', uname='empireadmin', passwd='Password123')
    AGENT = API.agents()
    if 'agents' not in AGENT:
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
        OPTIONS = {'Agent': AGENT_NAME} # ie. gather from module's "info"
        TASKID = API.module_exec('powershell/situational_awareness/host/antivirusproduct', \
                                OPTIONS)['taskID']
        print('new taskID = ' + str(TASKID))
        print(API.agent_get_results(AGENT_NAME, TASKID))

        # module exception example (needs admin rights but session is non-elevated)
        API.module_exec('powershell/situational_awareness/host/computerdetails', OPTIONS)

    except Exception as e:
        print('Error: ' + str(e))
    