from django.utils import timezone
from django.db import models
from secrets import token_urlsafe


class Token(models.Model):
    code = models.CharField(max_length=43)
    expiry = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.code = token_urlsafe()
            self.expiry = timezone.now() + timezone.timedelta(days=1)
        super(Token, self).save(*args, **kwargs)


    def is_valid(self):
        return self.expiry > timezone.now()


    def __str__(self):
        return "{} ({})".format(self.code, self.expiry)
