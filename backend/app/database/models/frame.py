from tortoise import fields
from tortoise.models import Model


class Frame(Model):
    """Model for frame, when you want to specify there is or whether there is not a weapon there"""

    id = fields.IntField(pk=True)
    image_url = fields.CharField(max_length=4096)
    box_top_left_x = fields.IntField(null=True)
    box_top_left_y = fields.IntField(null=True)
    box_bottom_right_x = fields.IntField(null=True)
    box_bottom_right_y = fields.IntField(null=True)
    has_weapon = fields.BooleanField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "frames"
