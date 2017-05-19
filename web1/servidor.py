#!/usr/bin/env python3
import os
from http.server import HTTPServer,  CGIHTTPRequestHandler

webdir = '.'
port = 8080

os.chdir(webdir)
srvraddr = ("",  port)
srvrobj = HTTPServer(srvraddr,  CGIHTTPRequestHandler)
print("Iniciando el servidor de web en el puerto: "+str(port))

srvrobj.serve_forever()
