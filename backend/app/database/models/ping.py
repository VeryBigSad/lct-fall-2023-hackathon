from tortoise import fields
from tortoise.models import Model


class Ping(Model):
    id = fields.IntField(pk=True)

    url = fields.CharField(max_length=4096)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "pings"
