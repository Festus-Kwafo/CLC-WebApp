from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    one_day = models.BooleanField(default=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    main_event = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event', args=[str(self.id)])

    def get_date_range(self):
        return self.start_date.strftime('%b %d') + ' - ' + self.end_date.strftime('%b %d, %Y')
