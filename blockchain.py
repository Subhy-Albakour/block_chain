class Blockchain(object):

    def __init__(self):
        self.chain = [] # contains the blockchain
        self.wallets = dict() # Contains the amount of coin each user owns
        self.wallets["admin"] = 100000000000000

    def add_block(self, block):
        # Add a block to the chain
        # It needs to check if a block is correct
        # Returns True if the block was added, False otherwise
        legal=self.check_legal_transactions(block)
        if block.is_proof_ready() and legal :
            self.chain.append(block)
            self.update_wallet(block)
            return True
        return False


    def update_wallet(self, block):
        # Update the values in the wallet
        for transaction in block.transactions:
            # need to be atomic
            self.wallets[transaction.sender]=self.wallets.get(transaction.sender,0) - transaction.amount
            self.wallets[transaction.receiver]=self.wallets.get(transaction.receiver,0) + transaction.amount
        return 


    def check_legal_transactions(self, block):
        # Check if the transactions of a block are legal given the current state
        # of the chain and the wallet
        # Returns a boolean
        wallets_copy=self.wallets.copy()
        for transaction in block.transactions:
            sender_blanace=wallets_copy[transaction.sender]
            if sender_blanace < transaction.amount:
                block.invalid_transactions.append((transaction,sender_blanace))
                return False
            else:
                wallets_copy[transaction.sender]=wallets_copy.get(transaction.sender,0) - transaction.amount
                wallets_copy[transaction.receiver]=wallets_copy.get(transaction.receiver,0) + transaction.amount
        return True
