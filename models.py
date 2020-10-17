from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Cliente(models.Model):
    nm_usuario = models.CharField(max_length=100)
    nr_telefone = models.CharField(max_length=11)
    ds_email = models.EmailField()
    ds_endereco = models.TextField()
    dt_inicio = models.DateTimeField(auto_now_add=True)
    im_foto = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'T_NDV_CLIENTE'
