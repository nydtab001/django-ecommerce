from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from reviews.models import ProductReview


@receiver(post_save, sender=ProductReview)
@receiver(post_delete, sender=ProductReview)
def update_product_average_rating(sender, instance, **kwargs):
    instance.product.average_rating()
    instance.product.save()
