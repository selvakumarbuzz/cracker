from django.db import models

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

from django.conf import settings
from django.db.models import Q
# Create your models here.

class QuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs
class TemplateManager(models.Manager):
    def get_queryset(self, *args,**kwargs):
        return QuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)
class Template(models.Model):
    template_name = models.CharField(max_length=255)
    objects = TemplateManager()

    def get_absolute_url(self):
        return f"/api/template/{self.pk}/"

    @property
    def endpoint(self):
        return self.get_absolute_url()

    @property
    def path(self):
        return f"/template/{self.pk}/"


class CategoryManager(models.Manager):
    def get_queryset(self, *args,**kwargs):
        return QuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

class Category(models.Model):
    template = models.ForeignKey(Template, default=1, null=True, on_delete=models.SET_NULL)
    category_name = models.CharField(max_length=255)
    objects = CategoryManager()

class BillingManager(models.Manager):
    def get_queryset(self, *args,**kwargs):
        return QuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

class Billing(models.Model):
    template = models.ForeignKey(Template, default=1, null=True, on_delete=models.SET_NULL)
    customer_Name = models.TextField(blank=True, default='')
    customer_Address = models.TextField(blank=True, default='')
    customer_PhoneNumber = models.TextField(blank=True, default='')
    final_Bill_Amount = models.TextField(blank=True, default='')
    customer_Email = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='billing/%Y/%m/', max_length=255, null=True)
    objects = BillingManager()


class ProductManager(models.Manager):
    def get_queryset(self, *args,**kwargs):
        return QuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

class Product(models.Model):
    # pk
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    availability = models.BooleanField(default=True)
    is_offer = models.BooleanField(default=True)
    template = models.ForeignKey(Template, default=1, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='product/%Y/%m/',max_length=255,null=True)
    objects = ProductManager()

    def get_absolute_url(self):
        return f"/api/products/{self.pk}/"

    @property
    def endpoint(self):
        return self.get_absolute_url()

    @property
    def path(self):
        return f"/products/{self.pk}/"



