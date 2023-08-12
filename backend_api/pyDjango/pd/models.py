from django.db import models

class DealsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    deal_url = models.CharField(max_length=500)
    img_url = models.CharField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


