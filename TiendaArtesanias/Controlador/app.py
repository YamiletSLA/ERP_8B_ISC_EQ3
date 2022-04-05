from datetime import timedelta
from urllib import request

from flask import Flask,render_template,request,flash,redirect,url_for,abort
from flask_bootstrap import Bootstrap
from Modelo.DAO import db, TipoPago, Usuario
from flask_login import current_user,login_user,logout_user, login_manager,login_required,LoginManager

app=Flask(__name__,template_folder='../vista',static_folder='../static')
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:hola.123@localhost:3306/sucumaster'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'

log_manager=LoginManager()
log_manager.init_app(app)
log_manager.login_view='mostrar_login'
log_manager.login_message='¡ Tu sesión expiró !'
log_manager.login_message_category="info"


@app.route('/')
def inicio():
    return render_template('loggin.html')

@app.route('/Usuarios/iniciarSesion')
def mostrar_login():
    if current_user.is_authenticated:
        return render_template('comunes/Principal.html')
    else:
        return render_template('usuarios/loggin.html')

@log_manager.user_loader
def cargar_usuario(id):
    return Usuario.query.get(int(id))

@app.route('/Usuario')
def Usuarios():
    us=Usuario()
    usuario=us.consultaGeneral()
    return render_template('Usuario/Consultar.html',usuario=usuario)

@app.route('/Usuario/Registrar')
def RegistrarUsuario():
    return render_template('Usuario/Registrar.html')

@app.route('/Usuario/nuevo',methods=['post'])
def nuevoUsuario():
    us= Usuario()
    us.nombreCompleto = request.form['nombreCompleto']
    us.nombreUsuario = request.form['nombreUsuario']
    us.password_hash = request.form['contraseña']
    us.tipoUsuario= request.form['tipoUsuario']
    us.estatus = request.form['estatus']

    us.insertar()
    flash('Usuario registrado con exito')
    return render_template('Usuario/Registrar.html')

@app.route('/Usuario/Ver/<int:id>')
def ConsultaIndUsuario(id):
    us = Usuario()
    return render_template('Usuario/Modificar.html',user=us.consultaIndividual(id))

@app.route("/validarSesion",methods=['POST'])
def login():
    nombreUsuario=request.form['nomUsu']
    password=request.form['password']
    print ("user:"+nombreUsuario+" pwd:"+password)
    usuario=Usuario()
    user=usuario.isValid(nombreUsuario,password)
    if user!=None:
        login_user(user)
        return render_template('comunes/Principal.html')
    else:
        flash('Nombre de usuario o contraseña incorrectos')
        return render_template('loggin.html')


@app.route('/Usuario/Modificar',methods=['post'])
def ModificarUsuario():
    us=Usuario()
    us.idUsuario = request.form['idUsuario']
    us.nombreCompleto = request.form['nombreCompleto']
    us.nombreUsuario = request.form['nombreUsuario']
    us.contraseña = request.form['contraseña']
    us.tipoUsuario = request.form['tipoUsuario']
    us.estatus = request.form['estatus']
    us.actualizar()
    flash('La modificación del suario se realizó con exito')
    return render_template('Usuario/Modificar.html',user=us)

@app.route('/Usuario/eliminar/<int:id>')
def eliminarUsuario(id):
    us=Usuario()
    us.eliminar(id)
    return redirect(url_for("Usuarios"))

############################################### TipoPago

@app.route('/TipoPago')
def TiposPago():
    ti=TipoPago()
    tipopago=ti.consultaGeneral()
    return render_template('TipoPago/Consultar.html',tipopago=tipopago)

@app.route('/TipoPago/Registrar')
def RegistrarTipoPago():
    return render_template('TipoPago/Registrar.html')

@app.route('/TipoPago/nuevo',methods=['post'])
def nuevoTipoPago():
    ti = TipoPago()

    ti.tipo = request.form['tipo']
    ti.insertar()
    flash('Tipo de Pago registrado con exito')
    return render_template('TipoPago/Registrar.html')

@app.route('/TipoPago/Ver/<int:id>')
def ConsultaIndTipoPago(id):
    ti = TipoPago()
    return render_template('TipoPago/Modificar.html',tipopa=ti.consultaIndividual(id))

@app.route('/TipoPago/Modificar',methods=['post'])
def ModificarTipoPago():
    ti = TipoPago()
    ti.idTipoPago = request.form['Id']
    ti.tipo = request.form['tipo']
    ti.actualizar()
    flash('La modificación del Tipo de Pago se realizó con exito')
    return render_template('TipoPago/Modificar.html',tipopa=ti)

@app.route('/TipoPago/eliminar/<int:id>')
def eliminarTipoPago(id):
    ti=TipoPago()
    ti.eliminar(id)
    return redirect(url_for("TiposPago"))


if __name__=='__main__':
    db.init_app(app)
    app.run(port=3006, debug=True)

