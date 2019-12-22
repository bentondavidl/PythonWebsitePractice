from flask import Flask, render_template
from noteapp.views.notes import bp as notes_bp
from noteapp.views.index import bp as index_bp

app = Flask(__name__)

app.register_blueprint(notes_bp)
app.register_blueprint(index_bp)

