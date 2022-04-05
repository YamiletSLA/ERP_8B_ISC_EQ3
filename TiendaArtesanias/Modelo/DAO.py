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
    __tablename__ = 'Usuario'
    idUsuario = Column(Integer, primary_key=True)

    nombreCompleto = Column(String, nullable=False)
    nombreUsuario = Column(String, nullable=False)
    contraseña = Column(String(128), nullable=False)
    estatus = Column(String, nullable=False)

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