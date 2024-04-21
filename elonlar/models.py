from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Kategoriya")

    def __str__(self):
        return f"Kategoriya: {self.name}"

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ['name']


class Avtomobillar(models.Model):
    name = models.CharField(max_length=255, verbose_name="Avtomobil nomi")
    content = models.TextField(verbose_name="Avtomobil haqida to'liq ma'lumot")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    photo = models.ImageField(verbose_name="Rasmi", upload_to='photos/', null=True, blank=True)
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarish")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Avtomobil'
        verbose_name_plural = 'Avtomobillar'
        ordering = ['-created', 'name']




class Profile(models.Model):
    full_name = models.OneToOneField(User,verbose_name="To'liq ism", on_delete=models.CASCADE)
    email = models.CharField(max_length=25,blank=True,verbose_name="\Email manzil")
    phone = models.CharField(max_length=13,verbose_name="Telefon raqam")
    photo = models.ImageField(upload_to='profile_pictures/', blank=True,verbose_name="Rasmi")
    mobile = models.CharField(max_length=13,verbose_name='Telefon raqam1')
    addres = models.CharField(max_length=50,verbose_name="Manzil")


    def __str__(self):
        return self.full_name.username


