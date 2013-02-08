from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=256, null=False, blank=False)

    # ...
    def __unicode__(self):
        return u'%s' % (self.email )