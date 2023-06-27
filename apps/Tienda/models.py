from django.db import models
# Create your models here.


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50,null=False) 
    def __str__(self):
        txt = "nombre: {0} - ID : {1}"
        return txt.format(self.nombre_categoria,self.id_categoria)


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=30,null=False)
    precio_producto = models.CharField(max_length=30,null=False)
    cantidad_producto = models.IntegerField(null=False)
    categoria_id = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenesProducto')






