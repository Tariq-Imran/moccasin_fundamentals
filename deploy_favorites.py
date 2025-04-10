from vyper import compile_code
from web3 import Web3 

# Anvil
MY_ADDRESS = "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"
PRIVATE_KEY = "00x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a"

def main():
    print("Let's read the vyper code and deploy it!")
    with open("favorites.vy", "r") as favorite_file:
        favorites_code= favorite_file.read() 
        compliation_details = compile_code(favorites_code, output_formats= ["bytecode", "abi"])
        print(compliation_details)

    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    favorites_contract = w3.eth.contract(bytecode=compliation_details["bytecode"], 
    abi=compliation_details["abi"])

    # To deploy this, we must build a transaction
    print("Building the transaction...")
    
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)

    transaction = favorites_contract.constructor().build_transaction(
        {
            "nonce": nonce,
            "from": MY_ADDRESS,
            "gasPrice": w3.eth.gas_price
        }
    )
    
    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
    print(signed_transaction)



if __name__ == "__main__":
    main()

