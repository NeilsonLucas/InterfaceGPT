#!/usr/bin/env python
import cgi

print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<title>Dados do formulário</title>")
print("</head>")
print("<body>")
print("<h1>Dados do formulário</h1>")

form = cgi.FieldStorage()
nome = form.getvalue("nome")
email = form.getvalue("email")

print("<p>Nome: {}</p>".format(nome))
print("<p>E-mail: {}</p>".format(email))

print("</body>")
print("</html>")
