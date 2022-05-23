from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


views = Blueprint('views', __name__)

@views.route('/', methods= ["GET", "POST"])
#cannot get to home page unless logged in
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")
        if len(note) < 1:
            flash("Note is too short", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added", category="success")
    return render_template("home.html", user=current_user)

@views.route("/delete-note", methods=["POST"])
#going to look for the noteId sent to us. We are sending the request not as a form, so the request
    #is going to come in the data parameter of the request object, which means we need to load it as JSON
def delete_note():
    #going to take in data from a POST request load it as a json object
    note = json.loads(request.data)
    #going to access noteId attribute (which is from index.js)
    noteId = note["noteId"]
    #this will look for the note that has that id
    note = Note.query.get(noteId)
    #check if that id exists
    if note:
        #if we own this note (the user who is signed in owns this note)
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    #This would be"jsonifying" an empty python dictionary which essentially means turn this into a json object that
    # we can return
        #we aren't returning anything here but it is a requirement from flask
    return jsonify({})