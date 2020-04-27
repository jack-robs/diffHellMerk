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

def testGetters():
    '''
    Fxn: testGetters()
    Does: test @property use for class fields
    Params: none
    returns passVal, testRun
    '''
    passVal, testRun = 0, 0

    p0 = pg.personGood("bob", 1, 2)

    try:
        assert "bob" == p0.personName, "Failed @property personName"
        passVal += 1
    except AssertionError as e: print(e)
    testRun += 1


    return passVal, testRun


def testSetters():
    '''
    fxn: testSetters()
    Does: test @val.setter methods in personGood
    Params: none
    returns: passVal, testRun
    '''
    passVal, testRun = 0, 0

    # soloVal and modVal not set
    p0 = pg.personGood("bob")
    p0.soloVal = 1
    p0.modVal =  2
    try:
        assert 1 == p0.soloVal, "Failed soloVal set, solo/mod None"
        passVal += 1
        assert 2 == p0.modVal, "Failed modVal set, solo/mod None, solo set first"
        passVal += 1
    except AssertionError as e: print(e)
    testRun += 2

    p1 = pg.personGood("joe")
    p0.modVal = 2
    p0.soloVal = 1
    try:
        assert 2 == p0.modVal, "Failed modVal set, solo/mod None, mod set first"
        passVal += 1
        assert 1 == p0.soloVal, "Failed soloVal set, solo/mod None, mod setFirst"
        passVal += 1

    except AssertionError as e: print(e)
    testRun += 2

    # soloVal set in instantiating, set modVal
    p2 = pg.personGood("anna", 4)
    p0.modVal = 5
    try:
        assert 5 == p0.modVal, "Failed modval set, solo set in instantiation"
        passVal += 1
    except AssertionError as e: print(e)
    testRun += 1

    # set soloVal, mod still none
    p3 = pg.personGood("raul")
    p3.soloVal = 6
    try:
        assert 6 == p3.soloVal, "Failed soloVal set, modVal none"
        passVal +=1
    except AssertionError as e: print(e)
    testRun += 1

    # set modVal, sol0 still none
    p4 = pg.personGood("christine")
    p4.soloVal = 3
    try:
        assert 3 == p4.soloVal, "Failed modVal set, soloVal none"
        passVal += 1
    except AssertionError as e: print(e)
    testRun += 1

    # modVal set in instantiating, set soloVal
    p5 = pg.personGood("joejoe", modVal=5)
    p5.soloVal = 4
    try:
        assert 4 == p5.soloVal, "Failed soloVal set, modVal set in inst."
        passVal += 1
    except AssertionError as e: print(e)
    testRun += 1
    
    # soloVal attempt, greater than mod, expect fail
    p6 = pg.personGood("jojojojo", modVal=5)
    try:
        p6.soloVal = 6
        print("Failed excepted soloVal > modVal logic deny")
    except ValueError:
        passVal += 1
    testRun += 1

    # mod val attempt, less than soloVal, expect fail
    p7 = pg.personGood("hello", soloVal=2)
    try:
        p7.modVal = 1
        print("Failed expected modVal < soloVal logic deny")
    except ValueError:
        passVal += 1
    testRun += 1


    return passVal, testRun


def testShareKey():
    '''
    Fxn: testModMath()
    Does: tests modMath class
    Params: none
    retunrs: passVal, testRun
    '''
    passVal, testRun = 0, 0
    #set copy in @property pubShare in class personGood to 3 for testing initially
    # will have to test throughput via an encrypt/decrypt test, not sure how to expose 
    # __privKey in personGood and keep intent of algorithm otherwise
    p0 = pg.personGood("bob", 7, 11)
    p0.makeShare()
    a0 = p0.pubShare
    try:
        assert a0 == 2, "incorrect pubShare gen'd, given 7^priv (mod 11), priv == 3 for test"
        passVal += 1
    except AssertionError as e: print(e)
    testRun += 1
    
    return passVal, testRun

def main():

    print("Test suite: Diffie Hellman Merkle Project")

    testsRun = 0
    passVals = 0

    tests = [peopleBasicTest, testGetters, testSetters, testShareKey]
    print("\n\t****Running Tests, in-test alerts:****\n")
    for i in tests:
        rval1, rval2 = i()
        testsRun += rval2
        passVals += rval1


    percentPassed = str(passVals / testsRun * 100) + "%"

    print("\n\nTests run: " + str(testsRun))
    print("Tests passed: " + str(passVals))
    print("% passed: " + percentPassed)

    
main()
