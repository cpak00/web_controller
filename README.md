# web_controller
this project is for a web_controller to control raspberry pi
using bottle-python but has include it in the project so you
needn't to download it again.The jquery framework is also con
tain.This project must use python3 because it use decode(), p
lease make sure that your raspberry pi has installed python and
its path is /usr/bin/python3. This project can also be used in
Ubuntu, Federo, Windows, and everywhere support python3 enviro
nment.

# how to use it
* make sure you install python3
* correct the ip address in config.py to your own(you can check ip by use 'ifconfig' in Linux)
* change the content of function control(cmd_) and realize your function
  cmd_ can conclude up,down,left,right,stop according to what button you will press in the page
* use python3 to run web_server.py
* open the ip in another device, such as your phone, and try to press the button
* if you have any knowledge about HTML and JAVASCRIPT, you can change the index.tpl to a more complex page