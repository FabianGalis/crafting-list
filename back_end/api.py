import flask, json
from flask import request, jsonify, redirect, url_for

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Dict list extracted from minecraft source
with open("database_recipes.json", "r") as read_recipes:
    recipes = json.load(read_recipes)

@app.route('/', methods=['GET'])
def home():
    #main page
    with open("front_end\main_page.html", "r") as read_page:
        return read_page.read()

@app.route('/recipes/all', methods=['GET'])
def api_all():
    return jsonify(recipes)

@app.route('/recipes/specify', methods=['GET'])
def api_find():
    id = ''
    group = ''
    # check if id/group provided from url
    if 'id' in request.args:
        id = str(request.args['id'])
    if 'group' in request.args:
        group = str(request.args['group'])
    if 'id' not in request.args and 'group' not in request.args:
        return "Error: No id or group field provided. Please specify at least one."

    # to store results
    found = []

    # Loop through the data and match results that fit the requested ID.
    for recipe in recipes:
        if recipe['crafted_item'] == id or ('group' in recipe and recipe['group'] == group):
            found.append(recipe)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(found)

app.run()