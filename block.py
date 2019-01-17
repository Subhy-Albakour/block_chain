import json
import hashlib


class Block(object):

    def __init__(self, header, transactions):

        # header is a BlockHeader and transaction is a list of Transaction
        self.header=header
        self.transactions=transactions
        self.N_STARTING_ZEROS = 4
        

    def to_dict(self):
        # Turns the object into a dictionary
        # There are two fields: header and transactions
        # The values are obtained by using the to_dict methods
        d={}
        d['header']=self.header.to_dict()
        d['transactions']=[tran.to_dict() for tran in self.transactions]

        return d

    def to_json(self):
        # Transforms into a json string
        # use the option sort_key=True to make the representation unique
        d=self.to_dict()
        json_string=json.dumps(d,sort_keys=True) # we sort to get a unique representation
        return json_string
        

    def is_proof_ready(self):
        # Check whether the block is proven
        # For that, make sure the hash begins by N_STARTING_ZEROS
        s=self.header.get_hash()
        binary=bin(int(s,16))[2:] #take the binary representation and exclude the first 2 elements (0b) at the beginning of the code 
        prefix=binary[:self.N_STARTING_ZEROS]

        zeros="".join(['0' for i in range(self.N_STARTING_ZEROS)])
        print("---------------------------------------------")
        print (len(binary))
        print(prefix)
        print(binary)
        print(zeros)
        return prefix==zeros


    def make_proof_ready(self):
        print("--------------------------------++++++++++++++++++++++++++++++")

        nonce=0
        count=0
        limit=100
        while count<limit:
            self.header.set_nonce(nonce)
            if self.is_proof_ready():
                return 
            nonce=nonce+1
            count=count+1
        return


import block_header
import block_reader
import blockchain

import json

import imp
imp.reload(block_reader)

imp.reload(block)


with open('blocks_to_prove/block0.json') as f:
    data = json.load(f)
   

block_obj=block_reader.read_block(data)
block_obj.make_proof_ready()
