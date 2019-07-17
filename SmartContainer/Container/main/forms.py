from django.forms import ModelForm


from .models import Container

class containerForm(ModelForm):

    class Meta:
        model = Container
        fields = ['ContainerID', 'PortID', 'PortName', 'PortExportDate']

        #, 'PortEntryYear', 'PortEntryCount', 'PortImportDate', 'PortExportDate', 'ShipKoName', 'ShipEngName', 'ShipTypeCode', 'ShipTypeName', 'CheckInOut'


