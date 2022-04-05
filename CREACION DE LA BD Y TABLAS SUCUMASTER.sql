
/*Creacion de la BD sucumaster*/
create database sucumaster;
use sucumaster;
/*Creación de tablas*/
create table Transportes (
idTransportes int auto_increment not null,
nombre varchar(20) not null,
telefono varchar(10) not null,
estatus varchar(1) not null,
constraint pk_Transportes primary key (idTransportes),
constraint uk_nombre_Transportes unique (nombre)
);

create table Especiales (
idEspeciales int auto_increment not null,
nombre varchar(20),
descripcion varchar(20),
costo int,
constraint pk_Especiales primary key (idEspeciales)
);

create table Cliente (
idCliente int auto_increment not null,
nombre varchar(30) not null,
direccion varchar(45) not null,
telefono varchar(10) not null,
RFC varchar(13) not null,
constraint pk_Cliente primary key (idCliente)
);


create table Categorias (
idCategorias int auto_increment not null,
nombre varchar(15) not null,
constraint pk_Categorias primary key (idCategorias)
);

create table TipoPago (
idTipoPago int auto_increment not null,
tipo varchar(10) not null,
constraint pk_TipoPago primary key (idTipoPago)
);

create table Estante (
idEstante int auto_increment not null,
nombre varchar(3) not null,
ubicacion varchar(30) not null,
constraint pk_Estante primary key (idEstante)
);

create table Usuario (
idUsuario int auto_increment not null,
nombreCompleto varchar(40) not null,
nombreUsuario varchar(10) not null,
contraseña varchar(10) not null,
tipoUsuario varchar(15) not null,
estatus varchar(1) not null,
constraint pk_Usuario primary key (idUsuario)
);

create table Ventas (
idVentas int auto_increment not null,
fecha date not null,
total int not null,
pago int not null,
tipoVenta varchar(10) not null,
estatus varchar(1) not null,
idUsuario int not null,
idCliente int not null,
idTipoPago int not null,
constraint pk_Ventas primary key (idVentas),
constraint fk_Usuario_Ventas foreign key(idUsuario) 
references Usuario(idUsuario),
constraint fk_Cliente_Ventas foreign key(idCliente) 
references Cliente(idCliente),
constraint fk_TipoPago_Ventas foreign key(idTipoPago) 
references TipoPago(idTipoPago)
);

create table Envio (
idEnvio int auto_increment,
tipoEnvio varchar(10),
precio int,
idTransportes int,
idVentas int,
constraint pk_Envio primary key (idEnvio),
constraint fk_Transportes_Envio foreign key(idTransportes) 
references Transportes(idTransportes),
constraint fk_Ventas_Envio foreign key(idVentas) 
references Ventas(idVentas)
);

create table CargosExtra (
idCargosExtra int auto_increment,
unidades int,
costo int,
subTotal int,
idEspeciales int ,
idVentas int,
constraint pk_CargosExtra primary key (idCargosExtra),
constraint fk_Especiales_CargosExtra foreign key(idEspeciales) 
references Especiales(idEspeciales),
constraint fk_Ventas_CargosExtra foreign key(idVentas) 
references Ventas(idVentas)
);

create table Productos (
idProducto int auto_increment not null,
nombre varchar(20) not null,
descripcion varchar(50),
precio int not null,
idCategorias int not null,
constraint pk_Productos primary key (idProducto),
constraint fk_Usuario_Categorias foreign key(idCategorias) 
references Categorias(idCategorias)
);

create table DetalleVenta (
idDetalleVenta int auto_increment not null,
cantidad int not null,
precio int not null,
subTotal int not null,
idVentas int not null,
idProducto int not null,
constraint pk_DetalleVenta primary key (idDetalleVenta),
constraint fk_Ventas_DetalleVenta foreign key(idVentas) 
references Ventas(idVentas),
constraint fk_Productos_DetalleVenta foreign key(idProducto) 
references Productos(idProducto)
);

create table DetalleEnvio (
idDetalleEnvio int auto_increment,
cantEnviada int,
cantRecibida int,
cantAceptada int,
idEnvio int,
idDetalleVenta int,
constraint pk_DetalleEnvio primary key (idDetalleEnvio),
constraint fk_Envio_DetalleEnvio foreign key(idEnvio) 
references Envio(idEnvio),
constraint fk_DetalleVenta_DetalleEnvio foreign key(idDetalleVenta) 
references DetalleVenta(idDetalleVenta)
);

create table Anticipo (
idAnticipo int auto_increment not null,
fecha date not null,
importe int,
idTipoPago int not null,
idVentas int not null,
constraint pk_Anticipo primary key (idAnticipo),
constraint fk_TipoPago_Anticipo foreign key(idTipoPago) 
references TipoPago(idTipoPago),
constraint fk_Ventas_Anticipo foreign key(idVentas) 
references Ventas(idVentas)
);

create table Almacen (
idAlmacen int auto_increment not null,
cantProducto int not null,
idProducto int not null,
idEstante int not null,
constraint pk_Almacen primary key (idAlmacen),
constraint fk_Productos_Almacen foreign key(idProducto) 
references Productos(idProducto),
constraint fk_Estante_Almacen foreign key(idEstante) 
references Estante(idEstante)
);

create table ReporteAlmacen (
idReporteAlmacen int auto_increment,
fecha date,
descripcion varchar(50),
movimiento varchar(45),
cantidad int,
idAlmacen int,
idProducto int,
constraint pk_ReporteAlmacen primary key (idReporteAlmacen),
constraint fk_Almacen_ReporteAlmacen foreign key(idAlmacen) 
references Almacen(idAlmacen),
constraint fk_Productos_ReporteAlmacen foreign key(idProducto) 
references Productos(idProducto)
);

/*use sucumaster;
create user userSucuMaster identified by 'hola.123';
grant insert,update,delete,select on TipoPago to userSucuMaster;
*/
