from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,ForeignKey,Integer,String,Float,Boolean,Date
from flask_login import UserMixin
from sqlalchemy.orm import relationship

db=SQLAlchemy()

class TipoPago(db.Model):
    __tablename__ = 'TipoPago'
    idTipoPago=Column(Integer, primary_key=True)
    tipo=Column(String(10))

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self,id):
        return self.query.get(id)

    def eliminar(self,id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    idUsuario = Column(Integer, primary_key=True)
    nombreCompleto = Column(String, nullable=False)
    nombreUsuario = Column(String, nullable=False)
    contraseña = Column(String, nullable=False)
    tipoUsuario = Column(String, nullable=False)
    estatus = Column(String, nullable=False)

    def is_vendedor(self):
        if self.tipoUsuario=="Vendedor":
            return True
        else:
            return False

    def is_administrador(self):
        if self.tipoUsuario=="Administrador":
            return True
        else:
            return False

    def is_almacenista(self):
        if self.tipoUsuario=="Almacenista":
            return True
        else:
            return False

    def is_authenticated(self):
        return True

    def is_active(self):
        if self.estatus=='A':
            return True
        else:
            return False
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.idUsuario

    def isValid(self,nomUsu,password):
        usuario = Usuario.query.filter(Usuario.nombreUsuario == nomUsu,Usuario.contraseña==password).first()
        if usuario != None and usuario.is_active():
            return usuario
        else:
            return None

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self,id):
        return self.query.get(id)

    def eliminar(self,id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    # def consultaGeneral(self):
    #     return self.query.order_by(Usuario.idUsuario.asc()).paginate(pagina, per_page=5, error_out=False).items
    #     # return self.query.all()


class Transportes(db.Model):
    __tablename__ = 'Transportes'
    idTransportes = Column(Integer, primary_key=True)
    nombre = Column(String(20))
    telefono=Column(String(10))
    estatus=Column(String(1))

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    # def consultaGeneral(self, pagina):
    #     return self.query.order_by(Transportes.idTransportes.asc()).paginate(pagina, per_page=5, error_out=False).items
    #     # return self.query.all()

class Productos(db.Model):
    __tablename__ = 'productos'
    idProducto = Column(Integer, primary_key=True)
    nombre = Column(String(20))
    descripcion = Column(String(50))
    precio = Column(Integer)
    Categoria = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    # def consultaGeneral(self, pagina):
    #     return self.query.order_by(Productos.idProducto.asc()).paginate(pagina, per_page=5, error_out=False).items
    #     # return self.query.all()

class Estante(db.Model):
    __tablename__ = 'Estante'
    idEstante=Column(Integer, primary_key=True)
    nombre = Column(String(3))
    ubicacion=Column(String(30))

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self,id):
        return self.query.get(id)

    def eliminar(self,id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    # def consultaGeneral(self, pagina):
    #     return self.query.order_by(Estante.idEstante.asc()).paginate(pagina, per_page=5, error_out=False).items
    #     # return self.query.all()

#########REPORTES#######
class Almacen(db.Model):
    __tablename__='almacen'
    idAlmacen = Column(Integer, primary_key=True)
    cantProducto = Column(Integer,nullable=False)
    Categoria = Column(String, nullable=False)
    Estante = Column(String, nullable=False)

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self,id):
        return self.query.get(id)

    def eliminar(self,id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

class ReporteAlmacen(db.Model):
    __tablename__ = 'reportealmacen'
    idReporteAlmacen = Column(Integer, primary_key=True)
    fecha = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    movimiento = Column(String, nullable=False)
    cantidad = Column(String, nullable=False)
    idAlmacen = Column(Integer, ForeignKey('almacen.idAlmacen'))
    Producto = Column(String, nullable=False)



    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self,id):
        return self.query.get(id)

    def eliminar(self,id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def editar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

##################Clientes
class Clientes(db.Model):
    __tablename__ = 'cliente'
    idCliente = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    direccion = Column(String(45))
    telefono = Column(String(10))
    RFC = Column(String(13))

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
    # def consultaGeneral(self, pagina):
    #     return self.query.order_by(Transportes.idTransportes.asc()).paginate(pagina, per_page=5, error_out=False).items
    #     # return self.query.all()

##################Categorias
class Categorias(db.Model):
    __tablename__ = 'Categorias'
    idCategorias = Column(Integer, primary_key=True)
    nombre = Column(String(20))

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

#####Ventas
class Ventas(db.Model):
    __tablename__ = 'ventas'
    idVentas = Column(Integer, primary_key=True)
    fecha = Column(Date)
    total=Column(Integer)
    pago=Column(Integer)
    tipoVenta = Column(String(10))
    estatus = Column(String(1))
    Usuario = Column(String(15))
    Cliente = Column(String(30))
    TipoPago = Column(String(15))

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

class DetalleVenta(db.Model):
    __tablename__ = 'DetalleVenta'
    idDetalleVenta = Column(Integer, primary_key=True)
    cantidad = Column(Integer, nullable=False)
    precio = Column(Integer, nullable=False)
    subTotal = Column(Integer)
    idVentas = Column(Integer)
    Producto = Column(String(30))

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def editar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

##################Envio
class Envio(db.Model):
    __tablename__ = 'Envio'
    idEnvio = Column(Integer, primary_key=True)
    precio = Column(Integer)
    Transportes = Column(String(30))
    idVentas = Column(Integer)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()