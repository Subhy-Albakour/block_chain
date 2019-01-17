import json
import hashlib


class BlockHeader(object):

    def __init__(self, index, previous_hash, timestamp, nonce):
        self.index=index
        self.previous_hash=previous_hash
        self.timestamp=timestamp
        self.nonce=nonce

    def to_dict(self):
        res={}
        res['index']=self.index
        res['previous_hash']=self.previous_hash
        res['timestamp']=self.timestamp
        res['nonce']=self.nonce

        return res
        

    def to_json(self):
        d=self.to_dict()
        json_string=json.dumps(d,sort_keys=True) # we sort to get a unique representation
        return json_string

    def set_nonce(self, new_nonce):
        
        self.nonce= new_nonce
        
        return

    def get_hash(self):

        json_string=self.to_json()
        encoded=json_string.encode("utf-8")
        hashed=hashlib.sha256(encoded)
        res=hashed.hexdigest()    

        return res

