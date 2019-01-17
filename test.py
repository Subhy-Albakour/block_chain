import block
import block_header
import block_reader
import blockchain

import json

import imp
imp.reload(block_header)
imp.reload(block)


with open('blocks_to_prove/block0.json') as f:
    data = json.load(f)
   

block_obj=block_reader.read_block(data)
block_obj.make_proof_ready()

# header=block_reader.read_header(data['header'])
# print(header.index)

# print(block)
# print(block.header)
# print(block.transactions[0].receiver)

