from Crypto import Random
from Crypto.PublicKey import RSA
import binascii 
from Crypto.Cipher import PKCS1_v1_5
import datetime
import collections
from collections import OrderedDict
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

class Client:
    def __init__(self) -> None:
        random = Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)
        
    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format = 'DER')).decode('ascii')
    
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity
        return collections.OrderedDict({
            "sender": identity,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp
        })
    def sign_tram(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf-8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

def display_transaction(transaction):
    dict = transaction.to_dict()
    print("Sender:", dict["sender"])
    print("---------")
    print("Receiver:", dict["receiver"])
    print("---------")
    print("Amount:", dict["amount"])
    print("---------")
    print("Timestamp:", dict["timestamp"])
    print("---------")

def dump_blockchain(self):
    print("Number of blocks in the chain:"+str(len(self)))
    for x in range (len(TPCoins)):
        block_temp=TPCoins[x]
        print("block#"+str(x))
        for transaction in block_temp.verified_transactions:
            display_transaction(transaction)
            print('-------------')
        print('=============================')

class Block:
    def __init__(self):
      self.verified_transactions=[]
      self.previous_block_hash=""
      self.Nounce=""

Sejal=Client()
t0 = Transaction("Genesis", Sejal.identity,500.0)
block0=Block()
block0.previous_block_hash=None
Nounce=None
block0.verified_transactions.append(t0)
digest=hash(block0)
last_block_hash=digest

TPCoins=[]
TPCoins.append(block0)
dump_blockchain(TPCoins)

