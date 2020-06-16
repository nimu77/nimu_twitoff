# web_app/routes/bike_trail.py

from flask import Blueprint, jsonify, request, render_template
from web_app.model import Trail, db, parse_records
bike_trail = Blueprint("bike_trail", __name__)

@bike_trail.route("/trails.json")
def list_trails():
    # trails = [
    #     {"id":1, "title": "Trail1"},
    #     {"id":2, "title": "Trail2"}
    # ]
    breakpoint()
    trail_records = Trail.query.all()
    print(trail_records)
    trails = parse_records(trail_records)
    return jsonify(trails)

@bike_trail.route("/trails")
def list_trails_for_humans():
    # trails = [
    #     {"id":1, "title": "Trail1"},
    #     {"id":2, "title": "Trail2"}
    # ]
    trail_records = Trail.query.all()
    print(trail_records)
    trails = parse_records(trail_records)

    return render_template("trails.html", message="Here's some bike trails in Washington", trails=trails)

@bike_trail.route("/trails/new")
def new_book():
    return render_template("new_trail.html")

@bike_trail.route("/trails/create", methods=["POST"])
def create_trail():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    new_trail = Trail(title=request.form["title"], city=request.form["city"])
    db.session.add(new_trail)
    db.session.commit()
    return jsonify({
        "message": "Trail Created Great!!!",
        "trail": dict(request.form)
    })