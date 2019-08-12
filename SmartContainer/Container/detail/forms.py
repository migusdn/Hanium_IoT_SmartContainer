from django.forms import ModelForm
from detail.models import Detail
from . import models

class DetailForm(ModelForm):

    class Meta:
        model = Detail
        fields = ['ContainerID', 'Temper', 'Humid', 'SetTemper', 'SetHumid', 'Door', 'UpTemper', 'DoTemper',
                  'UpHumid', 'DoHumid']

        #, 'PortEntryYear', 'PortEntryCount', 'PortImportDate', 'PortExportDate', 'ShipKoName', 'ShipEngName', 'ShipTypeCode', 'ShipTypeName', 'CheckInOut'


