from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mobile_no = models.BigIntegerField()
    message = models.TextField()

    

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name

class ScheduleVisit(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    message = models.TextField()

    

    class Meta:
        verbose_name = ("ScheduleVisit")
        verbose_name_plural = ("ScheduleVisits")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ScheduleVisit_detail", kwargs={"pk": self.pk})

