from block import Block
import datetime

block_chain = [Block.create_genesis_block()]
print("The genesis block has been created!")
print("Hash: %s" %block_chain[-1].hash)

n = 10

for i in range(1,n+1):
    block_chain.append(Block(block_chain[-1].hash,"DATA!",datetime.datetime.now()))
    print("Block #%d has been created" %i)
    print("Block #%d hash: %s" %(i,block_chain[i].hash))