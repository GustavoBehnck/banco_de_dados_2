from django.db import models

from django.db import models

class Client(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]

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


class Vehicle(models.Model):
    VEHICLE_STATES = [
        ('in use', 'Em uso'),
        ('ready', 'Disponível'),
        ('not ready', 'Indisponível momentaneamente'), # e.g. manutenção
        ('decomissioned', 'Decomissionada'),
    ]

    status = models.CharField(max_length=20,choices=VEHICLE_STATES)
    chassis = models.CharField(max_length=255, help_text="Consulte o manual do modelo para encontrar o chassi do veículo")
    observation = models.TextField(blank=True, null=True, verbose_name="Observação")
    model = models.ForeignKey(
        'VehicleModel',
        on_delete=models.CASCADE,
        related_name='vehicles',
        verbose_name="Modelo"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "vehicles"

    def __str__(self):
        return f"({self.id}) {self.model}, {self.chassis} - {self.status}"


class Contract(models.Model):
    lease_deed = models.TextField(verbose_name="Texto do contrato")
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name="contracts", verbose_name="Cliente")
    status = models.BooleanField(default=False, verbose_name="Está aprovado?")
    start_date = models.DateTimeField(verbose_name="Data de vigência")
    end_date = models.DateTimeField(verbose_name="Data de expiração")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contracts'

    def __str__(self):
        return f"Contrato {self.id} de cliente {self.client}"


class VehicleContract(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='vehicles_contracted')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicles_contracted')
    observation = models.TextField(blank=True, null=True, verbose_name="Observações")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'vehicles_contracted'

    def __str__(self):
        return f"{self.vehicle} em {self.contract}"

class JobsLog(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='jobs_logs')
    started_date = models.DateTimeField(verbose_name="Início das atividades")
    finished_date = models.DateTimeField(blank=True, null=True, verbose_name="Término das atividades")
    observation = models.TextField(blank=True, null=True, verbose_name="Observações")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'jobs_log'

    def __str__(self):
        if not self.finished_date:
            return f"Atividades do veículo {self.vehicle} começaram em {self.started_date}"
        else:
            return f"Atividades do veículo {self.vehicle} começaram em {self.started_date} e terminaram em {self.finished_date}"


class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='maintenances', verbose_name="Veículo")
    date = models.DateTimeField(verbose_name="Data de manutenção")
    reason = models.TextField(verbose_name="Justificativa")
    link_to_ticket = models.CharField(max_length=1024, blank=True, null=True, verbose_name="Link do ticket", help_text="Esse é o ID do ticket no ServiceNow")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'maintenances'

    def __str__(self):
        return f"Manutenção para {self.vehicle} em {self.date}"

