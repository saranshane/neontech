from django.db import models

class SosSetting(models.Model):
    id = models.BigAutoField(primary_key=True)  # Automatically generated primary key
    mobile_number_1 = models.CharField(max_length=15)  # Adjust max_length as needed
    mobile_number_2 = models.CharField(max_length=15, blank=True, null=True)  # Optional field
    gps_location = models.CharField(max_length=255, blank=True, null=True)  # Adjust max_length as needed

    def __str__(self):
        return f"SOS Setting {self.id} - {self.mobile_number_1}"

