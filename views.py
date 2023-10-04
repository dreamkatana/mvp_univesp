from flask import render_template, request
from app import app



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pokemon_name = request.form.get('search').lower()
        # Popula o banco de dados com o pokemon pesquisado
        ip_address = request.remote_addr  # Get client IP address

        # Create the request body
        body = {
            "ip_address": ip_address,
            "pokemon_name": pokemon_name
        }

        return render_template('home.html', pokemons=body)
    return render_template('home.html', pokemons=0)

@app.route("/home")
def inicio():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/estatisticas/")
def estatistica():
    #response = requests.get("http://searches_service:5001/searches")
    #searches = response.json()
    return render_template('estatistica.html', searches=0)
