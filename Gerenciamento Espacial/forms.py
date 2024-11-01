from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class MissionForm(FlaskForm):
    name = StringField('Nome da Missão', validators=[DataRequired()])
    launch_date = DateField('Data de Lançamento', format='%Y-%m-%d', validators=[DataRequired()])
    destination = StringField('Destino', validators=[DataRequired()])
    state = StringField('Estado', validators=[DataRequired()])
    crew = StringField('Tripulação')
    payload = StringField('Carga Útil')
    duration = StringField('Duração da Missão')
    cost = DecimalField('Custo da Missão', places=2, validators=[DataRequired()])
    status = TextAreaField('Status da Missão')
    submit = SubmitField('Salvar')
