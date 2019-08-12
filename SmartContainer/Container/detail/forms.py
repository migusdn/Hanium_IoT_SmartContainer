from django.forms import ModelForm
from Container.main.models import Container
from . import models

class containerDetailForm(ModelForm):

    class Meta:
        model = Container
        fields = ['ContainerID', 'SizeType', 'TotalWeight', 'Section', 'MBLNum', 'Msn', 'GoodsClassfiy', 'Pol',
                  'LeavePlace', 'LeaveClassfiy', 'LoadID', 'GoodsName']

        #, 'PortEntryYear', 'PortEntryCount', 'PortImportDate', 'PortExportDate', 'ShipKoName', 'ShipEngName', 'ShipTypeCode', 'ShipTypeName', 'CheckInOut'


