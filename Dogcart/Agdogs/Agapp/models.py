from django.db import models
 
class DogsBreed(models.Model):
    id = models.AutoField(primary_key=True)
    breed = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.breed)

class Dogs(models.Model):
    name = models.CharField(max_length=100)
    breed = models.ForeignKey(DogsBreed, on_delete=models.CASCADE, related_name='dogsbreed')
    age = models.IntegerField()
    price = models.DecimalField(max_digits=15,decimal_places=2)