from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue au serveur de l'Artiste Globe-trotter ! Ici, découvrez comment la musique peut vous faire voyager à travers le monde."

# Route pour Artiste du Web
@app.route('/artiste_du_web')
def artiste_du_web():
    return jsonify({"artiste": "Artiste du Web", "description": "En tant qu'artiste du web, vous pouvez utiliser la technologie et la créativité pour toucher un public mondial et découvrir de nouvelles cultures."})

# Route pour Musique
@app.route('/musique')
def musique():
    return jsonify({"musique": "Musique", "description": "La musique est une langue universelle qui peut briser les barrières culturelles et vous transporter dans différents coins du monde."})

# Route pour Globe Trotter
@app.route('/globe_trotter')
def globe_trotter():
    return jsonify({"globe_trotter": "Globe Trotter", "description": "Voyager à travers le monde vous permet de découvrir de nouvelles cultures, de nouvelles perspectives et de nouvelles expériences."})

# Routes pour chaque destination musicale
@app.route('/destination/paris')
def destination_paris():
    return jsonify({"destination": "Paris", "musique": "Chanson française", "description": "Découvrez Paris à travers la chanson française, des classiques d'Édith Piaf aux nouvelles stars comme Zaz."})

@app.route('/destination/new_york')
def destination_new_york():
    return jsonify({"destination": "New York", "musique": "Jazz", "description": "Plongez dans l'ambiance vibrante de New York avec le jazz, de Duke Ellington à Miles Davis."})

@app.route('/destination/tokyo')
def destination_tokyo():
    return jsonify({"destination": "Tokyo", "musique": "J-Pop", "description": "Explorez Tokyo avec la J-Pop, un mélange de sons électroniques et de mélodies accrocheuses."})

@app.route('/destination/kingston')
def destination_kingston():
    return jsonify({"destination": "Kingston", "musique": "Reggae", "description": "Sentez les vibrations de Kingston avec le reggae, porté par les légendes comme Bob Marley et Burning Spear."})

@app.route('/destination/rio_de_janeiro')
def destination_rio():
    return jsonify({"destination": "Rio de Janeiro", "musique": "Samba", "description": "Dansez au rythme de la samba à Rio, avec ses battements entraînants et sa culture festive."})

@app.route('/destination/mumbai')
def destination_mumbai():
    return jsonify({"destination": "Mumbai", "musique": "Bollywood", "description": "Plongez dans l'univers coloré et énergique de Bollywood à Mumbai avec des chansons et des danses emblématiques."})

if __name__ == '__main__':
    app.run(debug=True)
