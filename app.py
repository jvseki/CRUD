from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'minha_chave_secreta'

db = SQLAlchemy(app)


matriculas = db.Table('matriculas',
    db.Column('aluno_id', db.Integer, db.ForeignKey('aluno.id'), primary_key=True),
    db.Column('curso_id', db.Integer, db.ForeignKey('curso.id'), primary_key=True)
)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cursos = db.relationship('Curso', secondary=matriculas, backref=db.backref('alunos', lazy='dynamic'))

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alunos')
def alunos():
    lista_alunos = Aluno.query.all()
    return render_template('alunos.html', alunos=lista_alunos)

@app.route('/aluno/adicionar', methods=['GET', 'POST'])
def adicionar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        novo_aluno = Aluno(nome=nome)
        db.session.add(novo_aluno)
        db.session.commit()
        return redirect(url_for('alunos'))
    return render_template('adicionar_aluno.html')

@app.route('/aluno/editar/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    if request.method == 'POST':
        aluno.nome = request.form['nome']
        db.session.commit()
        return redirect(url_for('alunos'))
    return render_template('editar_aluno.html', aluno=aluno)

@app.route('/aluno/deletar/<int:id>')
def deletar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('alunos'))


@app.route('/cursos')
def cursos():
    lista_cursos = Curso.query.all()
    return render_template('cursos.html', cursos=lista_cursos)

@app.route('/curso/adicionar', methods=['GET', 'POST'])
def adicionar_curso():
    if request.method == 'POST':
        nome = request.form['nome']
        novo_curso = Curso(nome=nome)
        db.session.add(novo_curso)
        db.session.commit()
        return redirect(url_for('cursos'))
    return render_template('adicionar_curso.html')

@app.route('/curso/editar/<int:id>', methods=['GET', 'POST'])
def editar_curso(id):
    curso = Curso.query.get_or_404(id)
    if request.method == 'POST':
        curso.nome = request.form['nome']
        db.session.commit()
        return redirect(url_for('cursos'))
    return render_template('editar_curso.html', curso=curso)

@app.route('/curso/deletar/<int:id>')
def deletar_curso(id):
    curso = Curso.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for('cursos'))


@app.route('/matricular', methods=['GET', 'POST'])
def matricular():
    alunos = Aluno.query.all()
    cursos = Curso.query.all()
    if request.method == 'POST':
        aluno_id = request.form['aluno']
        curso_id = request.form['curso']
        aluno = Aluno.query.get(aluno_id)
        curso = Curso.query.get(curso_id)
        if curso not in aluno.cursos:
            aluno.cursos.append(curso)
            db.session.commit()
        return redirect(url_for('alunos'))
    return render_template('matricular.html', alunos=alunos, cursos=cursos)


if __name__ == '__main__':
    app.run(debug=True)
