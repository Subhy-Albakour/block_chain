import os
import time
import json
import block
import block_header
import block_reader
import blockchain
from blockchain import Blockchain



##----------- Exercise 11--------------

#The directory blocks, contains the serialization of some blocks.
#How many transactions are in each block?

#Implementation
def count_transactions(blocks_directory):
    blocks_sizes=[]
    for filename in os.listdir(blocks_directory):
        with open(blocks_directory+"/" +filename) as f:

            block_dict=json.load(f)
            block=block_reader.read_block(block_dict)
            blocks_sizes.append((filename[:-5],len(block.transactions)))
    print("block sizes in the directory:" +blocks_directory)
    print(blocks_sizes)
    avg=sum([p[1] for p in blocks_sizes])/len(blocks_sizes)
    print("average number of transactions: "+ str(avg))


## ------------Ecercise 18 ----------------
#For all blocks in the directory blocks to prove, prove it and give
#the nonce and the value of the hash function.

# Implementation

def prove_blocks(blocks_directory):
    filenames=sorted(os.listdir(blocks_directory))
    print("block : nonce, hash")
    for filename in filenames :
        with open(blocks_directory+"/" +filename) as f:

            block_dict=json.load(f)
            block=block_reader.read_block(block_dict)
            block.make_proof_ready()
            # print("----------------------")
            # print("block File : " + filename)
            # print("Hash Value : " + block.header.get_hash())
            # print("Nonce : " + str(block.header.nonce))
            print(filename[:-5]+" : "+str(block.header.nonce)+" , "+block.header.get_hash())







# -------------------Execrise 19-------------------
#Take one block from the directory blocks to prove and observe
#what happens when you increase the number of requested starting zero in the
#proof. From which number of leading zeros does the computation of the proof
#takes more than one minute? How many leading zeros are required in the Bitcoin
#system?

# Implementation


def execution_time_analize(block_file,leading_zeros_list):
    block=block_reader.read_block_file(block_file)

    exec_times=[]
    for num in leading_zeros_list:
        block.set_zeros(num)
        start = time.time()
        block.make_proof_ready()
        end = time.time()
        exec_times.append(end-start)

    import matplotlib.pyplot as plt
    plt.plot(leading_zeros_list, exec_times, 'ro-')
    plt.xlabel("number of leading zeros")
    plt.ylabel("execution time in seconds")
    plt.show()


# -------------------Execrise 23-------------------
#For each blockchain in the directory blockchain wallets, compute
#the value of the wallet of each user. To do so, create a Blockchain object and
#call the add block method for each block.

# Implementation
def compute_wallets(chain_directory):
    chains_list,filenames=block_reader.read_chains_directory(chain_directory)

    block_chains=[]
    for chain in chains_list:
        block_chain=Blockchain()
        for block in chain:
            block_chain.add_block(block)
        block_chains.append(block_chain)

    for i in range(len(block_chains)):
        block_chain=block_chains[i]
        filename=filenames[i]
        print("------------User Balances-------------")
        print(filename)
        print(block_chain.wallets)


# -------------------Execrise 25-------------------
#For each blockchain in the directory blockchain incorrect, check
#if it is correct. If a blockchain is incorrect, give the index of the first incorrect
#block and if necessary the index of the first incorrect transaction.

# Implementation
def detect_incorrect(chain_directory):

    chains_list,filenames=block_reader.read_chains_directory(chain_directory)
    print("chain : status, block, transaction, amount, sender balance")
    for i in range (len(chains_list)):
        chain=chains_list[i]
        filename=filenames[i]
        block_chain=Blockchain()
        good=True
        
        for block in chain:
            added=block_chain.add_block(block)
            if not added :
                good=False
                if block.is_proof_ready():

                    print("{} : incorrect, {}, {}, {}, {}".format(filename[:-5],block.header.index,block.invalid_transactions[0][0].index,
                    block.invalid_transactions[0][0].amount,block.invalid_transactions[0][1]))

                else :
                    print("{}, Not Proved, {}".format(filename[:-5],block.header.index))
 
                break # when there is an invalid block, no need to continue checking other blocks 
        if good:    
            print(filename[:-5]+": correct")





##----------- Exercise 11--------------
# --------------Results----------------

# uncomment the following to see the results of Exercise 11

# blocks_directory="blocks"
# count_transactions(blocks_directory)

##----------- Exercise 18--------------
# --------------Results----------------

# uncomment the following to see the results of Exercise 18

# blocks_directory="blocks_to_prove"
# prove_blocks(blocks_directory)

##----------- Exercise 19--------------
# --------------Results----------------

# uncomment the following to see the results of Exercise 19

# block_file="blocks_to_prove/block1.json"
# leading_zeros_list=range(3,5)
# execution_time_analize(block_file,leading_zeros_list)

##----------- Exercise 23--------------
# --------------Results----------------

# uncomment the following to see the results of Exercise 23

# chain_directory="blockchain_wallets"
# compute_wallets(chain_directory)

##----------- Exercise 25--------------
# --------------Results----------------

chain_directory="blockchain_incorrect"
detect_incorrect(chain_directory)



