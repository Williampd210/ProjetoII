from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:810502@localhost/espacosilmarabd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()

# Modelo da tabela Agendamentos
class Agendamento(db.Model):
    id_agendamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_servico = db.Column(db.Integer, db.ForeignKey('servicos.id_servico'), nullable=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=True)
    formato = db.Column(db.String(15), nullable=True)
    estado = db.Column(db.String(20), nullable=True)
    data_hora = db.Column(db.DateTime, nullable=True)
    observacoes = db.Column(db.String(150), nullable=True)

# Modelo da tabela Servicos
class Servico(db.Model):
    id_servico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)

# Modelo da tabela Usuarios
class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
