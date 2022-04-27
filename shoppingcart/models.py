from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from product.models import Product
from users.models import User


class ShoppingCart(models.Model):
    class StatusShoppingCart(models.IntegerChoices):
        PENDING = 1, "Carrinho de Compras"
        CONFIMED = 2, "Orçamento Confirmado"
        ORDER = 3, "Ordem de Serviço"
        CANCELED = 7, "Cancelado"
    
    client = models.ForeignKey(
        User,
        verbose_name="Cliente",
        related_name="client_shoppingcarts",
        on_delete=models.RESTRICT
    )
    status = models.IntegerField(
        verbose_name="Status",
        choices=StatusShoppingCart.choices,
        default=StatusShoppingCart.PENDING)
    date_created = models.DateTimeField("Data", auto_now=True)

    class Meta:
        verbose_name_plural = "Carrinhos de compras"
        verbose_name = "Carrinho de compra"

    @property 
    def amount(self):
        qs = self.products.all()
        return sum(product.sub_total for product in qs)
        
        # usando funções django
        # qs = self.products.all().aggregate(total=models.Sum(F("quantity") * F("price")) )                     
        # return qs["total"]

    def __str__(self):
        return f"{self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey(
        ShoppingCart,
        verbose_name="carinho de compras",
        related_name="products",
        on_delete=models.SET_NULL, null=True
    )
    product = models.ForeignKey(
        Product,
        verbose_name="produto",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField("quantidade", null=True, default=0)
    create_date = models.DateTimeField("data", auto_now_add=True)

    class Meta:
        verbose_name_plural = "itens do carrinho"
        ordering = ("pk",)
    
    def __str__(self):
        return f"{self.id}"
    
    @property
    def sub_total(self):
        return self.price * self.quantity
