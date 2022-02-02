from django.db import models




# Create your models here.
class Contract(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(max_length=100, null=False, unique=True)

    class Meta:
        ordering = ('slug',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class Rates(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, to_field="slug", db_column="contract")
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    currency = models.CharField(max_length=4)
    twenty = models.DecimalField(max_digits=6, decimal_places=2)
    forty = models.DecimalField(max_digits=6, decimal_places=2)
    fortyhc = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.contract.slug)


    
    