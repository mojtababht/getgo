from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import HttpResponse
import requests
from django_jalali.db import models as jmodels

class Address(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    lat = models.FloatField(null=True,blank=False)
    long = models.FloatField(null=True,blank=False)
    formated=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return str(self.name)
@receiver(post_save,sender=Address)
def setName(sender, instance, created, **kwargs):
    if created:
        data={'lat':instance.lat,'lng':instance.long}
        r=requests.get('https://api.neshan.org/v5/reverse?lat={}&lng={}'.format(instance.lat,instance.long),
        headers ={

        "Api-Key": "service.03aa018ac2c2439c9270d67fb8282bfd"
        }
        )
        try:
            instance.name=r.json()['route_name']
            instance.formated=r.json()['formatted_address']
            instance.save()
        except:
            pass




class Request(models.Model):
    user=models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    driver=models.ForeignKey('account.CustomUser',on_delete=models.SET_NULL,null=True,blank=True,related_name='req_driver')
    req_date=jmodels.jDateField(auto_now_add=True)
    package=models.ForeignKey('Package',on_delete=models.CASCADE)
    type=models.CharField(max_length=50,choices=[('regular','معمولی'),('instance','فوری')])
    sAddress=models.ForeignKey('Address',on_delete=models.CASCADE,related_name='saddress')
    dAddress=models.ForeignKey('Address',on_delete=models.CASCADE,related_name='daddress')
    sended=models.BooleanField(default=False)
    accepted=models.BooleanField(default=False)
    price=models.IntegerField()

    def __str__(self):
        return str(self.user)+" "+self.type
    def get_type(self):
        TYPE_CHOICES = [
            ('regular', 'معمولی'),
            ('instance', 'فوری'),
        ]
        type=dict(TYPE_CHOICES)
        return type.get(self.type)


class Package(models.Model):
    weight=models.CharField(max_length=50,choices=[('small','کوچک'),('normal','متوسط'),('large','بزرگ')])
    def __str__(self):
        return self.weight