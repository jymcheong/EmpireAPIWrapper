class code_execution(object):
    """ helper auto-generated class to provide auto-completion of modulename & options"""

    class invoke_metasploitpayload(object):
        """
        'Description': ('Spawns a new, hidden PowerShell window that downloads'
                            'and executes a Metasploit payload. This relies on the' 
                            'exploit/multi/scripts/web_delivery metasploit module.'),
            
        """

        path = 'powershell/code_execution/invoke_metasploitpayload'

        class options(object):
            """
            self.options = {
                'Agent' : {
                    'Description'   :   'Agent to run Metasploit payload on.',
                    'Required'      :   True,
                    'Value'         :   ''
                },
                'URL' : {
                    'Description'   :   'URL from the Metasploit web_delivery module',
                    'Required'      :   True,
                    'Value'         :   ''
                }
            }
            """    
            
            required_agent = 'Agent'
            required_url = 'URL'        
        
    