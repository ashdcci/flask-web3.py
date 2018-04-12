from flask import Flask,jsonify

class MyController(object):
    def index(self):
        return "index method call"
