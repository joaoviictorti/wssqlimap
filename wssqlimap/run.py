from http.server import HTTPServer, BaseHTTPRequestHandler
from websocket import create_connection
from urllib.parse import unquote, urlparse

class Send_Websocket():	

    def __init__(self,websocket:str):
        self.__webscocket = websocket

    def enviar_ws(self,payload):
        servidor_ws =  self.__websocket
        connection_ws = create_connection(servidor_ws)

        message = unquote(payload).replace('"','\'')
        data = "{\"id\":\""+message+"\"}" # payload para enviar ao websocket com a injeção sql

        connection_ws.send(data)
        resp = connection_ws.recv()
        connection_ws.close()

        if resp:
           return resp
        else:
           return ''

class HTTP(BaseHTTPRequestHandler):
	
    def __init__(self,websocket):
        self.__websocket = websocket

    def do_GET(self):
        self.send_response(200)
        try:
            payload = urlparse(self.path).query.split('=',1)[1] # /?id=123
			
        except IndexError:
           payload = False
				
        if payload:
            content = Send_Websocket(self.__websocket).enviar_ws(payload) # 123' UNION SELECT......
        else:
            content = 'Nenhum parâmetro especificado'

        self.send_header("Content-type","text/plain")
        self.end_headers()
        self.wfile.write(bytes())
        return
