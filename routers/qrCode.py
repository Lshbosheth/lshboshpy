from fastapi import APIRouter
from pydantic import BaseModel
import qrcode
import base64
from io import BytesIO


router = APIRouter(
    prefix="/qrCode",
    tags=["qrCode"],
    responses={404: {"description": "Not found"}},
)


class Item(BaseModel):
    text: str


@router.post("")
async def img(item: Item):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(item.text)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    img_buffer = BytesIO()
    image.save(img_buffer)
    encoded_string = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    img_buffer.close()
    return {
        "text": 'data:image/png;base64,' + encoded_string
    }
