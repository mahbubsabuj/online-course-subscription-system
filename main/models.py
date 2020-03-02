from django.db import models
from django.conf import settings
from django.shortcuts import reverse

category = (
    ('PY','Python'),
    ('CPP','C++'),
    ('JS','Javascript')
)
label = (
    ('P','primary'),
    ('S','secondary'),
    ('D','danger')
)
class Item(models.Model):
    title = models.CharField(max_length = 200)
    price = models.FloatField()
    category = models.CharField(choices = category,max_length = 5)
    label = models.CharField(choices = label,max_length = 1)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('main:product',kwargs = {'slug' : self.slug})
    def get_add_to_cart(self):
        return reverse('main:add-to-cart',kwargs = {'slug' : self.slug})



class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    ordered = models.BooleanField(default = False)
    item = models.ForeignKey(Item,on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.item.title}'   



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderItem) 
    start_date = models.DateTimeField(auto_now = True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default = False)
    def __str__(self):
        return self.user.username
