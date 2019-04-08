import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

#Configuro el correo que se va a enviar
sender_email = "ingenium.developers@gmail.com"
receiver_email = "alanucamargo@gmail.com"
password = "Cugs2019"

message = MIMEMultipart("alternative")
message["Subject"] = "Presupuesto"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
html = """\
<!DOCTYPE html>
<head>
  <title>Test</title>
    <meta charset="utf-8">
    <meta name="viewport"     content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie-edge">
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
<head>
  <style type="text/css">
  h1, h2, ul{text-align: center;}

   div[class^="col"] {
      border: 1px solid green;}
      
   div[class^="row"] {
      border: 1px solid green;}
      .borde{}

   table{
   width: 100%;
   border: 1px solid #000;}
  th, td {
   width: 25%;
   text-align: center;
   vertical-align: top;
   border: 1px solid #000}
   .borde{}
  </style>
</head>

<body>
<h1><center>PRESUPUESTO</center></h1>
<br>
<div class="container">
  <div class="row">
        <div class="col-2"><p>DATOS DE LA EMPRESA</p><p>LOGO OPCIONAL</p></div>
  </div>
</div>
<br>
<div class="container">
  <div class="row justify-content-end">
        <div class="col-2">NO. COTIZACION</div>     
        <div class="col-2">FECHA</div>
  </div>
</div>
<div class="container">
  <div class="row justify-content-end">
        <div class="col-2">#########</div>
        <div class="col-2">MM/DD/AA</div>
  </div>
</div>
<br>
<div class="container">
  <div class="row">
        <div class="col-4">DATOS DEL CLIENTE</div>
  </div>
</div>
<br>
<div class="container">
  <div class="row">
        <div class="col-12"><p>DESCRIPCION DEL TRABAJO</p></div>
  </div>
</div>
<div class="container">
  <div class="row">
        <div class="col-12"><p>aqui va el texto sobre el trabjo, muy especifico</p></div>
  </div>
</div>
<br>
<table class="egt">
  <tr>
    <th>DESCRIPCION</th>
    <th>CANTIDAD</th>
    <th>PRECIO UNIT</th>
    <th>TOTAL</th>
  </tr>
  <tr>
    <th>DESCRIPCION</th>
    <th>CANTIDAD</th>
    <th>{{ tamaño }}</th>
    <th>TOTAL</th>
  </tr>
  <tr>
    <th>DESCRIPCION</th>
    <th>CANTIDAD</th>
    <th>{{ material }}</th>
    <th>TOTAL</th>
  </tr>
  <tr>
    <th>DESCRIPCION</th>
    <th>CANTIDAD</th>
    <th>{{ estilo }}</th>
    <th>TOTAL</th>
  </tr>
  <tr>
    <th>DESCRIPCION</th>
    <th>CANTIDAD</th>
    <th>{{ tipo }}</th>
    <th>TOTAL</th>
  </tr>
  <tr>
    <th>DESCRIPCION</th>
    <th>CANTIDAD</th>
    <th>PRECIO UNIT</th>
    <th>TOTAL</th>
  </tr>
  <tr>
    <th>TOTAL</th>
    <th class="colspan justify-content-end">PRECIO TOTAL $$ </th>
  </tr>
</table>
</body>
</html>           

"""

  
# Turn these into plain/html MIMEText objects

part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first

message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
	server.login(sender_email, password)
	server.sendmail(
    	sender_email, receiver_email, message.as_string()
    )
print("Enviamos correo a {}".format(receiver_email))
