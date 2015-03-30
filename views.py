from django.http import HttpResponse


import qrcode
from imagemagick import WandImage
from django.utils.http import urlunquote


def generate_qrcode(request, data):
    if not data:
        data = 'http://www.epub360.com'
    data = urlunquote(data)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=5,
        border=0,
    )

    qr.add_data(data)

    qr.make(fit=True)
    img = qr.make_image(image_factory=WandImage)
    # img = qrcode.make(data, image_factory=WandImage)
    return HttpResponse(img._img.make_blob(format='png'), mimetype="image/png")





__author__ = 'waen'