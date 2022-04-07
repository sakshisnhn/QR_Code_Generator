# first install the module
# pip install myqr
from MyQR import myqr
# myqr.run("http://bit.ly/hackersrealm",save_name="qrchannel.png")
# myqr.run("https://www.youtube.com/c/CodeWithHarry",save_name="code_with_harry.png")
## to generate the coustomized qr code
# myqr.run(words="http://bit.ly/hackersrealm",picture="testing_harry.jpg",colorized=True,save_name="qrchannelcustomized.png")
myqr.run(words="https://www.linkedin.com/in/sakshi-singh-00b2b71b5/",picture="sakshi_photo.jpg",colorized=True,save_name="qrcodecustomized.png")