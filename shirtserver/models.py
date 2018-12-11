from django.db import models

class Shirt(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    pub_date = models.DateField()
    TYP = (
        ('M', 'M'),
        ('F', 'F'),
    )
    typ = models.CharField(max_length=1, choices=TYP)
    SIZE = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
    )
    size = models.CharField(max_length=4, choices=SIZE)

    color = models.CharField(max_length=30, null = True)
    image = models.ImageField(upload_to='static/shirtserver/images/', verbose_name='image', null = True)

    def __str__(self):
        return self.name
