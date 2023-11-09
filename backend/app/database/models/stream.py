from tortoise import fields
from tortoise.models import Model


class UploadedVideo(Model):
    """Model of a video that was/is being processed"""
    id = fields.IntField(pk=True)

    # TODO: add more fields here, idk yet which ones exactly

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "uploaded_videos"

class Camera(Model):
    """Camera, that needs to be proccessed"""
    id = fields.IntField(pk=True)
    rtsp_url = fields.CharField(max_length=4096)
    is_active = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "cameras"


