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
        if self.one_day:
            return self.start_date.strftime('%b %d, %Y')
        return self.start_date.strftime('%b %d') + ' - ' + self.end_date.strftime('%b %d, %Y')

    def get_time(self):
        if self.one_day:
            return self.start_date.strftime('%I:%M %p')
        return self.start_date.strftime('%I:%M %p')


class Message(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    publish_date = models.DateTimeField()
    published = models.BooleanField(default=False)
    cover_art = models.ImageField(upload_to='images/messages/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('message', args=[str(self.slug)])
