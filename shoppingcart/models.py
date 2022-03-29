from django.db import models
from users.models import User
from product.models import Product


class ShoppingCart(models.Model):
    client = models.ForeignKey(User, verbose_name='Cliente', on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField('Pedido', default=False)
    date_ordered = models.DateTimeField('Data', auto_now=True)

    class Meta:
        verbose_name_plural = "Carts"


class CartItem(models.Model):
    product_id = models.ForeignKey(Product, verbose_name='Produto', on_delete=models.SET_NULL, null=True)
    cart_id = models.ForeignKey(ShoppingCart, verbose_name='Carinho de Compras', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField('Quantidade', null=True, default=0)
    create_date = models.DateTimeField('Data', auto_now_add=True)

    class Meta:
        verbose_name_plural = "Order Itens"


class RentalOrder(models.Model):
    client = models.ForeignKey(User, verbose_name='Cliente', on_delete=models.CASCADE)
    cart_id = models.ForeignKey(ShoppingCart, verbose_name='Carinho de Compras', on_delete=models.SET_NULL, null=True)
    rental_date = models.DateTimeField('Data Locação', auto_now_add=True, auto_now=False)
    return_date = models.DateTimeField('Data Retorno', auto_now_add=True, auto_now=False)
    amount = models.DecimalField('Total', max_digits=100, decimal_places=2)
    id_paid = models.BooleanField('Pago', default=False)

    class Meta:
        verbose_name_plural = "Rental Order"

    def __str__(self):
        return self.cart_id

