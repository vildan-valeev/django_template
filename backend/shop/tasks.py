import logging
import dramatiq

from shop.models import Item

log = logging.getLogger(__name__)


@dramatiq.actor
def create_item_task(instance: int):
    print(f'NEW ITEM id={instance} CREATED!! I doing another work!!!!')


