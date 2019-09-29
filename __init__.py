#import json
from modules import cbpi
from MQTTClient import MQTTClient

mqttc = MQTTClient().connect()                                            # initialize the MQTT client

@cbpi.backgroundtask(key='mqtt_client', interval=5)                       # create bg job with an interval of 5 seconds 

def mqtt_client_background_task(api):

    for key, value in cbpi.cache.get('sensors').iteritems():              # loop over the sensors
        topic = 'craftbeerpi/sensor/' + str(value.instance.name)          # define the MQTT topic
	payload = value.instance.last_value
        mqttc.publish(topic, payload)                                     # connect to the MQTT server and publish the payload

    for count, (key, value) in enumerate(cbpi.cache["kettle"].iteritems(), 1):
        if value.target_temp is not None:
            topic = 'craftbeerpi/target/' + str(value.name)
            payload = value.target_temp
            mqttc.publish(topic, payload)                                 # connect to the MQTT server and publish the payload

    for count, (key, value) in enumerate(cbpi.cache["fermenter"].iteritems(), 1):
        if value.target_temp is not None:
            topic = 'craftbeerpi/target/' + str(value.name)
            payload = value.target_temp
            mqttc.publish(topic, payload)                                 # connect to the MQTT server and publish the payload

    for count, (key, value) in enumerate(cbpi.cache["actors"].iteritems(), 1):
        if value.state is not None:
            topic = 'craftbeerpi/actor/' + str(value.name)
            payload = value.state
            mqttc.publish(topic, payload)                                 # connect to the MQTT server and publish the payload

