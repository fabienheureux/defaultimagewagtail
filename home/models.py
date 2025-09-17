from wagtail.blocks import StreamBlock
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageBlock
from wagtail.images.widgets import get_image_model
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from django.db.utils import OperationalError
from wagtail import blocks


def get_image():
    try:
        return {
            "machin": {"image": get_image_model().objects.first(), "decorative": True},
            "youpi": "coucou",
        }
    except get_image_model().DoesNotExist:
        return


class MachinBlock(blocks.StructBlock):
    machin = ImageBlock()
    youpi = blocks.CharBlock()


class StoryBlock(StreamBlock):
    image = MachinBlock(default=get_image)


class HomePage(Page):
    body = StreamField(StoryBlock())
    content_panels = Page.content_panels + [FieldPanel("body")]
