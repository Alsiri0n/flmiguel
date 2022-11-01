from app import app

@app.route('/')
@app.route('/index')
def index() -> str:
    user = {'username': 'Alsiri0n'}
    return '''
    <html>
        <head>
            <title>Home page - Microblof</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''
