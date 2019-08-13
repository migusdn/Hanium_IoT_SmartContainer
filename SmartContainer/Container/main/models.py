from django.db import models

class Container(models.Model):
    ContainerID = models.CharField(max_length=100, null=True)
    SizeType = models.CharField(max_length=100, null=True)
    TotalWeight = models.CharField(max_length=100, null=True)
    Msn = models.CharField(max_length=100, null=True)
    Section = models.CharField(max_length=100, null=True)
    MBLNum = models.CharField(max_length=10, null=True)
    GoodsClassify = models.CharField(max_length=100, null=True)
    Pol = models.CharField(max_length=100, null=True)
    LeavePlace = models.CharField(max_length=100, null=True)
    LeaveClassify = models.CharField(max_length=100, null=True)
    LoadID = models.CharField(max_length=100, null=True)
    GoodsName = models.CharField(max_length=100, null=True)
    CarryingDate = models.CarryingDate(max_length=100, null=True)
    # PortEntryYear = models.CharField(max_length=100, null=True)
    # PortEntryCount = models.CharField(max_length=100, null=True)
    # PortImportDate = models.CharField(max_length=100, null=True)
    # ShipKoName = models.CharField(max_length=100, null=True)
    # ShipEngName = models.CharField(max_length=100, null=True)
    # ShipTypeCode = models.CharField(max_length=100, null=True)
    # ShipTypeName = models.CharField(max_length=100, null=True)
    # CheckInOut = models.CharField(max_length=100, null=True)
    # CheckInOutName = models.CharField(max_length=100, null=True)
    # LaidupCode = models.CharField(max_length=100, null=True)
    # LaidupSubCode = models.CharField(max_length=100, null=True)
    # LaidupPlace = models.CharField(max_length=100, null=True)
    # CheckDoor = models.CharField(max_length=100, null=True)
    # TemInfo = models.CharField(max_length=100, null=True)
    # WetInfo = models.CharField(max_length=100, null=True)
    # LocaInfo = models.CharField(max_length=100, null=True)
    # ContainerInfo = models.CharField(max_length=100, null=True)
    # ContainerloadInfo = models.CharField(max_length=100, null=True)
    # VibInfo = models.CharField(max_length=100, null=True)
    # BatteryInfo = models.CharField(max_length=100, null=True)
    # SecInfo = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['-Msn']       #Msn 기준 내림차순 정렬



