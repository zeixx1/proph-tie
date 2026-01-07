from flask import Flask, render_template, request
import random

def get_response():
    pool = [
        "Oui, sans aucun doute.",
        "Très probable.",
        "C'est certain.",
        "Les signes sont bons.",
        "Probable, mais garde un plan B.",
        "Peut-être, demande plus tard.",
        "Ce n'est pas clair, réessaie.",
        "Ne compte pas dessus.",
        "D'après moi non.",
        "Impossible de le prédire maintenant.",
        "Les chances sont faibles.",
        "Fais confiance à ton instinct.",
        "Les étoiles sourient à ta demande.",
        "Sois patient, la réponse viendra.",
        "Agis aujourd'hui, les signes suivront.",
        "Change d'approche et réessaye.",
        "C'est risqué, pèse le pour et le contre.",
        "Une opportunité inattendue apparaît.",
        "Rien n'est immuable, tout peut changer.",
        "La route est longue mais prometteuse."
    ]
    return random.choice(pool)


app = Flask("BouleMagique")

@app.route('/', methods=['GET', 'POST'])
def index():
    """Page principale — affiche le formulaire et gère la réponse.
    Si la question contient le mot 'fabrice' (insensible à la casse),
    on renvoie une réponse fixe unique.
    """
    response = None
    question = ''

    if request.method == 'POST':
        question = (request.form.get('question') or '').strip()
        if question:
            # règle spéciale pour 'fabrice'
            if 'fabrice' in question.lower():
                response = "le seul véritable dieu c'est fabrice"
            else:
                response = get_response()

    return render_template('index.html', response=response, question=question)


app.run('0.0.0.0', port=3907)
