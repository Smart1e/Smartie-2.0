class json_things():
    
    def create_json(language, password, username, file='Data/data.json', ):
        import json
        with open(file, "w") as f:
            settings = {'language': language, 'password': password, 'username': username}
            json_data = json.dumps(settings)
            f.write(json_data)
            
        
        """
        Creates a json file.
        """
        
        
        
    def save_json(key, value, file='Data/data.json'):
        import json
        with open(file, 'r') as f:
            current_json = json.load(f)
            
        current_json[key] = value
        
        with open(file, 'w') as f:
            myJSON = json.dumps(current_json)
            f.write(myJSON)
    
    
    def load_json(key='*', file='Data/data.json'):
        import json
        with open(file, 'r') as f:
            current_json = json.load(f)
        
        if key == '*':
            return current_json   
        else: 
            return current_json[key]        
            
    '''
    Old code:

    def read(key='all', file='settings.json'):
        import json
        if key == 'all':

            with open(file, "r") as f:
                data = json.load(f)

            f.close()
            return data
        else:
            with open(file, "r") as f:
                data = json.load(f)

            f.close()
            return data[key]
            
            
            
        '''        
        
        
        
