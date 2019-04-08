from wtforms import Form, TextField, TextAreaField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class contacto(Form):
	name = TextField('', [validators.Required(), validators.length(min=3, max=30)])
	email = EmailField('', [validators.Required()])
	text = TextAreaField('', [validators.required(), validators.length(max=200)])
	issue = SelectField ('En una escala del 1 al 5, ¿que tanto te gusta la pagina?', 
					choices=[('1', 'Soporte'), ('2', 'Duda'), ('3', 'Queja'), ('4', 'Sugerencia')])

class cont_cotizo(Form):
	name = TextField('', [validators.Required(), validators.length(min=3, max=30)])
	email = EmailField('', [validators.Required()])
