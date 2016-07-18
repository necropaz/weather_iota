# weather_iota - Python package

The IOTA Weather Node is a Weather Node built with a [Raspberry Pi](https://www.raspberrypi.org/) and the add-on board  [Sense HAT](https://www.raspberrypi.org/products/sense-hat/).
The Weather Node send and receive Data over the new [IOTA Protocol](https://www.iotatoken.com/).

## What I need to run an weather_iota instance?

required:
- [ ] Install the latest IOTA release from : [IOTA Node](https://github.com/IOTAledger/iota-gui-beta/releases)
- [ ] Install the latest iota python package [iota](https://github.com/necropaz/iota)
- [ ] the python package sys, json, urllib2 and os are also required

for more fun:
- [ ] [Raspberry Pi](https://www.raspberrypi.org/)
- [ ] microSD card with installed [Ubuntu MATE 16.04 LTS](https://ubuntu-mate.org/download/)
- [ ] Raspberry Pi [Sense HAT](https://www.raspberrypi.org/products/sense-hat/)
- [ ] Sense HAT python [package](https://pypi.python.org/pypi/sense-hat)


## Installation
If you already have installed pip then you can skip this point and can directly install the package with pip.
```ShellSession
$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv
```

To install the package it is very easy if you have installed pip.

```ShellSession
$ sudo pip install -i https://testpypi.python.org/pypi iota
$ sudo pip install -i https://testpypi.python.org/pypi weather_iota
```

## Weathernode
The IOTA Weather Node waiting until a client send a transaction with >0 IOTAs and a message.
With the message the client tell the node what is his request and an address on which the node can send his answer.
So can be send a command is arrived over the IOTA Protocol.
After this he read the Weather info from the Sense HAT and send them back or just show a promotion on his 8x8 LED Matrix.

### Running an instance
- First you have to import the package 
```Python
from weather_iota import weathernode
```

- Now you can run an instance very easy
```Python
node=weathernode("HIERCOMESMYSEED", temperature=100, humidity= 54, pressure=1024, senseHAT=false)
node.run()
```

### Testing node
You can run this script to test the weather node:
```Python
import sys
import json
import time
import os
from weather_iota import weathernode

seed=raw_input("Enter the seed of the IOTA Weather Node? ")

weather=weathernode(seed, temperature="32",humidity="50",pressure="1013", senseHAT=False)
weather.run()
print("End Iota Weather Node!")
```

### Weathernode class

#### `weathernode( seed, temperature=None, humidity=None, pressure=None, senseHAT=True)`

Make a instance of the iota weathernode.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`input` |`temperature` | string | No | You can input here a temperature for simulation. Default it is None.
`input` |`humidity` | string | No | You can input here a humidity for simulation. Default it is None.
`input` |`pressure` | string | No | You can input here a pressure for simulation. Default it is None.
`input` |`senseHAT` | bool | No | If you will simulate the SenseHAT you have to type senseHAT=False. Default it is True.
`return` |`ErrorMessage` | string | Yes | Will give you back an error message if it fails.

#### `run()`

Run the instance. Wait until a request is recived and is confirmed 100%.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`return` |`ErrorMessage` | string | Yes | Will give you back an error message if it fails.

#### `execute(jsonData)`

Execute the recived command.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`jsonData` | string | Yes | The message which is recived in json format.
`return` |`ErrorMessage` | string | Yes | Will give you back an error message if it fails.

#### `readWeather()`
Read the weather data out of the raspberry pi.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`return` |`weatherinfo` | string | Yes | The weather infos a string which are readed from the Sense HAT.

#### `scrollText(message)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`message` | string | Yes | The promotion text which the client send you.
`return` |`ErrorMessage` | string | Yes | Will give you back an error message if it fails.

## Weather client


### Running an instance
- First you have to import the package 
```Python
from weather_iota import weatherclient
```

- Now you can run an instance very easy
```Python
client=weatherclient("HIERCOMESMYSEED", "THEADDRESSOFTHEIOTAWEATHERNODE")
client.requestWeather()
client.sendPromotion("Here comes my promotion!")
```
### Testing client
You can run this script to test the weather client. There is a test instance running on a VPS Server you can use this address: DCSFTNCWDPUMJJQHIEL9VJVOIHMVLFEYQTEYNYOWHVUQ9PZWOXKZEXSUSWUQOLMSHFANN9PTCBTLUVLZIYOFOCLZJF
```Python
import sys
import json
import time
import os
from weather_iota import weatherclient

address=raw_input("The address of the Weather Node? ")
seed=raw_input("The seed of you Weather Client? ")
char=raw_input("If you will send a weather request tip w, if you wanna send a promotion tip p.? [w/p]? ")

client=weatherclient(seed, address)

if char=='w':
	client.requestWeather()

elif char=='p':
	message=raw_input("What for a promotion you wanna send? ")
	client.sendPromotion(message)

else:
	print("Your Input is not [r/p]")
```

### Weatherclient class

#### `weatherclient( seed, address)`

Make a instance of the iota weatherclient.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`input` |`address` | string | Yes | The address from the weather node.
`return` |`ErrorMessage` | string | Yes | Will give you back an error message if it fails.

#### `requestWeather()`

Send a weather request to the node and wait on the answer.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`return` |`weatherinfos` | string | Yes | The weather infos which are recived from the weather node.

#### `sendPromotion(promotion)`

Send a promotion to the weather node.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`promotion` | string | Yes | The promotion text which you wanna send.
`return` |`ErrorMessage` | string | Yes | Will give you back an error message if it fails.


