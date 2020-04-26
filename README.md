# Diffie Hellman Merkel Key Exchange Project
- shared encryption key generation without required key exchange process

# TODO
- do I need trusted lsit? maybe not, likely you'd want to share with whoever you verbally agree
to share with

- `builTrust()` method to say 'we want to do this key build together', afterwards all
get and set methods in class that interact with another person object will have to pass a 
`passTrust()`

- `receiveMod()` 
    - receive mod value from a `person.shareMod(personClass)` call
    - set it to a temp int var
    - call `passTrust()`
    - call `__setMod(value)`: sets self.modVal from shared value

- `receiveSoloVal()`
    - receive soloValue from `person.shareSoloVal(personClass)` call
    - set it to temp int var
    - call `passTrust()`
    - call `__setSolo(value)`: sets self.soloVal from shared value

- keyGen class, employ with startegy pattern into personGood class

- personEvil class

- keySniff class, employ with startegy pattern inot personEvil class

- (T) person class, parent class for personGood personEvil


## TOC

## Files

## High Level Use


**Diffie Hellman Merkel Oneway function**
* `Y^x (mod P)

* Generate shared value format: 
    - Alice: `Y^A (mod P) = a`
    - Bob: `Y^B (mod P) = b`

* Generate private key format:
    - Alice: `b^A (mod P) = PrivKey`
        - b: shared from Bob
        - A: private to Alice
    - Bob: `a^B (mod 11) = PrivKey`
        - a: shared from Alice
        - B: private to Bob
    - What is PrivKey:
        - a jointly-known private key that Alice and Bob can use to symmetrically encrypt messages
        to each other

* Alice and Bob agree on Y and P publicly

* Alice use (A, a):
    - Alice secret: `A`
    - `Y^A (mod P) = a`
    - Share `a` publicly`

* Bob use (B, b):
    - Bob secret: `B`
    - `Y^B (mod P) = b`
    - Share `b` pubicly

* Eve will get:
    - Y, P, a, b

**Code Steps**
- Create 3x people classes: `alice, bob, eve`
....


## Classes

## Specific Use

