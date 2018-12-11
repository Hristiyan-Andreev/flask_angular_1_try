from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FormField, HiddenField
from wtforms.validators import DataRequired

# Form for setting Elemental Live IP address
class IPForm(FlaskForm):
	ipaddress = StringField('Elemental IP Adress', validators=[DataRequired()] )
	submit = SubmitField('Set')

# Buttons for manual Testing of GPI signal, activating or logging GPI inputs
class GPIctrl(FlaskForm):
	stream_id = IntegerField('Stream ID:', validators=[DataRequired()] )
	btn_set = SubmitField('Set', validators=[DataRequired()])
	btn_ss_cue= SubmitField('Test')