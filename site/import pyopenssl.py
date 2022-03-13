import pyopenssl
import base64
from encodings import utf_8
ween = "Hello world"
nogger = base64.b64encode(ween.encode('utf-8'))
print(nogger)
