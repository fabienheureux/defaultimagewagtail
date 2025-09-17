from wagtail.blocks import StreamBlock
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageBlock
from wagtail.images.widgets import get_image_model
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from django.db.utils import OperationalError


def get_image():
    try:
        return {"image": get_image_model().objects.first(), "decorative": True}
    except (get_image_model().DoesNotExist, OperationalError):
        # OperationnalError ensure this won't crash when running makemigrations with
        # an empty db, in CI for example.
        return


class StoryBlock(StreamBlock):
    image = ImageBlock(default=get_image())


class HomePage(Page):
    body = StreamField(StoryBlock())
    content_panels = Page.content_panels + [FieldPanel("body")]
