## *** Need: username, password, password verification and (optionally) email address ***
## *** Redirect to welcome page, or provide error information if any input is invalid ***


# the following should trigger error:
# any empty fields(not sure about email; not listed)
# username/password not valid (ex:space char or less than 3 characters or more than 20 characters)
# users password and password-confirmation do not match
# user provides email, but not a valid one - e.g. single @, single ., contains no spaces and is between 3 and 20 characters
# feedback message should be next to the field it refers to 
    # **** do not use email input type. Just use text (does not perform client-side validation). The will allow us to check
    # **** that the server side validation is working by letting errors through the client side. DO use type='password' for 
    # **** for password and password-verification to hide characters typed (this input type does not include any additional validation.)
# for username and email fields, preserve what user typed, so they don't have to retype
    # password fields should be cleared for security reasons
# If all input correct, direct to welcome page that states: "Welcome, [username]!"
# use templates (one for index, one for home page and one for welcome page) to render the HTML for your web app

from flask import Flask, request, redirect, render_template
import html
import os

app = Flask(__name__)
app = app.config['DEBUG'] = True







@app.route("/signup")
def home():

@app.route("/welcome")
def welcome_greeting():


@app.route("/")
def index():




app.run()

