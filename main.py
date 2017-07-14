from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True



def isEmpty(aString):
    if aString == '':
        return True
    else:
        return False

def noSpaces(aString):
    if ' ' in aString:
        return True
    else:
        return False

def isEqual(aString, anotherString):
    if aString == anotherString:
        return True
    else:
        return False

def isEmail(aString):
    if aString == '':
        return True
    if '.' in aString and '@' in aString:
        return True
    else:
        return False

def isGoodLength(aString):
    if aString != '':
        if len(aString) > 2 and len(aString) < 21:
            return False
        else:
            return True
    else:
        return True


@app.route('/', methods=['POST', 'GET'])
def validate():
    if request.method == 'GET':
        return render_template('signup_form.html')

    if request.method == 'POST':
        username = request.form[('username')]
        password = request.form[('password')]
        verifyPassword = request.form[('verifyPassword')]
        email = request.form[('email')]

        username_error = ''
        password_error = ''
        verifyPassword_error = ''
        email_error = ''


        if isGoodLength(username):
            username_error = 'Usernames must be between three and twenty characters, yo'

        if isGoodLength(password):
            password_error = 'Passwords must be between three and twenty characters, yo'

        if isGoodLength(email):
            email_error = 'Emails must be between three and twenty characters, yo'


        if isEmpty(username):
            username_error = 'Enter a username to continue'

        if isEmpty(password):
            password_error = 'Enter a password to continue'

        if isEmpty(verifyPassword):
            verifyPassword_error = 'You must verify your password to continue'


        if noSpaces(username):
            username_error = 'Usernames cannot contain spaces'

        if noSpaces(password):
            password_error = 'Passwords cannot contain spaces'


        if not isEqual(password, verifyPassword):
            verifyPassword_error = 'does not match'

        if not isEmail(email):
            email_error = 'email must contain . and @'


        if not username_error and not password_error and not verifyPassword_error and not email_error:
            return render_template('mainpage.html', username = username)

        else:
            return render_template('signup_form.html',
                                        username = username,
                                        email = email,
                                        username_error = username_error,
                                        password_error = password_error,
                                        verifyPassword_error = verifyPassword_error,
                                        email_error = email_error
                                        )









app.run()
