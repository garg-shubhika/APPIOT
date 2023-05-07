import paho.mqtt.client as mqtt
import random
import time

humd_threshold = 20
temp_threshold = 25

client = mqtt.Client(protocol=mqtt.MQTTv31)
client.connect("localhost")

n = 10000
device_ids = ["device_{}".format(i) for i in range(n)]
count = 0
for did in device_ids:
    temp = random.randint(10, 30)
    humd = random.randint(10, 30)

    if random.random() < 0.5 and humd > humd_threshold:
        if random.random() < 0.2 and temp > temp_threshold:
            payload = '{{"id":"{0}","t":{1},"h":{2}}}'.format(did, temp, humd)
            count = count+1
        else:
            payload = '{{"id":"{0}","h":{1}}}'.format(did, humd)
            count = count+1
    elif random.random() < 0.2 and temp > temp_threshold:
        payload = '{{"id":"{0}","t":{1}}}'.format(did, temp)
        count = count+1
    else:
        continue

    client.publish("sensors", payload)
print("Total messages sent: ", count)