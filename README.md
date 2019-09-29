# craftbeerpi-MQTTClient

This plugin allows you to send data to an MQTT message broker using a [CraftBeerPi background task](https://github.com/Manuel83/craftbeerpi3/wiki/Custom-Background-Task).

## Installation

```
cd craftbeerpi3/modules/plugins/

git clone https://github.com/jpfranca1977/craftbeerpi-MQTTClient

cd craftbeerpi-MQTTClient
```
In case you miss the eclipse paho library. Install the dependencies using:
```
pip install paho-mqtt
```

## Configuration

Configure host, port, username, passwrd in the ```MQTTClient.py´´´ file.

Configure your MQTT topics and data in the ```__init__.py``` file. 

```

## Testing

In order to test the client in a local environment you'll need an MQTT message broker such as [Mosquitto](https://mosquitto.org/). You can easily install the message broker on your local CraftBeerPi by using the following command. 

```
sudo apt-get install mosquitto mosquitto-clients
```

If you want to subscribe to the published content I recomend the [MQTT.fx](http://www.mqttfx.org/) client.

## Thanks

This plugin was created for my specific needs based on code from 

https://github.com/peakMeissner/cbpi-MQTTClient

and

https://github.com/aravndal/ThingSpeak

Thanks for the original coders!
