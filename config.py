# IP ADDRESS, Please change this into your own ip address
IP_ADDRESS = '192.168.12.1'
PORT = 88 # My Pi has another web_server so in order to not have congress I choose port 88

# This function will be used after Page break down
def end():
    print('End')


# This is the function to accept the command and do the control
# cmd_=(
#    left,
#    right,
#    down,
#    up,
#    stop
#     )
import os
def control(cmd_):
    angle = 0
    if cmd_ == 'up':
	angle = 0
    if cmd_ == 'down':
	angle = 90
    if cmd_ == 'left':
	angle = 45
    if cmd_ == 'right':
	angle = 135
    if cmd_ == 'stop':
	angle = 180
    print(angle)
    os.system('cd /home/pi/medog;sudo ./test %d' % angle)
