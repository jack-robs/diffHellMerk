#class for person in pair of  Diffie Hellman Merkel key generation 

class personGood:
    
    def __init__(self, personName, soloVal=None, modVal=None):
        '''
        Fxn: __init__
        Does: init'd a personGood object, involved in shared priv key generation 
        Params:
        - personName: str, name of person
        - soloVal: `Y` in `Y^x (mod P)`, default of none, which allows one person to decide 
        and send `Y` value to the other personGood
        - modVal: `P` in `Y^x (modP)`, default of none, same reasoning
        '''
        # __ is private field
        self.__personName = personName
        self.__soloVal = soloVal
        self.__modVal = modVal
        self.__pubShare = None
        self.__privKey = None

    
    #-------------------@property getters---------------------#
    
    @property
    def personName(self):
        '''
        Fxn: @property personName()
        Does: get personName
        Params: self
        Returns: self._personName
        '''
        return self.__personName

    @property
    def soloVal(self):
        '''
        Fxn: @property soloVal()
        Does: get soloVal
        Params: self
        Returns: self.__soloVal
        '''
        return self.__soloVal

    @property
    def modVal(self):
        '''
        Fxn: @property modVal()
        Does: get modVal
        Params: self
        Returns: self.__modVal
        '''
        return self.__modVal

    @property
    def pubShare(self):
        '''
        Fxn: @property pubShare()
        Does: get pubShare
        Params: self
        Returns: self.__pubShare
        '''
        return self.__pubShare

 
    #-------------------@value.setter-----------------------#
    @soloVal.setter
    def soloVal(self, value):
        '''
        Fxn: @x.setter soloVal()
        Does: sets soloVal if other party decides on it and/or not instantaited with class
        - soloVal must be less than modVal, if modVal already set
        Params: self, value - value to set soloVal to in `soloVal^x (mod modVal)`
        Returns: none
        '''
        if self.__modVal == None:
            self.__soloVal = value
        elif self.__modVal > value:
            self.__soloVal = value
        else:
            raise ValueError("soloVal must be less than modVal, mod val already set")

    @modVal.setter
    def modVal(self, value):
        '''
        Fxn: @x.setter modVal()
        Does: set modVal if other party decides on it and/or not instantiated with class
        - modVal must be greater than soloVal, if soloVal already set
        Params: self, value - value to set modVal to, int, `soloVal^x (mod modVal)`
        Returns: none
        '''
        if self.__soloVal == None:
            self.__modVal = value
        elif self.__soloVal < value:
            self.__modVal = value
        else:
            raise ValueError("modVal must be greater than soloVal, soloVal already set")



    # TODO confirm privKey: do encryption, see if it works!


        
    def toString(self):
        '''
        Fxn: toString()
        Does: returns state of personGood
        Params: self
        Return: person, str
        '''
        #TODO add more fields for later steps
        person = ""
        person += self.__personName
        person += " " + str(self.__soloVal)
        person += " " + str(self.__modVal)
        person += " " + str(self.__pubShare)

        return person
        
































