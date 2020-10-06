import json

class Save:
    def __init__(self,dico):
        self.dico = dico
        self.fileName = "data.json"
    
    def getDico(self):
        return self.dico
    
    def upload(self):

        with open(self.fileName, 'w') as file:
            file.write(json.dumps(self.dico))
        
    def download(self):

        with open(self.fileName,'r') as file:
            return json.loads(file.read())


"""
dico = {"1D":["1F",0,1],"2D":["2F",0,0]}
n = Save(dico)
n.upload()
print(n.download())
"""