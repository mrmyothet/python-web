class Telephone:
    def dial_phone(self):
        print("dialing the phone")

class Camera:
    def take_photo(self):
        print("taking photo")

class SmartPhone(Telephone, Camera):
    def surf_web(self):
        print("surfing the web")

my_phone = SmartPhone()
my_phone.dial_phone()
my_phone.take_photo()
my_phone.surf_web()