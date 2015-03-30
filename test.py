__author__ = 'waen'

import qrcode
from imagemagick import WandImage

img = qrcode.make('http://www.epub360.com', image_factory=WandImage)
img.save('test.png')