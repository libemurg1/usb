# import usb library PyUSB
import os
import usb.core as usb

def read8(dev,length=4):
    dev.set_configuration()
    data=dev.read(1,length)
    print("Data Read : ",str(data))

print(" Scanning USB Device \n")
devices=usb.find(find_all=True,custom_match = lambda d : d.idVendor==0x0e8d and d.idProduct==0x2000)
#devices=usb.find(find_all=True)
device_count=0
dev=None
if devices:
    for device in devices:
        device_count+=1
        if device is not None:
            print("============================DEVICE================================\n\a")
            print(str(device))
            print("=============================END==================================\n")
        # print("{} devices Found\n".format(device_count))
        read8(device)
    #os.system("clear")
else:
    print("No Device Found")

