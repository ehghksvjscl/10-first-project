from django.db import models


class TempDate(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "core"
        abstract = True
