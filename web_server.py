#! /usr/bin/python3
# this python code use decode function, which must be used in python3.x
from bottle import get, post, run, request, template, route, static_file
from config import IP_ADDRESS, PORT, end, control
import os

currentPath = os.path.dirname(os.path.realpath(__file__))

@route('/static/css/<filename>')
def server_static(filename):
    # currentPath = os.path.dirname(os.path.realpath(__file__))
    return static_file(filename, root=(currentPath+'/static/css'))


@route('/static/fonts/<filename>')
def server_static(filename):
    # currentPath = os.path.dirname(os.path.realpath(__file__))
    return static_file(filename, root=(currentPath+'/static/fonts'))


@route('/static/js/<filename>')
def server_static(filename):
    # currentPath = os.path.dirname(os.path.realpath(__file__))
    return static_file(filename, root=(currentPath+'/static/js'))


@get("/")
def index():
    return template(currentPath+r"/index")


@post("/cmd")
def cmd():
    command_ = request.body.read().decode()
    control(command_)
    return "OK"


try:
    run(host=IP_ADDRESS, port=PORT)
finally:
    end()
