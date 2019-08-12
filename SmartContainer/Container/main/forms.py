from django.forms import ModelForm


from .models import Container

class containerForm(ModelForm):

    class Meta:
        model = Container
        fields = ['ContainerID', 'SizeType', 'TotalWeight', 'Section', 'MBLNum', 'Msn', 'GoodsClassify', 'Pol', 'LeavePlace', 'LeaveClassify', 'LoadID', 'GoodsName']

        #, 'PortEntryYear', 'PortEntryCount', 'PortImportDate', 'PortExportDate', 'ShipKoName', 'ShipEngName', 'ShipTypeCode', 'ShipTypeName', 'CheckInOut'



