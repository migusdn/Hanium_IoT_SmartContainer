from django.forms import ModelForm
from Container.main.models import Container
from . import models

class containerDetailForm(ModelForm):

    class Meta:
        model = Container
        fields = ['ContainerID', 'PortID', 'PortName', 'PortExportDate']

        #, 'PortEntryYear', 'PortEntryCount', 'PortImportDate', 'PortExportDate', 'ShipKoName', 'ShipEngName', 'ShipTypeCode', 'ShipTypeName', 'CheckInOut'


