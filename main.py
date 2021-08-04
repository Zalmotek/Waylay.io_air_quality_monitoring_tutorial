from m5stack import *
from m5ui import *
from uiflow import *
import urequests
import module

import wifiCfg
import time
import json


setScreenColor(0xffffff)


status = None
PM1 = None
PM2_5 = None
json_data = None
PM10 = None
DataMap = None

pm0 = module.get(module.PM25)
wifiCfg.autoConnect(lcdShow=True)
wifiCfg.reconnect()
pm1 = M5TextBox(33, 120, "Text", lcd.FONT_DejaVu24, 0x2596be, rotate=0)
pm2 = M5TextBox(140, 120, "Text", lcd.FONT_DejaVu24, 0x2596be, rotate=0)
pm10 = M5TextBox(251, 120, "Text", lcd.FONT_DejaVu24, 0x2596be, rotate=0)
image0 = M5Img(110, 201, "res/waylay.png", True)
image1 = M5Img(240, 41, "res/dust_light.png", True)
image2 = M5Img(128, 41, "res/co2_cloud.png", True)
image3 = M5Img(16, 41, "res/dust.png", True)
label0 = M5TextBox(36, 149, "PM1", lcd.FONT_Default, 0x2596be, rotate=0)
label1 = M5TextBox(137, 149, "PM2.5", lcd.FONT_Default, 0x2596be, rotate=0)
HttpStatus = M5TextBox(263, 209, "Status", lcd.FONT_Default, 0x2596be, rotate=0)
label2 = M5TextBox(251, 149, "PM10", lcd.FONT_Default, 0x2596be, rotate=0)
ps = M5TextBox(9, 209, "Waiting", lcd.FONT_Default, 0x2596be, rotate=0)


# Describe this function...
def SendPOST():
  global status, PM1, PM2_5, json_data, PM10, DataMap
  status = 'No StatusCode'
  try:
    req = urequests.request(method='POST', url='Replace_With_Your_Webscript_Address',data=json_data, headers={'Content-Type':'application/json'})
    ps.setColor(0x006600)
    wait(5)
    status = req.status_code
    ps.setText('Data Sent')
  except:
    wait(5)
    status = req.status_code
    ps.setText('Not Sent')
  wait(5)
  HttpStatus.setText(str(status))

# Describe this function...
def GetEnviro():
  global status, PM1, PM2_5, json_data, PM10, DataMap
  PM1 = pm0.get_pm1_0_factory()
  PM2_5 = pm0.get_pm2_5_factory()
  PM10 = pm0.get_pm10_factory()
  DataMap = {'PM1':PM1,'PM2.5':PM2_5,'PM10':PM10}
  json_data = json.dumps(DataMap)
  pm1.setText(str(PM1))
  pm2.setText(str(PM2_5))
  pm10.setText(str(PM10))



image0.show()
import custom.urequests as urequests
while True:
  if wifiCfg.wlan_sta.isconnected():
    GetEnviro()
    SendPOST()
    wait(10)
  else:
    wait(1)
    lcd.print('reconnecting', 0, 30, 0x33ff33)
    wait(1)
lcd.clear()

