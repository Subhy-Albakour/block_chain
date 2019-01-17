class Blockchain(object):

    def __init__(self):
        self.chain = [] # contains the blockchain
        self.wallets = dict() # Contains the amount of coin each user owns
        self.wallets["admin"] = 100000000000000

    def add_block(self, block):
        # Add a block to the chain
        # It needs to check if a block is correct
        # Returns True if the block was added, False otherwise
        pass

    def update_wallet(self, block):
        # Update the values in the wallet
        # We assume the block is correct
        pass

    def check_legal_transactions(self, block):
        # Check if the transactions of a block are legal given the current state
        # of the chain and the wallet
        # Returns a boolean
        pass
