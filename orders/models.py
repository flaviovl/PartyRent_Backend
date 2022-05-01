from django.db import models
from shoppingcart.models import ShoppingCart
from users.models import User


class RentalOrder(models.Model):
    class StatusRentalOrder(models.IntegerChoices):
        PAY = 1, "Pago"
        DELIVERD = 2, "Entregue"
        RETURNED = 3, "Devolvido"
        CANCELED = 4, "Cancelado"
        REFUNDED_PAY = 5, "Reembolsado"
        
    client = models.ForeignKey(
        User,
        verbose_name="Cliente",
        related_name="client_orders",
        on_delete=models.PROTECT,
    )
    cart = models.ForeignKey(
        ShoppingCart,
        verbose_name="Carinho de Compras",
        related_name="shoppingcart_orders",
        on_delete=models.PROTECT,
    )
    rental_date = models.DateTimeField("Data Locação", auto_now=False, auto_now_add=False, blank=False, null=False)
    return_date = models.DateTimeField("Data Retorno", auto_now=False, auto_now_add=False, blank=False, null=False)
    amount = models.DecimalField("Total", max_digits=100, decimal_places=2)
    status = models.IntegerField("Status", choices=StatusRentalOrder.choices, default=StatusRentalOrder.PAY)

    class Meta:
        verbose_name_plural = "Pedidos de Locação"

    def __str__(self):
        return f"{self.id}"


# class Payment(models.Model):
#     order = models.ForeignKey(
#         RentalOrder,
#         verbose_name="Pedido",
#         related_name="rentalorder_payments",
#         on_delete=models.PROTECT
#     )
#     client = models.ForeignKey(
#         User,
#         verbose_name="Cliente",
#         related_name="client_orders",
#         on_delete=models.PROTECT,
#     )
#     amount = models.FloatField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.client.email


# class Refund(models.Model):
#     order = models.ForeignKey(
#         RentalOrder,
#         verbose_name="Reembolso",
#         related_name="rentalorder_refunds",
#         on_delete=models.PROTECT
#     )
#     reason = models.TextField()
#     accepted = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.pk}"














    #     def get_absolute_url(self):
    #         # return f'/articles/{self.slug}/'
    #         return reverse("articles:detail", kwargs={"slug": self.slug})

    #     def save(self, *args, **kwargs):
    #         # obj = Article.objects.get(id=1)
    #         # set something
    #         # if self.slug is None:
    #         #     self.slug = slugify(self.title)
    #         # if self.slug is None:
    #         #     slugify_instance_title(self, save=False)
    #         super().save(*args, **kwargs)
    #         # obj.save()
    #         # do another something


    # def article_pre_save(sender, instance, *args, **kwargs):
    #     # print('pre_save')
    #     if instance.slug is None:
    #         slugify_instance_title(instance, save=False)

    # pre_save.connect(article_pre_save, sender=Article)


    # def article_post_save(sender, instance, created, *args, **kwargs):
    #     # print('post_save')
    #     if created:
    #         slugify_instance_title(instance, save=True)

# post_save.connect(article_post_save, sender=Article)

