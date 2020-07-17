from django.db import models


# Create your models here.
class Missions(models.Model):
    mission = models.CharField(max_length=500, db_index=True, verbose_name="Mission")
    is_completed = models.BooleanField(default=False, verbose_name="Is completed ?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mission}"
