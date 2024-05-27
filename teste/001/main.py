from flask import Flask, render_template, redirect, request, flash
import json
import ast
import os
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'glf'

logado = False

@app.route('/')
def home():
    global logado
    logado = False
    return render_template('login.html')

@app.route('/adm')
def adm():
    if logado == True:
       conect_bd = mysql.connector.connect(host='localhost', user='root', database='usuarios', password='python78')

    if conect_bd.is_connected():
            print('conectado')
            cursor = conect_bd.cursor()
            cursor.execute('select * from cadastrados;')
            usuarios = cursor.fetchall()
    return render_template("administrador.html",usuarios=usuarios)
    if logado == False:
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():

    global logado

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    conect_bd = mysql.connector.connect(host='localhost', user='root', database='usuarios', password='python78')
    cont = 0
    if conect_bd.is_connected():
        print('conectado')
        cursor = conect_bd.cursor()
        cursor.execute('select * from cadastrados;')
        usuariosbd = cursor.fetchall()
        
        for usuario in usuariosbd:
            cont += 1
            usuarioNome = str(usuario[1])
            usuarioSenha = str(usuario[2])

            if nome == 'adm' and senha == '000':
                logado = True
                return redirect('/adm')

            if usuarioNome == nome and usuarioSenha == senha:
                return render_template("usuario.html")
            
            if cont >= len(usuariosbd):
                flash('USUARIO INVALIDO')
                return redirect("/")
    else:
        return redirect('/')        

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    global logado
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    conect_bd = mysql.connector.connect(host='localhost', user='root', database='usuarios', password='python78')
    if conect_bd.is_connected():
        cursur = conect_bd.cursor()
        cursur.execute(f"insert into usuario values (default, '{nome}', '{senha}');")
    if conect_bd.is_connected():
        cursur.close()
        conect_bd.close()

   
    logado = True
    flash(f"{nome} CADASTRADO!")
    return redirect('/adm')


@app.route('/excluirUsuario', methods=['POST'])
def excluirUsuario():
    global logado
    logado = True
    nome = request.form.get('')
    usuarioID = request.form.get('UsuarioPexcluir')
    conect_bd = mysql.connector.connect(host='localhost', user='root', database='usuarios', password='python78')
    if conect_bd.is_connected():
        cursur = conect_bd.cursor()
        cursur.execute(f"delete from usuario where id='{usuarioID}';")

    if conect_bd.is_connected():
        cursur.close()
        conect_bd.close()

    flash(f'{nome} EXCLUIDO')
    return redirect('/adm')


@app.route("/upload", methods=['POST'])
def upload():
    global logado
    logado = True

    arquivo = request.files.get('documento')
    nome_arquivo = arquivo.filename.replace(" ","-")
    arquivo.save(os.path.join('../arquivos', nome_arquivo))
    
    flash('Arquivo salvo')
    return redirect('/adm')

if __name__ in "__main__":
    app.run(debug=True)    


