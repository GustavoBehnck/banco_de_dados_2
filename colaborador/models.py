from django.db import models

from django.db import models

class Client(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]

    id = models.AutoField(primary_key=True)  # Auto-incrementing PK
    cnpj = models.CharField(max_length=255, unique=True, verbose_name="CNPJ")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    trade_name = models.CharField(max_length=255, db_comment="Nome fantasia", verbose_name="Nome fantasia")
    company_name = models.CharField(max_length=255, unique=True, db_comment="Razão social", verbose_name="Razão social")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "clients"
    
    def __str__(self):
        return self.trade_name
