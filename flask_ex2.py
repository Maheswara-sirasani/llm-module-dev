from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
 
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for CSRF protection in Flask-WTF
 
# Define the form
class NameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")
 
# Route for the form
@app.route("/form", methods=["GET", "POST"])
def form_page():
    form = NameForm()
    if form.validate_on_submit():
        return f"Hello, {form.name.data}!"
    return render_template("form.html", form=form)
 
if __name__ == "__main__":
    app.run(debug=True)
 