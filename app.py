from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import pdfkit
from datetime import datetime, timedelta
import forms

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = '_secret_key_'
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
	sitio = 'index'
	return render_template('index.html', sitio=sitio)				

@app.route('/about')
def about():
	sitio = 'nosotros'
	return render_template('about.html', sitio=sitio)

@app.route('/holo')
def holo():
	sitio = 'holograma'
	cont1=forms.cont_cotizo(request.form)


	return render_template('holo.html', sitio=sitio, form = cont1)	

@app.route('/cotizacion', methods =['GET', 'POST'])
def cotizacion():
	precio = int(request.form['tamanio_holograma'])+int(request.form['ambiente_holograma'])+int(request.form['estilo_holograma'])+int(request.form['tipo_holograma'])
	if request.form['tamanio_holograma'] == '5000':
		tiempo = 15
	elif request.form['tamanio_holograma'] == '7000':
		tiempo = 25
	else:
		tiempo = 30
	fecha_estimada = (datetime.now() + timedelta(days=tiempo)).strftime('%d/%m/%y')

	cont1=forms.cont_cotizo(request.form)
	print(cont1.name.data)
	print(cont1.email.data)

	#Configuro el correo que se va a enviar
	sender_email = "ingenium.developers@gmail.com"
	receiver_email = cont1.email.data
	password = "Cugs2019"

	message = MIMEMultipart("alternative")
	message["Subject"] = "Presupuesto"
	message["From"] = sender_email
	message["To"] = receiver_email
	message["BBC"] = "alanucamargo@gmail.com"

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
	        <div class="col-2">""" + str(datetime.now().strftime("%d/%m/%Y")) + """</div>
	  </div>
	</div>
	<br>
	<div class="container">
	  <div class="row">
	        <div class="col-4">DATOS DEL CLIENTE: """ + cont1.name.data + ", " + cont1.email.data + """</div>
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
	  </tr>
	  <tr>
	    <th>""" + ("Chico" if request.form['tamanio_holograma'] == "5000" else ("Mediano" if request.form['tamanio_holograma'] == "7000" else "Grande")) + """</th>
	    <th>1</th>
	    <th>""" + request.form['tamanio_holograma'] + """</th>
	  </tr>
	  <tr>
	    <th>""" + ("Iluminado" if request.form['ambiente_holograma'] == "1500" else ("Oscuro" ))+ """</th>
	    <th>1</th>
	    <th>""" + request.form['ambiente_holograma'] + """</th>
	  </tr>
	  <tr>
	    <th>""" + ("Madera" if request.form['estilo_holograma'] == "2100" else ("Aluminio" ))+ """</th>
	    <th>1</th>
	    <th>""" + request.form['estilo_holograma'] + """</th>
	  </tr>
	  <tr>
	    <th> """ + ("Estatico" if request.form['tipo_holograma'] == "7000" else ("Dinamico" if request.form['tipo_holograma'] == "8000" else "Informativo")) + """</th>
	    <th>1</th>
	    <th> """ + request.form['tipo_holograma']  + """ </th>
	  </tr>
	  <tr>
	    <th>TOTAL</th>
	    <th class="colspan justify-content-end" colspan="3"> """ + str(precio) + """</th>
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



	return render_template('hago_cotizacion.html', precio = precio, fecha_estimada = fecha_estimada)


@app.route('/cotizo', methods = ['GET','POST'])
def descargo_pdf():
	if request.method=='POST':
		tamaño = int(request.form['tamanio_holograma'])
		material = int(request.form['ambiente_holograma'])
		ambiente = int(request.form['estilo_holograma'])
		tipo = int(request.form['tipo_holograma'])
		rendered = render_template('test.html', material = material, tipo = tipo, tamaño = tamaño, ambiente = ambiente)
		pdf = pdfkit.from_string(rendered, False)

		response = make_response(pdf)
		response.headers['Content-Type'] = 'application/pdf'
		response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

		return response


@app.route('/contacto', methods =['GET', 'POST'])
def contacto():
	sitio = 'contacto'
	cont=forms.contacto(request.form)

	if request.method=='POST' and cont.validate(): 
		print(cont.name.data)
		print(cont.email.data)
		print(cont.text.data)
		return render_template('nose.html', form=cont, sitio=sitio)
	return render_template('contacto.html', form=cont, sitio=sitio)

@app.route('/faq')
def faq():
	sitio = 'faq'
	return render_template('faq.html', sitio=sitio)

if __name__=='__main__':
	app.run(port=8080, debug=True)


	