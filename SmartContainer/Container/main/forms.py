from django.forms import ModelForm


from .models import Container

class containerForm(ModelForm):

    class Meta:
        model = Container
        fields = ['ContainerID', 'SizeType', 'TotalWeight', 'GoodsName', 'GoodsClassify',  'Section', 'LeavePlace', 'CarryingDate']

        #, 'PortEntryYear', 'PortEntryCount', 'PortImportDate', 'PortExportDate', 'ShipKoName', 'ShipEngName', 'ShipTypeCode', 'ShipTypeName', 'CheckInOut'