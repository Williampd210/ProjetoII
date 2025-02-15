from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:810502@localhost/espacosilmarabd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()

# Modelo da tabela Agendamentos
class Agendamento(db.Model):
    __tablename__ = 'agendamentos'
    id_agendamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_servico = db.Column(db.Integer, db.ForeignKey('servicos.id_servico'), nullable=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=True)  # Chave estrangeira para usuarios
    formato = db.Column(db.String(15), nullable=True)
    estado = db.Column(db.String(20), nullable=True)
    data = db.Column(db.Date, nullable=False)  # Novo campo para a data
    hora = db.Column(db.Time, nullable=False)  # Novo campo para o horário
    observacoes = db.Column(db.String(150), nullable=True)

    def __repr__(self):
        return f"<Agendamento {self.id_agendamento} - Serviço {self.id_servico} - {self.data} {self.hora}>"
    
# Modelo da tabela Servicos
class Servico(db.Model):
    id_servico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)

# Modelo da tabela Usuarios
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.id_usuario} - {self.nome}>"
