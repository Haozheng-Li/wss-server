from django.utils import timezone
from django.db import models
from apps.accounts.models import Users


class Devices(models.Model):
    NODE_TYPE_CHOICES = (
        ('motion detect', 'MotionDetect'),
        ('gateway', 'Gateway'),
    )
    DEVICE_TYPE_CHOICES = (
        ('Raspberry Pi', 'Raspberry Pi'),
    )
    PROTOCOL_CHOICES = (
        ('HTTP', 'HTTP'),
    )
    SDK_CHOICES = (
        ('Python', 'Python'),
        ('C++', 'C++'),
        ('C', 'C'),
    )
    STATUS_CHOICES = (
        ('inactive', 'Inactive'),
        ('active', 'Active'),
        ('enable', 'Enable'),
        ('disable', 'Disable'),
    )

    device_name = models.CharField(max_length=200, blank=False)
    node_type = models.CharField(max_length=200, choices=NODE_TYPE_CHOICES, default='motion detect')
    device_type = models.CharField(max_length=200, choices=DEVICE_TYPE_CHOICES, default='Raspberry Pi')
    api_key = models.CharField(max_length=150, editable=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='enable')
    protocol = models.CharField(max_length=50, choices=PROTOCOL_CHOICES, default='HTTP')
    sdk = models.CharField(max_length=50, choices=SDK_CHOICES, default='Python')
    suc_conv_num = models.PositiveIntegerField(default=0)
    failed_conv_num = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    last_login_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ("-created_time",)
        verbose_name = "Devices"
        verbose_name_plural = "Devices"

    def __str__(self) -> str:
        return str(self.device_name)
