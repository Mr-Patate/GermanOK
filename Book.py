import random
from Save import Save
"""

This script contains everything that has a purpose with words

"""

class Word:
    def __init__(self):
        d = Save("")
        self.dico = d.download()

    def getDico(self):
        return self.dico

    def pickWord(self):
        print("A Word is picked")
        key = random.choice(list(self.dico))
        return key ,self.dico[key]

    def compareWord(self,key,word):
        if self.dico[key][0] == word:
            return True
        else:
            return False

    def updateWord(self,word,point):
        if point:
            self.dico[word][1] += 1
        else:
            self.dico[word][2] += 1
        d = Save(self.getDico())
        d.upload()
    
    def deleteWord(self,word):
        self.dico.pop(word)
        d = Save(self.getDico())
        d.upload()

    def newWord(self,de,fr):
        print("New Word learned: {} for {}".format(de,fr))
        try:
            if self.dico[de]:
                print("Word Already Exist")
                pass
            else:
                pass
        except KeyError:
            print("Creating New Word")
            self.dico[de] = [fr,0,0]
            d = Save(self.getDico())
            d.upload()

"""
dico = {"1D":["1F",0,0],"2D":["2F",0,0]}
n = Word()
he = n.pickWord()
print(he)
print(he[0])

n.newWord("ok","ok")
print(n.getDico())
n.newWord("1D","1F")
"""