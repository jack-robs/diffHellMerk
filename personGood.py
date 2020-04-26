#class for person in pair of  Diffie Hellman Merkel key generation 

class personGood:
    
    def __init__(self, personName, soloVal=None, modVal=None, trustedPartner=[]): 
        '''
        Fxn: __init__
        Does: init'd a personGood object, involved in shared priv key generation 
        Params:
        - personName: str, name of person
        - soloVal: `Y` in `Y^x (mod P)`, default of none, which allows one person to decide 
        and send `Y` value to the other personGood
        - modVal: `P` in `Y^x (modP)`, default of none, same reasoning
        - trustedPartner: list strs, names that are trusted to key exchange with. 
            - an object can only be instantiated w/ initial trusted partners  
            - when a person wants to share with others, it will firts check if trusted, and then
            add object.personName to registeredPartners
            - all interactions after check if registeredPartner is ok
        '''

        # __ is private field
        self.personName = personName
        self.soloVal = soloVal
        self.modVal = modVal
        self.pubShare = None
        # don't make a getter for __
        self.__privKey = None
        # TODO see if this makes sense in scheme of implied trust of sharing mods
        self.__trustedPartner = trustedPartner

    def __checkTrust(self, personClass):
        #REMOVE __ FOR TESTING
        '''
        Fxn: checkTrust()
        Does: confirms person object passed in is on trusted list
        Params:
        - personClass, object, personGood
        Returns: bool, trust/no trust
        '''
        name = personClass.getName()
        return name in self.__trustedPartner


    def shareMod(self, modVal, personClass):
        '''
        Fxn: shareMod()
        Does: sets modVal for personClass object 
        Params: 
        - modVal; int, modValue, `P` in `Y^x (mod P)`
        - personClass: class, personGood object, other person in DHM key generation
        Return: true/false boolean for success, handshake pattern
        '''
        
        return True

    def __setMod(self, modVal):
        #TODO confirm only instance itself can set modVal
        '''
        Fxn: __setMod(), private function
        Does: sets modVal if modVal cretaed by other partner
        Params: modVal, value to set mod to. 
        Return: none
        '''
        print("in class")
        pass




    def getName(self):
        '''
        Fxn: getName() 
        Does: getter for personName
        Params: self
        Return: self.personName
        '''
        return self.personName

    def getSoloVal(self):
        '''
        Fxn: getSoloVal()
        Does: getter soloVal
        Params: self
        Return:  self.personName
        '''
        return self.soloVal

    def getModVal(self):
        '''
        Fxn: getModVal()
        Does: getter modVal
        Params: self
        Return: self.modVal
        '''
        return self.ModVal

    def getPubShare(self):
        '''
        Fxn: getPubShare()
        Does: getter pubShare
        Params: self
        Return: self.pubShare
        '''
        return self.pubShare

    def getPrivKey(self):
        '''
        Fxn: getPrivKey()
        Does: getter privKey
        Params: self
        Return: self.privKey
        '''
        return self.privKey

        
    def toString(self):
        '''
        Fxn: toString()
        Does: returns state of personGood
        Params: self
        Return: person, str
        '''
        #TODO add more fields for later steps
        person = ""
        person += self.personName
        person += " " + str(self.soloVal)
        person += " " + str(self.modVal)
        person += " " + str(self.pubShare)

        return person
        
































