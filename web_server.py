#! /usr/bin/python3
# this python code use decode function, which must be used in python3.x
from bottle import get, post, run, request, template, route, static_file
from config import IP_ADDRESS, PORT, end, control


@route('/static/css/<filename>')
def server_static(filename):
    # currentPath = os.path.dirname(os.path.realpath(__file__))
    return static_file(filename, root='./static/css')


@route('/static/fonts/<filename>')
def server_static(filename):
    # currentPath = os.path.dirname(os.path.realpath(__file__))
    return static_file(filename, root='./static/fonts')


@route('/static/js/<filename>')
def server_static(filename):
    # currentPath = os.path.dirname(os.path.realpath(__file__))
    return static_file(filename, root='./static/js')


@get("/")
def index():
    return template("index")


@post("/cmd")
def cmd():
    command_ = request.body.read().decode()
    control(command_)
    return "OK"


try:
    run(host=IP_ADDRESS, port=PORT)
finally:
    end()
