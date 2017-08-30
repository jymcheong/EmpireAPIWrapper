import EmpireAPIWrapper


if __name__ == "__main__":
                                    # change to your IP/host & (token or credentials)
    api = EmpireAPIWrapper.empireAPI('empirec2', uname='empireadmin', passwd='Password123')
    agent = api.agents()
    agent_name = agent['agents'][0]['name']
    
    try:
        # shell command example
        data = {'Agent': agent_name, 'command': 'date'} # date is a rather slow command
        taskID = api.agent_run_shell_cmd(agent_name, data)['taskID']
        print('new taskID = ' + str(taskID))
        print(api.agent_get_results(agent_name,taskID))
        
        # module execution Job example
        options = {'Agent': agent_name} # ie. gather from module's "info"
        taskID = api.module_exec('powershell/situational_awareness/host/antivirusproduct', options)['taskID']
        print('new taskID = ' + str(taskID))
        print(api.agent_get_results(agent_name,taskID))
       
        # module exception example (needs admin rights but session is non-elevated)
        api.module_exec('powershell/situational_awareness/host/computerdetails', options)
        api.agent_get

    except Exception as e:
        print('Error: ' + str(e))