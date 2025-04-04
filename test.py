from web3 import Web3 # type: ignore

NUM_OF_ACCOUNTS = 1300
w3 = Web3(Web3.HTTPProvider("https://testnet-rpc.superposition.so"))

disperse_contract_address = Web3.to_checksum_address("0x5E4E54c0Cc7DaFAe4824BB13873eE5f178984847")

disperse_abi = [
    {
        "constant": False,
        "inputs": [
            {"name": "recipients", "type": "address[]"},
            {"name": "values", "type": "uint256[]"}
        ],
        "name": "disperseEther",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    }
]

disperse_contract = w3.eth.contract(address=disperse_contract_address, abi=disperse_abi)

target_address = Web3.to_checksum_address("0x0949A6F2eA643c4F088419f59D9ed42FAA63c283")
recipients = [target_address] * NUM_OF_ACCOUNTS
values = [0] * NUM_OF_ACCOUNTS

sender_address = Web3.to_checksum_address("0x0949A6F2eA643c4F088419f59D9ed42FAA63c283")
private_key = "..."

nonce = w3.eth.get_transaction_count(sender_address)
gas_price = w3.eth.gas_price

transaction = disperse_contract.functions.disperseEther(recipients, values).build_transaction({
    "from": sender_address,
    "value": 0,
    "gas": 80000000,
    "gasPrice": gas_price,
    "nonce": nonce
})

signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

print("Transaction sent. Hash:", tx_hash.hex())
