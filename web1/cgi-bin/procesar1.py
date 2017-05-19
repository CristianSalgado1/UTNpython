#!/usr/bin/env python3
import cgi
form = cgi.FieldStorage()

print('Content-type: text/html\n')

print("""
<html> 
     <head> 
          <meta charset="utf-8"/> 
          <title>Página de retorno</title> 
     </head> 
     <body> 
          <h1>Hola %s!</h1> 
     </body> 
</html>"""  % cgi.escape(form['nombre'].value)) 
