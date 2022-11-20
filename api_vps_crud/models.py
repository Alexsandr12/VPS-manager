import uuid
from django.db import models


class Vps(models.Model):
    STATUS_VPS = [
        ("SR", "started"),
        ("BL", "blocked"),
        ("SP", "stopped"),
    ]
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpu = models.SmallIntegerField(null=False)
    hdd = models.SmallIntegerField(null=False)
    ram = models.SmallIntegerField(null=False)
    status = models.CharField(max_length=2, choices=STATUS_VPS, default="SR")

    class Meta:
        verbose_name_plural = "VPS"
