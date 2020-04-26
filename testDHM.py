#Test file for Diffie-Hellman-Merkle project

import personGood as pg


def peopleBasicTest():
    '''
    fxn: peopleClassTest()
    does: tests class instantation of class People()
    params: none
    returns: passVal, int, 1 pass, 0 fail
    '''
    passVal = 0
    testRun = 0
     
    #personGood object, mod and solo value enumerated
    pA = pg.personGood('bob', 1, 2)
    expA = "bob 1 2 None"
    actA = pA.toString()
    try: 
        assert expA == actA,  "Failed bob 1 2 None"
        passVal += 1
    except AssertionError as e: print(e)

    testRun += 1

    #personGood object, mod and solo value defaults used
    pB = pg.personGood('alice')
    expB = 'alice None None None'
    actB = pB.toString()
    try: 
        assert expB == actB, "Failed alice None None None"
        passVal += 1
    except AssertionError as e: print(e)

    testRun += 1


    #personGood object, mod custom, solo default
    pC = pg.personGood('alice', modVal=2)
    expC = 'alice None 2 None'
    actC = pC.toString()
    try: 
        assert expC == actC, "Failed alice None 2 None"
        passVal += 1
    except AssertionError as e: print(e)

    testRun += 1

    #personGood object, mod default, solo custom
    pD = pg.personGood('steve', 4)
    expD = "steve 4 None None"
    actD = pD.toString()
    try: 
        assert expD == actD, "Failed steve 4 None None"
        passVal += 1
    except AssertionError as e: print(e)
    testRun += 1


    return passVal, testRun


def peopleGettersTestInitial():
    '''
    fxn: peopleGettersTest()
    does: tests getters for personGood init fields
    params: none
    returns: passVal, int, 1 pass, 0 fail
    '''
    passVal = 0
    testRun = 0
     
    pA = pg.personGood('jojo', 1, 2)


    # personGood object, getName()
    expA = pA.getName()
    try:
        assert expA == 'jojo', "Failed getName()"
        passVal += 1
    except AssertionError as e: print(e)
    testRun += 1

    # personGood object, getSoloVal()
    expB = pA.getSoloVal()
    try:
        assert expB == 1, "Failed getSoloVal()"
        passVal += 1
    except AssertionError as e: print(e)
    testRun += 1
   

    return passVal, testRun


def checkTrustTest():
    '''
    fxn: checkTrustTest()
    does: confirms personGood object that another personGood object interacts with
    is on trusted list. trusted list is init'd with object
    params: none
    returns: passVal, testRun

    NOTE: checkTrust is __ private in personGood, un-private for this test to run
    '''
    passVal, testRun = 0, 0
    expA = pg.personGood('bob', 1, 2, ['josh', 'steven'])
    expB = pg.personGood('josh')
    expC  = pg.personGood('ryan')
    
    try:
        # trusted
        res1 = expA.checkTrust(expB)
        try:
            assert res1 == True, "Failed trusted check"
            passVal += 1
        except AssertionError as e: print(e)
        testRun += 1

        # untrusted
        res2 = expA.checkTrust(expC)
        try: 
            assert res2 == False, "Failed untrusted check"
            passVal += 1
        except AssertionError as e: print(e)
        testRun += 1

    except AttributeError:
        print("\n\tcheckTrust() currently private in personGood(), make un-private for testing\n")
        return 0, 0

    #trusted

    #not trusted

    return passVal, testRun




def shareMod():
    #TODO add to tests[]
    '''
    fxn: setMod()
    does: tests setting mod for key partner, and access modifiers
    - want to prevent caller (or anyone else) from calling __setMod(), just share mode
    Params: none
    returns: passVal, testRun
    '''
    passVal = 0
    testRun = 0

    expA = pg.personGood("alice", 1, 2, ["bob"])
    expB = pg.personGood("bob")

    

    return passVal, testRun

def main():

    print("Test suite: Diffie Hellman Merkle Project")

    testsRun = 0
    passVals = 0

    print("\n\t****Running Tests, in-test alerts:****\n")
    tests = [peopleBasicTest(), peopleGettersTestInitial(), checkTrustTest()]
    for i in tests:
        rval1, rval2 = i
        testsRun += rval2
        passVals += rval1


    percentPassed = str(passVals / testsRun * 100) + "%"

    print("Tests run: " + str(testsRun))
    print("Tests passed: " + str(passVals))
    print("% passed: " + percentPassed)

    
main()
