from django.db import models
from django.forms import ModelForm
from gui.validator import *
from users.models import User

# Create your models here.
class Server(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=128, null=False,blank=False)

    # ...
    def __unicode__(self):
        return u'%s' % (self.type )

class Host(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False,blank=False)

    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

class DataCenter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False,blank=False)

    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

class Cluster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False,blank=False)

    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

class Configuration(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=False, null=False)
    server = models.ForeignKey(Server, blank=False, null=False)
    cpu = models.IntegerField(blank=False,null=False,default=4,validators=[validate_even,validate_cpu])
    memory = models.IntegerField(blank=False,null=False,default=4,validators=[validate_even,validate_memory])
    host = models.ForeignKey(Host, blank=False, null=False)
    data_center = models.ForeignKey(DataCenter, blank=False, null=False)
    cluster = models.ForeignKey(Cluster, blank=False, null=False)
    # ...
    def __unicode__(self):
        return u'%s-%s-%s' % ( self.data_center, self.cpu, self.cluster.id )

class ConfigurationForm(ModelForm):
    class Meta:
        model = Configuration
        fields = ('server', 'cpu','memory','host','data_center','cluster')