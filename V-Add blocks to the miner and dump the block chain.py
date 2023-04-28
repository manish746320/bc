from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
import datetime
import binascii
from collections import OrderedDict
import collections
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
import hashlib

print("Sejal,14")
class Client:
    def __init__(self):
        random = Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class Transaction:
    def __init__(self, sender, recipent, value):
        self.sender = sender
        self.recipent = recipent
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity
        return collections.OrderedDict({
            'sender': identity,
            'recipent': self.recipent,
            'value': self.value,
            'time': self.time
        })

    def sign_tran(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

def display_transaction(transaction):
    # for transaction in transactions:
    dict = transaction.to_dict()
    print("sender:" + dict['sender'])
    print('-----')
    print("recipent:" + dict['recipent'])
    print('-----')
    print("value:" + str(dict['value']))
    print('-----')
    print("time:" + str(dict['time']))
    print('-----')

def dump_blockchain(self):
    print("Number of blocks in the chain:" + str(len(self)))
    for x in range (len(TPCoins)):
        block_temp=TPCoins[x]
        print("block#" + str(x))
        for transaction in block_temp.verified_transaction:
            display_transaction(transaction)
            print("...............")
            print("====================")

class Block:
    def __init__(self):
        self.verified_transaction=[]
        self.previous_block_hash=""
        self.Nonce=""

def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message,difficulty=1):
    assert difficulty>=1 #debugging
    prefix= '1'* difficulty #verify diffficulty
    print ("prefix",prefix)
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))
        print("Testing --> " + digest)
        if digest.startswith(prefix): 
            print("After " + str(i) + "iterations found nounce " + digest)
            return i
mine("Sejal", 3)

transactions = []

Sejal = Client()
Kinjal= Client()
Komal = Client()

t0=Transaction(
    "Genesis",
    Sejal.identity,
    500.0
)
t1 = Transaction(
    Sejal,
    Kinjal.identity,
    15.0
)
t1.sign_tran()
transactions.append(t1)

t2 = Transaction(
    Kinjal,
    Komal.identity,
    17.0
)

t2.sign_tran()
transactions.append(t2)

t3 = Transaction(
    Komal,
    Kinjal.identity,
    10.0
)

#blockchain
TPCoins=[]

block0=Block()
block0.previous_block_hash=None
Nonce=None
block0.verified_transaction.append(t0)
digest=hash(block0)
last_block_hash = digest
last_block_hash=digest 
TPCoins.append(block0)

block1=Block()
block1.previous_block_hash=last_block_hash
block1.verified_transaction.append(t1)
block1.verified_transaction.append(t2)
block1.Nonce=mine(block1,2)
digest=hash(block1)
last_block_hash=digest
TPCoins.append(block1)

block2=Block()
block2.previous_block_hash=last_block_hash
block2.verified_transaction.append(t3)
Nonce=mine(block2,2)
block2.Nonce=mine(block2,2)
digest=hash(block2)
last_block_hash=digest
TPCoins.append(block2)

dump_blockchain(TPCoins)







