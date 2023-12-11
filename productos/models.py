from django.db import models


STATUS_CHOICES = (
    (1, 'Entregado'),
    (2, 'En Transito'),
)
CITY_ORIGIN = (
    ('TOLUCA', 'Toluca'),
    ('METEPEC', 'Metepec'),
)
CITY_DESTINY = (
    ('CDMX', 'Ciudad de Mexico'),
    ('QUERETARO', 'Queretaro'),
    ('MONTERREY', 'Monterrey'),
)

#Modelo de Inventario
class Inventario(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    stock = models.IntegerField()
    stockl = models.IntegerField()
    stockr = models.IntegerField()
    cantidad_maxima = models.IntegerField()
    cantidad_minima = models.IntegerField()
    venta_maxima = models.IntegerField()
    venta_minima = models.IntegerField()
    BoM = models.IntegerField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES)
    def __str__(self):
        return self.nombre

#Modelo de Solicitud
class Solicitud(models.Model):
    caja_de_airpods = models.IntegerField()
    caja_de_telefono = models.IntegerField()
    caja_de_cargador = models.IntegerField()
    plastico_para_carcasas_de_iphone = models.IntegerField()
    plastico_para_carcasas_de_airpods = models.IntegerField()
    caja_de_cable = models.IntegerField()

    def __str__(self):
        return f'Solicitud {self.id}'
    

#Modelo para los envios
class Envio(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE,default=None)
    origen = models.CharField(max_length=255,choices=CITY_ORIGIN)
    destino = models.CharField(max_length=255, choices=CITY_DESTINY)
    fecha = models.DateField()
    peso = models.IntegerField()

    def __str__(self):
        return f"Envío de {self.origen} a {self.destino} con fecha {self.fecha} y peso {self.peso} kg"

#Modelo para las Piezas Plasticas    
class PlasticParts(models.Model):
    caja_de_airpods = models.IntegerField(default=0)
    caja_de_telefono = models.IntegerField(default=0)
    caja_de_cargador = models.IntegerField(default=0)
    plastico_para_carcasas_de_iphone = models.IntegerField(default=0)
    plastico_para_carcasas_de_airpods = models.IntegerField(default=0)
    caja_de_cable = models.IntegerField(default=0)

#Modelo para Piezas electronicas
class ElectronicParts(models.Model):
    cameras = models.IntegerField(default=0)
    biometric_sensors = models.IntegerField(default=0)
    baseband = models.IntegerField(default=0)
    power_management = models.IntegerField(default=0)
    processor = models.IntegerField(default=0)
    nand = models.IntegerField(default=0)
    dram = models.IntegerField(default=0)
    accelerometer = models.IntegerField(default=0)
    battery = models.IntegerField(default=0)
    microphone = models.IntegerField(default=0)
    speakers = models.IntegerField(default=0)