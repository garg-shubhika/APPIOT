import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
                print("Payload:", msg.payload())
client = mqtt.Client()
client.connect("localhost",1883,60)
client.subscribe("sensors")
client.on_message=on_message
client.loop_forever() 