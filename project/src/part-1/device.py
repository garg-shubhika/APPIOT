import paho.mqtt.client as mqtt
import random
import time

client=mqtt.Client(protocol=mqtt.MQTTv31)
client.connect("localhost")

n = 10000
device_ids = ["device_{}".format(i) for i in range(n)]
while True:
	for did in device_ids:
          	temp = random.randint(10,30)
          	humd = random.randint(10,30)
          	payload = '{{"id":{0},"t":{1},"h":{2}}}'.format(did,temp,humd)
          	client.publish("sensors", payload)
        time.sleep(12*3600)