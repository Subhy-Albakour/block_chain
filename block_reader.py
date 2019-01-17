import json

from block_header import BlockHeader
from transaction import Transaction
from block import Block
from blockchain import Blockchain


def read_header(header):
    # Implement these functions to help you
    # Takes a dictionary as an input
    index=header['index']
    timestamp=header['timestamp']
    previous_hash=header['previous_hash']
    nonce=header['nonce']
    block_header=BlockHeader(index,previous_hash,timestamp,nonce)

    return block_header

def read_transaction(transaction):
    
    index=transaction['index']
    sender=transaction['sender']
    receiver=transaction['receiver']
    amount=transaction['amount']

    transaction_obj=Transaction(index,sender,receiver,amount)

    return transaction_obj

def read_block(block):
    # Reads a block from a dictionary
    header_dict=block['header']
    trnasaction_dicts=block['transactions']
    header=read_header(header_dict)
    transactions=[read_transaction(tran_dict) for tran_dict in trnasaction_dicts ]

    block_obj=Block(header,transactions)

    return block_obj

    

def read_block_json(block_json):
    # Reads a block in json format

    block=json.loads(block_json)
    block_obj=read_block(block)

    return block_obj

def read_chain(chain):
    # read the chain from a json str
    # Returns a list of Block
    # This method does not do any checking
    pass
