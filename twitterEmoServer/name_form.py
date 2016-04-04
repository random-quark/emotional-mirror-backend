from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, IntegerField, FloatField, BooleanField
from wtforms.validators import Optional, NumberRange

class NameForm(Form):
    #name = StringField('What is your name?') #, validators=[Required()]
    neg_rel = SelectField(
        "neg_rel",
        choices=[('', "select"), ('$gt', '>'), ('$lt', '<'), ('$gte', '>='), ('$lte', '<='), ('==', '==')]
        , default=0, validators=[Optional()]
        )
    pos_rel = SelectField(
        'pos_rel',
        choices=[('', "select"), ('$gt', '>'), ('$lt', '<'), ('$gte', '>='), ('$lte', '<='), ('==', '==')]
        , default=0, validators=[Optional()]
        )
    neu_rel = SelectField(
        'neu_rel',
        choices=[('', "select"), ('$gt', '>'), ('$lt', '<'), ('$gte', '>='), ('$lte', '<='), ('==', '==')]
        , default=0, validators=[Optional()]
        )
    comp_rel = SelectField(
        'comp_rel',
        choices=[('', "select"), ('$gt', '>'), ('$lt', '<'), ('$gte', '>='), ('$lte', '<='), ('==', '==')]
        , default=0, validators=[Optional()]
        )

    pos_value = FloatField('positive_value', validators=[Optional(), NumberRange(0,1)])
    neg_value = FloatField('negative_value', validators=[Optional(), NumberRange(0,1)])
    neu_value = FloatField('neutral_value', validators=[Optional(), NumberRange(0,1)])
    comp_value = FloatField('composite_value', validators=[Optional(), NumberRange(-1,1)])
    max_results = IntegerField("maximum_results", default=1)
    exclude_past = BooleanField("exclude_past", default=False)
    randomize_results = BooleanField("randomize_results", default=True)

    submit = SubmitField('Submit')
