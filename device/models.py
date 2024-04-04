from django.db import models


# Create your models here.
class Device(models.Model):
    Device_datatype = models.ForeignKey('Device_datatype', on_delete=models.CASCADE)
    device_name = models.CharField(verbose_name='设备名称', max_length=128)

    class Meta:
        db_table = "device"


# 设备表
class Device_datatype(models.Model):
    binary_type = models.BooleanField(verbose_name='二元类型', null=True)
    value_type = models.BooleanField(verbose_name='数值类型', null=True)
    diff_typr = models.BooleanField(verbose_name='微分类型', null=True)
    inte_type = models.BooleanField(verbose_name='积分类型', null=True)

    class Meta:
        db_table = "device_datatype"


# 转接表
class Binary(models.Model):
    uid = models.ForeignKey('Device_datatype', on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name='状态')

    class Meta:
        db_table = "Binary"


class Value(models.Model):
    uid = models.ForeignKey('Device_datatype', on_delete=models.CASCADE)
    value = models.FloatField(verbose_name='数值')

    class Meta:
        db_table = "value"


class Differential(models.Model):
    uid = models.ForeignKey('Device_datatype', on_delete=models.CASCADE)
    differential = models.FloatField(verbose_name='微分数值')

    class Meta:
        db_table = "differential"


class Integral(models.Model):
    uid = models.ForeignKey('Device_datatype', on_delete=models.CASCADE)
    integral = models.FloatField(verbose_name='积分数值')

    class Meta:
        db_table = "integral"
