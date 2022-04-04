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
    idUsuario=Column(Integer, primary_key=True)
    nombreCompleto = Column(String(40))
    nombreUsuario=Column(String(10))
    contraseña=Column(String(10))
    tipoUsuario=Column(String(15))
    estatus=Column(String(1))


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
