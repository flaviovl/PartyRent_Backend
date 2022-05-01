from io import BytesIO

from django.core.files import File
from django.db import models
from django.utils.text import slugify
from PartyRental.settings import BASE_DEBUG_URL as baseURL
from PIL import Image


class Category(models.Model):
    name = models.CharField('nome', max_length=50)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ('id',)

    def __str__(self): 
        return self.name

    @property
    def path_pk(self):
        return f"api/category/{self.pk}/"
    
    @property
    def path_slug(self):
        return f"api/category/{self.slug}/"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='Categoria',
        related_name='products',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    name = models.CharField('nome', max_length=50)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    description = models.TextField('descrição', blank=True)
    price = models.DecimalField('preço', max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images/", default="images/no-image.png", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="thumbnail/", blank=True, null=True)
    in_stock = models.BooleanField('estoque', default=True)
    is_active = models.BooleanField('ativo', default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return f"{self.id}: {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    @property
    def endpoint_pk(self):
        return self.get_absolute_pk_url()
    
    @property
    def endpoint_slug(self):
        return self.get_absolute_slug_url()

    @property
    def path_pk(self):
        return f"api/product/{self.pk}/"
    
    @property
    def path_slug(self):
        return f"api/product/{self.slug}/"

    @property
    def image_url(self):
        return f'{baseURL}{self.image.url}' if self.image else ''
    
    @property
    def thumbnail_url(self):
        return self.get_thumbnail()

    def get_absolute_slug_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_absolute_pk_url(self):
        return f'/{self.category.id}/{self.id}/'

    def get_thumbnail(self):
        if self.thumbnail:
            return f'{baseURL}{self.thumbnail.url}'
        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()

            return f'{baseURL}{self.thumbnail.url}'
        else:
            return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        return File(thumb_io, name=image.name)
