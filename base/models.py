from django.db import models
import datetime
import os
from django.core.validators import RegexValidator

class Category(models.Model):
    name = models.CharField(unique=True,max_length=40,db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ("position",)
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

class Event(models.Model):

    def get_date_name(self, filename: str) -> str:
        file_ext = "." + filename.strip().split(".")[-1]
        date = "Party_picture"+str(datetime.datetime.now()).split(".")[0].replace(" ", "-") + file_ext
        return os.path.join("Events/", date)

    slug = models.SlugField(max_length=100,db_index=True)
    name = models.CharField(unique=True,max_length=100,db_index=True)
    description = models.TextField(unique=True,max_length=2000)
    event_price = models.PositiveIntegerField()
    picture = models.ImageField(upload_to=get_date_name)
    date = models.DateField(blank=True,null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ("date",)
        verbose_name = "События"
        verbose_name_plural = "События"

class Dish(models.Model):

    def get_date_name(self,filename:str) -> str:
        file_ext="."+filename.strip().split(".")[-1]
        date="Typical_dish"+str(datetime.datetime.now()).split(".")[0].replace(" ","-")+file_ext
        return os.path.join("Dishes/",date)

    slug = models.SlugField(max_length=100,db_index=True)
    name = models.CharField(unique=True,max_length=30,db_index=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.TextField(max_length=100,blank=True)
    ingredient = models.CharField(max_length=300,unique=False)
    position = models.SmallIntegerField()
    in_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=get_date_name)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        index_together = (('id','slug'),)
        verbose_name = "Блюда"
        verbose_name_plural = "Блюда"

class AboutUs(models.Model):
    pozition = models.PositiveIntegerField(unique=True,blank=False)
    title = models.CharField(max_length=100)
    exactly_about_us = models.TextField(max_length = 2000)

    class Meta:
        verbose_name = "Про нас"
        verbose_name_plural = "Про нас"

    def __str__(self):
        return self.title


class Specials(models.Model):

    def get_date_name(self, filename: str) -> str:
        file_ext = "." + filename.strip().split(".")[-1]
        date = "Special" + str(datetime.datetime.now()).split(".")[0].replace(" ", "-") + file_ext
        return os.path.join("Specials/", date)

    title = models.TextField(max_length=500)
    slug = models.SlugField(max_length=100, db_index=True)
    name = models.CharField(unique=True, max_length=30, db_index=True)
    about = models.TextField(max_length=2000)
    picture = models.ImageField(upload_to=get_date_name)
    pozition = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Cпециальные предложения"
        verbose_name_plural = "Cпециальные предложения"

    def __str__(self):
        return self.name

class Galery(models.Model):
    def get_date_name(self,filename:str) -> str:
        file_ext = "." + filename.strip().split(".")[-1]
        date = "RestaurantPhoto" + str(datetime.datetime.now()).split(".")[0].replace(" ", "-") + file_ext
        return os.path.join("Restaurant/", date)

    pozition=models.PositiveIntegerField()
    picture = models.ImageField(upload_to=get_date_name)

    class Meta:
        verbose_name = "Фотографии"
        verbose_name_plural = "Фотографии"

class VideoAboutUs(models.Model):
    def get_date_name(self, filename: str) -> str:
        file_ext = "." + filename.strip().split(".")[-1]
        date = "RestaurantPhoto" + str(datetime.datetime.now()).split(".")[0].replace(" ", "-") + file_ext
        return os.path.join("Preview/", date)
    def video_name(self, filename: str) -> str:
        file_ext = "." + filename.strip().split(".")[-1]
        date = "video" + str(datetime.datetime.now()).split(".")[0].replace(" ", "-") + file_ext
        return os.path.join("Preview/", date)
    text = models.TextField(max_length=2000)
    preview = models.ImageField(upload_to=get_date_name)
    video_link = models.CharField(max_length=200)

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name = "Обзорное видео"
        verbose_name_plural = "Обзорное видео"

class ReservationForm(models.Model):
    mail_re = RegexValidator(regex=r'^[^-|_]\w*[-{0,1}]?\w*?[@]?\w*(.com)?$',message="Invalid mail")
    phone_re = RegexValidator(regex=r'^[+]?\d{8,14}$',message="Invalid phone")
    date_re = RegexValidator(regex=r'^(\d{1,2})([-: .]\d{1,2})?(-\d{4})?$',message="Invalid date")
    time_re = RegexValidator(regex=r'^(\d{1,2})([-: ]\d{1,2})?$', message="Invalid time")
    number_of_people_re = RegexValidator(regex=r'^[1-5][1-9]?$', message="Invalid time")
    name = models.CharField(max_length=70)
    mail = models.CharField(max_length=30,validators=[mail_re])
    phone = models.CharField(max_length=15,validators=[phone_re])
    date = models.CharField(max_length=20,validators=[date_re])
    time = models.CharField(max_length=20,validators=[time_re])
    number_of_people = models.SmallIntegerField(validators=[number_of_people_re])
    text = models.TextField(max_length=500,blank=True)
    is_processed = models.BooleanField(default=False)
    timeadd = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ("-timeadd","-is_processed",)

    def __str__(self):
        return f'{self.name}({self.date})'

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=70)
    text = models.TextField(max_length=500)
    done = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}.{self.text[:20]}'

    class Meta:
        ordering = ("-done",)