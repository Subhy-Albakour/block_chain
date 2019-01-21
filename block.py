import json
import hashlib


class Block(object):

    def __init__(self, header, transactions,zeros=4):

        # header is a BlockHeader and transaction is a list of Transaction
        self.header=header
        self.transactions=transactions
        self.N_STARTING_ZEROS = zeros
        self.invalid_transactions=[]

    def set_zeros(self,n):
        self.N_STARTING_ZEROS=n  
        

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
        zeros="".join(['0' for i in range(self.N_STARTING_ZEROS)])
        prefix=s[:self.N_STARTING_ZEROS]
        return prefix==zeros


    def make_proof_ready(self):


        nonce=0
        while True:
            self.header.set_nonce(nonce)
            if self.is_proof_ready():
                return 
            nonce=nonce+1
        return
    

