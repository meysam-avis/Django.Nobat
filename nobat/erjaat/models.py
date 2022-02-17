from django.db import models

# Create your models here.
class Erjaat(models.Model):

    BAKHSH_LIST = [
        ('01', '01'),
        ('02', '02'),
        ('07', '07'),
    ]
    BABAT_LIST = [
        ('بازدید', 'بازدید'),
        ('تفکیک', 'تفکیک'),
    ]
    asli = models.CharField(max_length=10,null=True)
    faree= models.CharField(max_length=10,null=True)
    bakhsh = models.CharField(max_length=3,choices=BAKHSH_LIST, default='02')
    babat = models.CharField(max_length=250, choices=BABAT_LIST, default='بازدید')
    malek_mellicode = models.CharField(max_length=11, null=True)
