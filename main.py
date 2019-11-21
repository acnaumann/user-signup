## *** Need: username, password, password verification and (optionally) email address ***
## *** Redirect to welcome page, or provide error information if any input is invalid ***


# the following should trigger error:
# any empty fields(not  email)
# username/password not valid (ex:space char or less than 3 characters or more than 20 characters)
# user password and password-confirmation do not match
# user provides email, but not a valid one - e.g. single @, single ., contains no spaces and is between 3 and 20 characters
# feedback message should be next to the field it refers to 
    # **** do not use email input type. Just use text (does not perform client-side validation). The will allow us to check
    # **** that the server side validation is working by letting errors through the client side. DO use type='password' for 
    # **** for password and password-verification to hide characters typed (this input type does not include any additional validation.)
# for username and email fields, preserve what user typed, so they don't have to retype
    # password fields should be cleared for security reasons
# If all input correct, direct to welcome page that states: "Welcome, [username]!"
# use templates (one for index, one for home page and one for welcome page) to render the HTML for your web app

from flask import Flask, request, redirect, render_template, escape


app = Flask(__name__)
app.config['DEBUG'] = True



# @app.route("/verify", methods=['POST'])
# def verify_entries():
    
   
#     
#     


        
@app.route("/verify", methods=['POST'])
def verify():
    username = request.form["user-name"]
    if len(username) < 3 or len(username) > 20 or username == '' or ' ' in username:
        name_error = "That's not a valid username"
    else:
        name_error = None
        
        

    password = request.form["password"]
    if len(password) < 3 or len (password) > 20 or password == '' or ' ' in password:
        pass_error = "That's not a valid password".format(password)
    else: 
        pass_error = None

        
    verify_password = request.form['verify-password']
    if verify_password == '' or password != verify_password:
        verify_pass_error = "Passwords don't match".format(verify_password)
    else:
        verify_pass_error = None
    
    email = request.form["email"]
    if email != '':
        if ' ' in email or (email.count('@') > 1) or len(email)<3 or len(email) > 20 or (email.count('.') > 1):
            email_error = "That's not a valid email".format(email)
        else:
            email_error = None
           

    username = escape(username)
    password = escape(password)
    verify_password = escape(verify_password)
    email = escape(email)

    if not email_error and not pass_error and not name_error and not verify_pass_error:
        return render_template("welcome.html", username=username)

    return render_template ("index.html", name_error=name_error, pass_error=pass_error, verify_pass_error=verify_pass_error, email_error=email_error)

     


# @app.route("/welcome")
# def welcome_greeting():
#     username = request.form['username']
    



@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template("index.html", error=encoded_error and escape(encoded_error))




app.run()

