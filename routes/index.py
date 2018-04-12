#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import environ
import sys
sys.path.append("..")
from flask import Flask, request, render_template,  abort, redirect, url_for, session, escape, Blueprint, jsonify
#from flask_mongoengine import MongoEngine
from werkzeug.utils import secure_filename


### Utils Class Calling
from ..class1 import MyClass
theclass = MyClass()

### Controller Class Calling
from ..controller.address import AddressController
from ..controller.contract import ContractController
addressController = AddressController()
contractController = ContractController()

class Routeclass(object):
    routes = Blueprint('api', __name__)

    @routes.route('/address')
    def address():
        return addressController.index()

    @routes.route('/contract')
    def contract():
        return contractController.index()

    @routes.route('/getBlockNumber')
    def getBlockNumber():
        return contractController.getBlockNumber()

    @routes.route('/sendToken', methods=['POST'])
    def sendToken():
        return contractController.send_token()

    @routes.route('/sendToAddr',methods=['GET', 'POST'])
    def sendToAddr():
        return contractController.sendToAddr()