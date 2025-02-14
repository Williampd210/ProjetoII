from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
import pymysql

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'espacosilmarabd',
    'charset': 'utf8mb4'
}

# Criar a instância do Flask
app = Flask(__name__, static_folder='static')
app.secret_key = 'sua_chave_secreta'  # Necessário para usar flash messages e sessões

# Função para conectar ao banco de dados
def get_db_connection():
    connection = pymysql.connect(**db_config)
    return connection

# Página inicial que renderiza o formulário de cadastro
@app.route('/')
def index():
    return render_template('index.html')  # Página principal (após o login)

# Rota para receber os dados do formulário de cadastro e inserir no banco de dados
@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    try:
        # Conectar ao banco de dados
        connection = get_db_connection()
        cursor = connection.cursor()

        # Verificar se o email já existe
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Se o email já existe, mostrar uma mensagem de erro
            flash("Este e-mail já está cadastrado. Tente com outro.", 'error')
            return redirect(url_for('index'))

        # Inserir os dados na tabela 'usuarios'
        sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, email, senha))
        connection.commit()

        cursor.close()
        connection.close()

        # Redirecionar para a página de login após o cadastro
        flash("Cadastro realizado com sucesso! Agora, faça login.", 'success')
        return redirect(url_for('login'))  # Redireciona para a página de login

    except pymysql.MySQLError as e:
        print(f"Erro ao inserir dados: {e}")
        flash("Erro ao cadastrar, tente novamente.", 'error')
        return redirect(url_for('index'))

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Conectar ao banco de dados
        connection = get_db_connection()
        cursor = connection.cursor()

        # Verificar se o e-mail e a senha correspondem a um usuário
        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            # Se os dados estiverem corretos, armazenar o usuário na sessão
            session['user_id'] = user[0]  # Armazenar o id do usuário na sessão (id_usuario)
            session['user_name'] = user[1]  # Armazenar o nome na sessão (nome)
            flash(f"Bem-vindo, {user[1]}!", 'success')  # Mensagem de boas-vindas
            return redirect(url_for('index'))  # Redireciona para a página index (principal)
        else:
            # Se os dados estiverem incorretos, mostrar uma mensagem de erro
            flash("E-mail ou senha incorretos. Tente novamente.", 'error')
            return redirect(url_for('login'))  # Redireciona para a página de login

    return render_template('login.html')  # Exibe o formulário de login

# Página principal (index.html)
@app.route('/index')
def home():
    # Certificar-se de que o usuário está logado antes de acessar a página principal
    if 'user_id' not in session:
        flash("Você precisa fazer login para acessar a página.", 'warning')
        return redirect(url_for('login'))
    return render_template('index.html')  # Exibe a página principal

# Outras páginas (exemplo)
@app.route('/servicos', endpoint='servicos')  # Adicionando o endpoint correto
def servicos():
    return render_template('servicos.html')  # Página de serviços

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')  # Certifique-se de que o arquivo existe em "templates/"

@app.route('/contato')
def contato():
    return render_template('contato.html')  # Página de contato

if __name__ == '__main__':
    app.run(debug=True)
