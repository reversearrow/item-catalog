from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from models import Categories


class ItemForm(FlaskForm):
    name = StringField('Name', validators=[
                       DataRequired()])
    description = TextAreaField('Description', validators=[
                                DataRequired()])
    category = SelectField(
        u'Category')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.uuid, category.name)
                                 for category in Categories.query.order_by('name').all()]
