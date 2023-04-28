from Crypto import Random
from Crypto.PublicKey import RSA
import binascii 
from Crypto.Cipher import PKCS1_v1_5
import datetime
import collections
from collections import OrderedDict
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
#prac 1 b
#a simple client class that will generate private and public key by using the builtin Pytyhon RSA algorithm and ttest it (with class)
class Client:
    def __init__(self) -> None:
        random = Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)
        
    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format = 'DER')).decode('ascii')
    

#transaction class to send & receive money and test it
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
transaction = []

Manish = Client()
Disha = Client()
t1 = Transaction( Disha, Manish.identity, 15.0)
t1.sign_tram()
display_transaction(t1)

from Crypto import Random
from Crypto.PublicKey import RSA
import binascii 
from Crypto.Cipher import PKCS1_v1_5
import datetime
import collections
from collections import OrderedDict
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
