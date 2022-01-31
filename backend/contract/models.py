from django.db import models




# Create your models here.
class Contracts(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(max_length=100, null=False, unique=True)    

    def __str__(self):
        return self.name

class Rates():
    contract = models.ForeignKey(Contracts, on_delete=models.CASCADE,related_name='rate_contract')
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    currency = models.CharField(max_length=4)
    twenty = models.DecimalField(max_digits=4)
    forty = models.DecimalField(max_digits=4)
    fortyhc = models.DecimalField(max_digits=4)

    
    