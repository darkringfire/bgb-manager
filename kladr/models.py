from django.db import models

region_id = '3800000000000'

class KladrManager(models.Manager):
    def get_queryset(self):
        return models.QuerySet()


class Region(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False

    def __str__(self):
        return self.name


