import qrcode

from qrcode.constants import ERROR_CORRECT_H
from src.config import FILL_COLOR, BACK_COLOR

def create_custom_qr(data: str, size: int, border: int) -> qrcode.image.base.BaseImage:
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=size,
        border=border
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)
    return img

