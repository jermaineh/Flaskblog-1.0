from flask import Flask
from flask_sqlalchemy import SQLAchemy 



app = Flask(__name__)
app.config['SECRET_KEY'] = 'F4a5341708bcc2f196aa6c691164421f'
app.config['SQLAchemy_DATABASE_URI'] = 'sqlite:///site.db'