# web_app/routes/bike_trail.py

from flask import Blueprint, jsonify, request, render_template

bike_trail = Blueprint("bike_trail", __name__)

@bike_trail.route("/trails.json")
def list_trails():
    trails = [
        {"id":1, "title": "Trail1"},
        {"id":2, "title": "Trail2"}
    ]

@bike_trail.route("/trails")
def list_trails_for_humans():
    trails = [
        {"id":1, "title": "Trail1"},
        {"id":2, "title": "Trail2"}
    ]

    return render_template("trails.html", message="Here's some bike trails in Washington", trails=trails)

@bike_trail.route("/trails/new")
def new_book():
    return render_template("new_trail.html")

@bike_trail.route("/trails/create", methods=["POST"])
def create_trail():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    return jsonify({
        "message": "Trail Created Great!!! (TODO)",
        "trail": dict(request.form)
    })