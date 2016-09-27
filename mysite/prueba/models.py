from django.db import models

# Create your models here.
class Usuario(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)

	class Meta:
		db_table = 'Usuario'

	def natural_key(self):
		return {'nombre':self.nombre,'apellido':self.apellido}

	def __str__(self):
		return self.nombre

	def get_json(self):
		return {'id':self.id,'nombre':self.nombre,'apellido':self.apellido}


class Universidad(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)
	aprobado = models.BooleanField(default=False)

	class Meta:
		db_table = 'Universidad'

	def natural_key(self):
		return {'nombre':self.nombre,'direccion':self.direccion,'aprobado':self.aprobado}

	def __str__(self):
		return self.nombre

	def get_json(self):
		return {'id':self.id,'nombre':self.nombre,'direccion':self.direccion,'aprobado':self.aprobado}
	

class Companero(models.Model):
	id = models.AutoField(primary_key=True)
	id_usuario_uno = models.ForeignKey(Usuario, related_name='usuario')
	id_usuario_dos = models.ForeignKey(Usuario, related_name='companero')
	id_universidad = models.ForeignKey(Universidad)

	class Meta:
		db_table = 'Companero'

	def get_json(self):
		return {'id':self.id,'id_usuario_uno':self.id_usuario_uno.get_json(),'id_usuario_dos':self.id_usuario_dos.get_json(),'id_universidad':self.id_universidad.get_json()}