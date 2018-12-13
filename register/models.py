from django.utils.timezone import now, timedelta
from django.db import models
from secrets import token_urlsafe


class Token(models.Model):
    code = models.CharField(max_length=43)
    expiry = models.DateTimeField()


    def save(self, *args, **kwargs):
        if not self.code:
            self.code = token_urlsafe()
        if not self.expiry:
            self.expiry = now() + timedelta(days=1)
        return super(Token, self).save(*args, **kwargs)


    def is_valid(self):
        return self.expiry > now()


    def consume(self):
        if self.expiry:
            self.expiry -= timedelta(days=1)


    def __str__(self):
        return "{} [{}]".format(self.code, self.expiry)

