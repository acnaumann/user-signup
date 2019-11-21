## *** Need: username, password, password verification and (optionally) email address ***
## *** Redirect to welcome page, or provide error information if any input is invalid ***


# the following should trigger error:
# any empty fields(not  email)
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

from flask import Flask, request, redirect, render_template, escape


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/verify", methods=['POST'])
def verify_entries():
    username = request.form["user-name"]
    password = request.form["password"]
    verify_password = request.form['verify-password']
    email = request.form["email"]

    
    # if username == '':
    #     error = 'Please enter a valid response'.format(username)
    #     return redirect ("/?error=" + error)
        


    if len(username) < 3 or len (username) > 20 or username == '' or ' ' in username:
        error = "That's not a valid username".format(username)
        return redirect ("/?error=" + error)


    # if len(password) < 3 or len (password) > 20 or password == '' or ' ' in password:
    #     error = "That's not a valid password".format(password)
    #     return redirect ("/?error=" + error)

    # if password != verify_password:
    #     error = "Passwords don't match".format(verify_password)
    #     return redirect ("/?error" + error)


    


    username = escape(username)
# if (len(username) or len(password) or len()) < 20:
#     error = "password must be less than 20 characters"
#     return redirect ("/?error=" + error)

    return render_template('welcome.html', username=username)
# if password != verify-password:
#     error = "Passwords did not match"







@app.route("/welcome")
def welcome_greeting():
    username = request.form['username']
    return render_template("welcome.html", username=username)



@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template("index.html", error=encoded_error and escape(encoded_error))




app.run()

