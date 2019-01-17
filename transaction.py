class Transaction(object):

    def __init__(self, index, sender, receiver, amount):

        self.index=index
        self.sender=sender
        self.receiver=receiver
        self.amount=amount


    def to_dict(self):
        d={}
        
        d['index']=self.index
        d['sender']=self.sender
        d['receiver']=self.receiver
        d['amount']=self.amount

        return d
