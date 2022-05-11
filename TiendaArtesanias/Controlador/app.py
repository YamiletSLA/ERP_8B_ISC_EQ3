from datetime import timedelta
from urllib import request

from flask import Flask,render_template,request,flash,redirect,url_for,abort
from flask_bootstrap import Bootstrap
from Modelo.DAO import db, TipoPago, Usuario, Transportes, Productos, Estante, Almacen, ReporteAlmacen
from flask_login import current_user,login_user,logout_user, login_manager,login_required,LoginManager

app=Flask(__name__,template_folder='../vista',static_folder='../static')
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/sucumaster'
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

@app.route('/Principal')
def pagPrincipal():
    if current_user.is_authenticated:
        return render_template('comunes/Principal.html')
    else:
        return render_template('loggin.html')


@app.route('/Usuarios/iniciarSesion')
def mostrar_login():
    if current_user.is_authenticated:
        return render_template('comunes/Principal.html')
    else:
        return render_template('loggin.html')
####usuarios/loggin.html
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
    password_hash=request.form['password']
    usuario=Usuario()
    user=usuario.isValid(nombreUsuario,password_hash)
    if user!=None:
        login_user(user)
        return render_template('comunes/Principal.html')
    else:
        flash('Nombre de usuario o contraseña incorrectos')
        return render_template('loggin.html')

@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    logout_user()
    return redirect(url_for('mostrar_login'))

@app.route('/Usuario/Modificar',methods=['post'])
def ModificarUsuario():
    us=Usuario()
    us.idUsuario = request.form['idUsuario']
    us.nombreCompleto = request.form['nombreCompleto']
    us.nombreUsuario = request.form['nombreUsuario']
    us.password_hash = request.form['contraseña']
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

############Transportes

@app.route('/Transportes')
def consultaGeneralTransportes():
    t=Transportes()
    return render_template('Transportes/Consultar.html',transportes=t.consultaGeneral())

@app.route('/Transportes/Registrar')
def RegistrarTransporte():
    return render_template('Transportes/Registrar.html')

@app.route('/Transportes/nuevo',methods=['post'])
def nuevoTransporte():
    t = Transportes()
    t.nombre = request.form['nombre']
    t.telefono=request.form['telefono']
    t.estatus=request.form['estatus']
    t.insertar()
    flash('Transporte registrado con exito')
    return render_template('Transportes/Registrar.html')

@app.route('/Transportes/Ver/<int:id>')
def ConsultaIndTransportes(id):
    t = Transportes()
    return render_template('Transportes/Modificar.html',trans=t.consultaIndividual(id))

@app.route('/Transportes/Modificar',methods=['post'])
def ModificarTransportes():
    t= Transportes()
    t.idTipoPago = request.form['Id']
    t.nombre = request.form['nombre']
    t.telefono=request.form['telefono']
    t.estatus=request.form['estatus']

    t.actualizar()
    flash('La modificación del Transporte se realizó con exito')
    return render_template('Transportes/Modificar.html',trans=t)

@app.route('/Transportes/eliminar/<int:id>')
def eliminarTransporte(id):
    t=Transportes()
    t.eliminar(id)
    return render_template('Transportes/Consultar.html', trans=t)

##################

@app.route('/Productos')
def ConsultaGeneralProductos():
    pr=Productos()
    productos=pr.consultaGeneral()
    return render_template('Productos/Consultar.html',productos=productos)

@app.route('/Productos/Registrar')
def RegistrarNuevoProductos():
    return render_template('Productos/Registrar.html')

@app.route('/Productos/nuevo',methods=['post'])
def nuevoProductos():
    pr= Productos()
    pr.nombre = request.form['nombre']
    pr.descripcion = request.form['descripcion']
    pr.precio = request.form['precio']
    pr.idCategorias= request.form['idCategorias']

    pr.insertar()
    flash('Producto registrado con exito')
    return render_template('Productos/Registrar.html')

@app.route('/Productos/Ver/<int:id>')
def ConsultaIndProductos(id):
    pr = Productos()
    return render_template('Productos/Modificar.html',produc=pr.consultaIndividual(id))

@app.route('/Productos/Modificar',methods=['post'])
def ModificarProduct():
    pr=Productos()
    pr.idProducto = request.form['idProducto']
    pr.nombre = request.form['nombre']
    pr.descripcion = request.form['descripcion']
    pr.precio = request.form['precio']
    pr.idCategorias = request.form['idCategorias']
    pr.actualizar()
    flash('La modificación del producto se realizó con exito')
    return render_template('Productos/Modificar.html',produc=pr)


@app.route('/Productos/eliminar/<int:id>')
def eliminarProductos(id):
    pr=Productos()
    pr.eliminar(id)
    return render_template('Productos/Consultar.html',prod=pr)


################ESTANTE

@app.route('/Estante')
def ConsultaDeEstante():
    est=Estante()
    estante=est.consultaGeneral()
    return render_template('Estante/Consultar.html',estante=estante)

@app.route('/Estante/Registrar')
def RegistrarNuevoEstante():
    return render_template('Estante/Registrar.html')

@app.route('/Estante/nuevo',methods=['post'])
def RegistroNuevoEstante():
    est= Estante()
    est.nombre = request.form['nombre']
    est.ubicacion = request.form['ubicacion']

    est.insertar()
    flash('Estante registrado con exito')
    return render_template('Estante/Registrar.html')

@app.route('/Estante/Ver/<int:id>')
def ConsultaIndEstante(id):
    est = Estante()
    return render_template('Estante/Modificar.html',estant=est.consultaIndividual(id))

@app.route('/Estante/Modificar',methods=['post'])
def ModificacionDeEstante():
    est=Estante()
    est.idEstante = request.form['idEstante']
    est.nombre = request.form['nombre']
    est.ubicacion = request.form['ubicacion']
    est.actualizar()
    flash('La modificación del estante se realizó con exito')
    return render_template('Estante/Modificar.html',estant=est)

@app.route('/Estante/eliminar/<int:id>')
def eliminarEstantes(id):
    est=Estante()
    est.eliminar(id)
    return render_template('Estante/Consultar.html',esta=est)




########################ALMACEN#############################

@app.route('/Almacen')
def ConsultaDeAlmacen():
    alm=Almacen()
    almacen=alm.consultaGeneral()
    return render_template('Almacen/Consultar.html',almacen=almacen)

@app.route('/Almacen/nuevo')
@login_required
def nuevoAlmacen():
    if current_user.is_authenticated:
            return render_template('Almacen/Registrar.html')
    else:
        abort(404)

@app.route('/Almacen/Agregar',methods=['post'])
@login_required
def RegistroNuevoAlmacen():
    alm= Almacen()
    alm.cantProducto = request.form['cantProducto']
    alm.idProducto = request.form['idProducto']
    alm.idEstante = request.form['idEstante']
    alm.agregar()
    flash('Almacen registrado con exito')
    return render_template('Almacen/Registrar.html', alma=alm)

@app.route('/Almacen/Ver/<int:id>')
def ConsultaIndAlmacen(id):
    alm = Almacen()
    return render_template('Almacen/Modificar.html',alma=alm.consultaIndividual(id))

@app.route('/Almacen/Modificar',methods=['post'])
def ModificacionDeAlmacen():
    alm=Almacen()
    alm.idAlmacen = request.form['idAlmacen']
    alm.cantProducto = request.form['cantProducto']
    alm.idProducto = request.form['idProducto']
    alm.idEstante = request.form['idEstante']
    alm.actualizar()
    flash('La modificación del estante se realizó con exito')
    return render_template('Almacen/Modificar.html',alma=alm)

@app.route('/Almacen/eliminar/<int:id>')
def eliminarAlmacen(id):
    alm=Almacen()
    alm.eliminar(id)
    return render_template('Almacen/Consultar.html',almacen=alm.consultaGeneral())


########################REPORTES############################
@app.route('/Reporte')
def ConsultaRepAlm():
    rp= ReporteAlmacen()
    reporte=rp.consultaGeneral()
    return render_template('RepAlm/Reportes.html',reporte=reporte)


@app.route('/Reporte/nuevo')
@login_required
def nuevoReporte():
    if current_user.is_authenticated:
            return render_template('RepAlm/Registrar.html')
    else:
        abort(404)


@app.route('/Reporte/Agregar',methods=['post'])
@login_required
def agregarReporte():
      rp=ReporteAlmacen()
      rp.fecha=request.form['fecha']
      rp.descripcion=request.form['descripcion']
      rp.movimiento=request.form['movimiento']
      rp.cantidad=request.form['cantidad']
      rp.idAlmacen=request.form['idAlmacen']
      rp.idProducto=request.form['idProducto']
      rp.agregar()
      flash('¡ Rerporte agregado con exito !')
      return render_template('RepAlm/Registrar.html',repor=rp)

@app.route('/Reporte/Ver/<int:id>')
def ConsultaIndReporte(id):
    rp = ReporteAlmacen()
    return render_template('RepAlm/Modificar.html',repor=rp.consultaIndividual(id))

@app.route('/Reporte/Modificar',methods=['POST'])
@login_required
def editarReporte():
    rp = ReporteAlmacen()
    rp.idReporteAlmacen = request.form['idReporteAlmacen']
    rp.fecha = request.form['fecha']
    rp.descripcion = request.form['descripcion']
    rp.movimiento = request.form['movimiento']
    rp.cantidad = request.form['cantidad']
    rp.idAlmacen = request.form['idAlmacen']
    rp.idProducto = request.form['idProducto']
    rp.editar()
    flash('La modificación del estante se realizó con exito')
    return render_template('RepAlm/Modificar.html', repor=rp)

@app.route('/Reporte/eliminar/<int:id>')
@login_required
def eliminarReporte(id):
            rp=ReporteAlmacen()
            rp.eliminar(id)
            return render_template('RepAlm/Reportes.html', reporte=rp.consultaGeneral())

if __name__ == '__main__':
        db.init_app(app)
        app.run(port=3006, debug=True)