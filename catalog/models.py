from django.db import models

# Create your models here.
Status_list = (
        ('Y', 'Yes'),
        ('N', 'No')
    )

class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(help_text='Enter category name', max_length=25)
    display_name = models.CharField(help_text='Enter the category display name', max_length=25)
    active = models.CharField(help_text='Enter category status', choices=Status_list, default='Y', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')


class Subcategorie(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    name = models.CharField(help_text='Enter subcategory name', max_length=25)
    display_name = models.CharField(help_text='Enter the subcategory display name', max_length=25)
    active = models.CharField('Enter subcategory status', choices=Status_list, default='Y', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey('Subcategorie', on_delete=models.CASCADE)
    name = models.CharField(help_text='Enter product name', max_length=25)
    display_name = models.CharField(help_text='Enter the product display name', max_length=25)
    short_desciption = models.TextField(help_text='Enter short description(max=255)', max_length=255)
    full_description = models.TextField(help_text='Enter full description(max=1000)', max_length=1000)
    price = models.IntegerField(help_text='Enter product price')
    stock = models.IntegerField(help_text="Enter Stock")
    active = models.CharField(help_text='Enter product status', choices=Status_list, default='Y', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name