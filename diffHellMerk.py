#Class to generate private key from Diffie Hellman Merkle key gen equation, employs strategy pattern
class diffHellMerk:

    def __init__(self):
        self.name = 'dht'
    
    def shareKey(self, personGood, copy):
        print("in shareKey")
        soloVal = personGood.soloVal
        modVal = personGood.modVal
        return soloVal**copy % modVal 
        
        


