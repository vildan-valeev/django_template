from django.db.models.signals import post_save
from django.dispatch import receiver


from shop.models import Item
from shop.tasks import create_item_task


@receiver(post_save, sender=Item)
def item_signal(sender, instance: Item, created, **kwargs):
    if kwargs.get('raw', False):  # disable signal, when create model from command "manage.py loaddata", because will be errors
        return False

    # your code here
    if created:
        print('Signal')
        # create_item_task.send(instance.id)
    return True
