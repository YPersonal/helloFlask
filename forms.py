from wtforms import Form, StringField,PasswordField,validators,TextAreaField



class LoginForm(Form):
    username = StringField("username",[validators.Required()])
    description = TextAreaField("description")
