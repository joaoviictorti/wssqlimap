import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
from argparse import RawTextHelpFormatter
from .run import HTTP

def argumentos():
    parser = argparse.ArgumentParser(usage="wssqlimap --ws \"ws://teste:9000/\" --lhost 127.0.0.1 --lport 6060 ",formatter_class=RawTextHelpFormatter)
    parser.add_argument("--version",action="version",version="wssqlimap 0.0.1")
    parser.add_argument("--ws","-W",dest="Websocket",action="store",type=str,required=False,help="Insert the websocket for the test")
    parser.add_argument("--lhost",dest="host",action="store",type=str,required=True,default="127.0.0.1",help="Enter your ip. Default=127.0.0.1")
    parser.add_argument("--lport",dest="port",action="store",type=int,required=True,default="80",help="Enter your port. Default=80")
    args = parser.parse_args()
    server = HTTPServer((args.host,args.port),HTTP)
    print("Use esse comando em outro terminal para realização da injeção com sqlmap: sqlmap -u \"http://ip:port/?id=123\" -p id .....")
    server.serve_forever()