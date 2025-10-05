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


class Farm(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]

    name = models.CharField(max_length=255, verbose_name="Nome da fazenda")
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='farms', verbose_name="Propriedade de")
    cep = models.CharField(max_length=20, verbose_name="CEP")
    address = models.CharField(max_length=255, verbose_name="Endereço")
    area = models.FloatField(verbose_name="Área (ha)", help_text="ha = hectares")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "farms"
    
    def __str__(self):
        return "self.name"


class VehicleModel(models.Model):
    """
    Modelos de veículos
    """
    MODEL_CHOICES = [
        ('planting', 'Semeadora'),
        ('spraying', 'Pulverizador'),
        ('harvesting', 'Colheitadora'),
    ]

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20,choices=MODEL_CHOICES, verbose_name="Tipo")
    battery_capacity = models.FloatField(verbose_name="Capacidade da bateria (Wh)") # TODO revisit this
    fabrication_year = models.IntegerField(verbose_name="Ano do modelo")
    charging_time = models.FloatField(verbose_name="Tempo de recarga (h)", help_text="Tempo para completar um ciclo de carregamento, em horas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "models"
    
    def __str__(self):
        return f"{self.type} ({self.fabrication_year})"

