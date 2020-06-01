from django.db import models
from datetime import date

# Create your models here.
class Hotelinfo(models.Model):
    hotelid=models.CharField(max_length=20,primary_key=True)
    hotelname=models.CharField(max_length=40,default=None)
    loc=models.CharField(max_length=40, default=None)

    def __str__(self):
        return self.hotelid

class Roominformation(models.Model):
    roomid=models.CharField(primary_key=True,max_length=20)
    hotel=models.ForeignKey(Hotelinfo,default=None,on_delete=models.CASCADE,related_name="hotel")
    roomtype=models.CharField(db_column='RoomType', max_length=20)
    price=models.IntegerField()
    image=models.ImageField(upload_to='pics')
    sdate=models.DateField(default=date.today)
    edate=models.DateField(default=date.today)

    def __str__(self):
        return self.roomtype

class Bookingdetails1(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user_name=models.CharField(max_length=1000)
    email=models.EmailField(max_length=20)
    phone=models.IntegerField()
    startdate=models.DateField()
    enddate=models.DateField()
    address1=models.CharField(max_length=100)
    hotel1=models.ForeignKey(Hotelinfo,default=None,on_delete=models.CASCADE)
    room1=models.ForeignKey(Roominformation,default=None,on_delete=models.CASCADE)
    
    
    
    
