import json
import os

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


def read_block_file(file_path):
    block_file= open(file_path)
    block_dict=json.load(block_file)
    block=read_block(block_dict)
    return block

def read_blocks_directory(directory):
    blocks=[]
    filenames=sorted(os.listdir(directory))
    for filename in filenames :
        file_path=directory+"/" +filename
        block=read_block_file(file_path)
        blocks.append(block)
    return blocks

def read_chains_directory(directory):
    chains=[]
    filenames=sorted(os.listdir(directory))
    for filename in filenames:
        #filenames.append(filename)
        with open(directory+"/" +filename) as f:

            chain_json=json.load(f)
            chain=read_chain(chain_json)
            chains.append(chain)

    return (chains, filenames)
    

def read_block_json(block_json):
    # Reads a block in json format

    block=json.loads(block_json)
    block_obj=read_block(block)

    return block_obj

def read_chain(chain):
    # read the chain from a json str
    # Returns a list of Block
    # This method does not do any checking
    res=[read_block(block_dict) for block_dict in chain]
    return res

    
