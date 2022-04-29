from django.db import models
from product.models import Product
from users.models import User


class Review(models.Model):

    client = models.ForeignKey(
        User,
        verbose_name="Cliente",
        related_name="client_reviews",
        on_delete=models.RESTRICT,
    )
    product = models.ForeignKey(
        Product,
        verbose_name="Produto",
        related_name="product_reviews",
        on_delete=models.RESTRICT,
    )
    date = models.DateTimeField("Data", auto_now=True)
    star_rating = models.PositiveIntegerField("Stars", default=5)
    comment = models.TextField("Comentário", max_length=200)

    class Meta:
        verbose_name = ("Comentário")
        verbose_name_plural = ("Comentarios")
        ordering = ["id"]

    def __str__(self):
        return f"Cliente: {self.client.username} - Produto: {self.product.name}"
