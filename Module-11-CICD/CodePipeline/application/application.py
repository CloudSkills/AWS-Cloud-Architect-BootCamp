from flask import Flask, render_template, request, jsonify


application = Flask(__name__)


@application.route("/")
def home():
    return 'Hello, Cloudskills Friends!'


application.run()