import hashlib
class BitCoinBlockChain:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash=previous_block_hash
        self.transaction_list= transaction_list

        self.block_data=transaction_list+"-"+previous_block_hash
        self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()
bl_lm=int(input("Block Limit: "))
tr_p_bl_lm=int(input("Transaction per block limit: "))
transaction_array=[[ "" for trans_count in range (tr_p_bl_lm)] for block in range(bl_lm)]
for row in range (bl_lm):
    for col in range (tr_p_bl_lm):
        transaction_array[row][col]="X"
for row in range (bl_lm):
    for col in range (tr_p_bl_lm):
        print(transaction_array[row][col],end=" ")
    print()
hash_array=[ "START" for index in range (bl_lm+1)]

transaction_count=0
i=1
tc=0
previous_block_hash="START"
for block_index in range (bl_lm):
    transaction_sum=""
    print( "BLOCK:",block_index+1)
    print( "Initial_Hash:{"+previous_block_hash+"}")
    for transaction_count in range (tr_p_bl_lm):
         tc=tc+i
         print("Trans_Index:",tc)
         sender=input("Enter sender: ")
         receiver=input("Enter Receiver: ")
         amount=input("Enter Amount: ")
         transaction_array[block_index][transaction_count]= "{"+sender+"}"+" sends "+amount+" BitCoins to "+"{"+receiver+"}"
    for count in range (tr_p_bl_lm):
        transaction_sum=transaction_sum+transaction_array[block_index][count]
        
        
    current_block=BitCoinBlockChain("Initial String",transaction_sum)
    hash_array[block_index+1]=current_block.block_hash
    print("Current block hash: ",current_block.block_hash)
    previous_block_hash=current_block.block_hash
   
    
i=1   
for row in range (bl_lm):
    for col in range (tr_p_bl_lm):
        print(transaction_array[row][col],end=" ")
    print()         
i=1
tc=0
previous_block_hash="START"
for block_index in range (bl_lm):
    print( "BLOCK= ",block_index+1)
    print("Previous hash= ["+hash_array[block_index]+"]")
    for transaction_count in range (tr_p_bl_lm):
         tc=tc+i
         print("Trans_Index:",tc,end=" ")
         print(transaction_array[block_index][transaction_count],end=" ")
    print()
    print("Current Block Hash= ["+hash_array[block_index+1]+"]")
    print("____________________________________________________")
         
         
    
    
        

