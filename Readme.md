# Ranploy

Tool to generate the transaction data to deploy bytecode to a new contract. 
Use this if you already have the bytecode and want to create a new Ethereum smart contract with that bytecode.

It's actually useful if you want to create contracts with a random hex string for code.

## Example

```shell
$ python main.py --bytecode 11223344
6004600d60003960046000f30011223344
```

You then need to create a transaction and use this as the payload data

```
web3.eth.sendTransaction({from: "0x8d26D6d498a01243820154c7Ddb63b47c00DbF6e", data: "0x6004600d60003960046000f30011223344"})
```

Your contract will have this bytecode
```
web3.eth.getCode("0xDdB083baD281D7242FF69E36c7565b003785cb1A")
'0x11223344'
```

