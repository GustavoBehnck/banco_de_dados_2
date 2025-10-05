from django.contrib import admin
from .models import (
    Client, Farm, VehicleModel, Vehicle, Contract,
    VehicleContract, JobsLog, Maintenance
)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('trade_name', 'company_name', 'cnpj', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('trade_name', 'company_name', 'cnpj')


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'cep', 'address', 'area', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'client')
    search_fields = ('name', 'client__trade_name', 'cep', 'address')


@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ('type', 'fabrication_year', 'battery_capacity', 'charging_time', 'created_at', 'updated_at')
    list_filter = ('type',)
    search_fields = ('type',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'chassis', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'model')
    search_fields = ('chassis', 'model__type')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'status', 'start_date', 'end_date', 'created_at', 'updated_at')
    list_filter = ('status', 'client')
    search_fields = ('client__trade_name',)


@admin.register(VehicleContract)
class VehicleContractAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'contract', 'created_at', 'updated_at')
    list_filter = ('vehicle', 'contract')
    search_fields = ('vehicle__chassis', 'contract__id')


@admin.register(JobsLog)
class JobsLogAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'started_date', 'finished_date', 'created_at', 'updated_at')
    list_filter = ('vehicle',)
    search_fields = ('vehicle__chassis',)


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'date', 'reason', 'link_to_ticket', 'created_at', 'updated_at')
    list_filter = ('vehicle', 'date')
    search_fields = ('vehicle__chassis', 'reason', 'link_to_ticket')
