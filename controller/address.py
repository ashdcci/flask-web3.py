from flask import Flask,jsonify, request
from web3 import Web3, HTTPProvider, IPCProvider
import sample_flask_app.config.devConfig as config
import os, sys, json, logging, numpy
from web3.contract import ConciseContract


class AddressController(object):
    def __init__(self):
       self.w3 = Web3(HTTPProvider('https://rinkeby.infura.io/'+config.WEB3_TOKEN))
       self.gasPriceGwei = 584
       self.gasLimit = 52968
       #Chain ID of Ropsten Test Net is 3, replace it to 1 for Main Net
       self.chainId = self.w3.net.chainId
       self.w3.eth.defaultAccount = config.ETH_MY_ADDR


    def index(self):
        return "address controller index method call"

    def getBalance(self):
        if request.method == 'POST':
            try:
                if request.form.get('address') is None : raise ValueError(' Require Fields are Missing.')
                address = request.form.get('address')
                balance = self.w3.toWei(self.w3.eth.getBalance(address),'ether')
                print(balance)


                return jsonify({
                        "status":1,
                        "message":"address balance",
                        "balance": float(balance)
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

    def error_handling(self):
        return 'Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                         sys.exc_info()[1],
                                         sys.exc_info()[2].tb_lineno)