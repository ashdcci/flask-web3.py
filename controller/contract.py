from flask import Flask,jsonify, request
# import numpy
from web3 import Web3, HTTPProvider, IPCProvider

import sample_flask_app.config.devConfig as config
import os, sys, json, logging, numpy
from web3.contract import ConciseContract
from bson import json_util, ObjectId
from web3.middleware import geth_poa_middleware
# import json
# import logging
# import sys
# from web3.middleware.pythonic import (
#     pythonic_middleware,
#     to_hexbytes,
# )

# size_extraData_for_poa = 200   # can change
# pythonic_middleware.__closure__[2].cell_contents['eth_getBlockByNumber'].args[1].args[0]['extraData'] = to_hexbytes(size_extraData_for_poa, variable_length=True)
# pythonic_middleware.__closure__[2].cell_contents['eth_getBlockByHash'].args[1].args[0]['extraData'] = to_hexbytes(size_extraData_for_poa, variable_length=True)

class ContractController(object):
    
    def __init__(self):
       self.w3 = Web3(HTTPProvider(config.WEB3_URL))
       self.gasPriceGwei = 584
       self.gasLimit = 52968
       #Chain ID of Ropsten Test Net is 3, replace it to 1 for Main Net
       self.chainId = self.w3.net.chainId
       print(self.chainId)
       self.w3.eth.defaultAccount = config.ETH_MY_ADDR
       self.w3.middleware_stack.inject(geth_poa_middleware, layer=0)
       print(self.w3.version.node)
       print(config.WEB3_URL)

    def index(self):
        return jsonify({"msg":"contract controller index method call"}) , 200

    def send_token(self):
        if request.method == 'POST':
            try:
                if request.form.get('to_address') is None : raise ValueError(' Require Fields are Missing.')

                ### variable defination
                destAddress = request.form['to_address']
                contractAddress = config.ETH_CONTRACT_ADDR 
                txValue = self.w3.toHex(self.w3.toWei('0.7854', 'ether'))
                # txData = self.w3.toHex('oh hai mark')
                transferAmount = 8
                
                ### contract instance call
                abiArray = json.load(open('./config/wallet.json'))
                contract = self.w3.eth.contract(address=contractAddress, abi=abiArray )
                print(contract)
                ### get transaction count 
                count = self.w3.eth.getTransactionCount(config.ETH_MY_ADDR)

                ### get balance before send
                # beforeBalance = contract.functions.balanceOf(config.ETH_MY_ADDR)
                beforeBalance = contract.functions.balanceOf(config.ETH_MY_ADDR).call()
                # data = json.loads(json_util.dumps(beforeBalance))
                print('to_address', destAddress)
                print('tx count',count)
                # print('tx count',count, self.w3.toHex(self.w3.toInt(self.gasPriceGwei*1e9)), self.w3.toHex(self.w3.toWei(self.gasPriceGwei, 'ether')) )
                print('before balance',beforeBalance)
                # self.w3.eth.enable_unaudited_features()
                # dataTx = contract.transact({
                #     'from': config.ETH_MY_ADDR,
                #     # 'to': destAddress,
                #     # 'value': 5,
                #     # 'gas': self.gasLimit
                # }).transfer(destAddress, transferAmount)

                # dataTx = 

                unicorn_txn = contract.functions.transfer(
                    destAddress,
                    transferAmount,
                ).buildTransaction({
                    'chainId': self.chainId,
                    'gas': self.gasLimit,
                    'gasPrice': self.gasPriceGwei,
                    'nonce':  self.w3.toHex(count),
                })
                print(unicorn_txn)
                private_key = config.ETH_PRIV_KEY
                signed_txn = self.w3.eth.account.signTransaction(unicorn_txn, private_key=private_key)
                print('signTx hash ', signed_txn)
                receipt = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction) 
                print(self.w3.toHex(self.w3.sha3(signed_txn.rawTransaction)))


                print(self.w3.eth.getTransaction(self.w3.toHex(receipt)))

                # print(destichk,mychk)
                # receipt = self.w3.eth.sendTransaction({
                #     'to': contractAddress,
                #     # 'from': config.ETH_MY_ADDR,
                #     'data': contract.functions.transfer(destAddress, transferAmount).transact(),
                #     # 'gas': self.gasLimit,
                #     # 'gasPrice':self.gasPriceGwei
                #     # 'value': 0
                #     })
                
                # receipt = contract.transact({'from': config.ETH_MY_ADDR}).transfer(destAddress, transferAmount)

                
                # print(dataTx)
                ### set enable_unaudited_features
                # self.w3.eth.enable_unaudited_features()


                # ### make raw transaction json
                # rawTransaction = {
                #     'nonce': self.w3.toHex(count),
                #     'gasPrice': self.gasPriceGwei * 1e9,
                #     'gas': self.gasLimit,
                #     'to': contractAddress,
                #     'from': config.ETH_MY_ADDR,
                #     'value': "0x0",
                #     'data': contract.functions.transfer(destAddress, transferAmount).transact(),
                #     'chainId': self.chainId
                # }
                # print('raw tx hash',rawTransaction)

                # ### signed transaction
                # signed = self.w3.eth.account.signTransaction(rawTransaction, config.ETH_PRIV_KEY)

                # ### get receipt
                # receipt = self.w3.eth.sendRawTransaction(signed.rawTransaction)
                print('tx hash',self.w3.toHex(receipt))

                # # get balance after send
                afterBalance = contract.call().balanceOf(config.ETH_MY_ADDR)
                print('after balace',afterBalance)


                return jsonify({
                            "status":1,
                            "message":"send token api called",
                            # "tx_hash": self.w3.toHex(receipt),
                            "token_before_send": beforeBalance,
                            "token_after_send": afterBalance
                        }) , 200

            except Exception as e:
                    print(e)
                    return jsonify({
                        "status":0,
                        "message":"exception fetch in performing operation",
                        "ex_msg": self.error_handling()
                    }) , 500
        else:
            return jsonify({
                    "status":0,
                    "message":"Method not Allowed",
                }) , 403            

    def getBlockNumber(self):
        return jsonify({"status":1,"msg":"Latest blockNumber","block": self.w3.eth.blockNumber}) , 200

    def error_handling(self):
        return 'Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                         sys.exc_info()[1],
                                         sys.exc_info()[2].tb_lineno)
    def sendToAddr(self):
        if request.method == 'POST':
            try:
                print(request.form.get('to_address'))
                if request.form.get('to_address') is None : raise ValueError('Require Fields are missing')
                destAddress = request.form['to_address']
                #destAddress = '0x213A85d570e3580b18A079602e3fFdD541C6C651'
                #contractAddress = config.ETH_CONTRACT_ADDR 
                #txValue = self.w3.toHex(self.w3.toWei('0.7854', 'ether'))
                #txData = self.w3.toHex(self.w3.toAscii('oh hai mark'))
                
                
                count = self.w3.eth.getTransactionCount(config.ETH_MY_ADDR)
                
                self.w3.eth.enable_unaudited_features()
                rawTx = {
                    'nonce': self.w3.toHex(count),
                    'gasPrice': self.gasPriceGwei * 1e9,
                    'gas': self.gasLimit,
                    'to': destAddress,
                    'from': config.ETH_MY_ADDR,
                    'value': self.w3.toWei('0.84487', 'ether'),
                    'chainId': self.chainId
                }

                signed = self.w3.eth.account.signTransaction(rawTx, config.ETH_PRIV_KEY)
                
                receipt = self.w3.eth.sendRawTransaction(signed.rawTransaction)

                return jsonify({
                    "status":1,
                    "message":"send to address api call",
                    "getTransactionCount": count,
                    "tx_hash": self.w3.toHex(receipt)
                }) , 200

            except Exception as e:
                print(e)
                return jsonify({
                    "status":0,
                    "message":"exception fetch in performing operation",
                    "ex_msg": self.error_handling()
                }) , 500

        else:
            return jsonify({
                    "status":0,
                    "message":"Method not Allowed",
                }) , 403