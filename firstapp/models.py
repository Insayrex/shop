from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "{0} {1} - {2}".format(self.id, self.name, self.email)

