# ESP32 "live" camera

## Motivation

I want a camera that gives me a live feed of images from a surf point that's a good 30-minute car journey from where I live. Internet connections aren't all that reliable on a beach setting - at least not in Brazil. Moreover (and this is the real kicker, because this is what has kept me from installing the camera with the camera-as-server architecture), for some reason the ISP in the hotel I'm trying to install the camera in doesn't allow - not without expressed consent by the contractor, who isn't really well-versed in why exactly they have to do this, which makes me a bit uncomfortable to ask as this would make me a bit too dependent on them - port forwarding, which makes it impossible for me to access the camera at all through the internet. 

Given that the camera-as-server architecture is what allows me to transmit video live, plus the fact that I'm not sure I could even do an ok job of live transmission in the first place - because of hardware limitations in the ESP32, plus network speeds, the impacts of which I haven't even had the chance of evaluating regarding the performance of the system with packet loss - and the fact that I'd have to be a bit too uncomfortable around people I'm not really familiar with, I'm lead to the conclusion that this is too much of a hassle.

The thing is that, the end-result - a functioning system that gives me live visual information on my surf spot - is so useful that I can't simply give up on this. After a month or two without really working on it, but continually frustrated by seeing the camera sitting idle, I came up with a different approach today - which isn't particularly complicated or hard, it's actually simpler. I know why I haven't pursued this earlier (at least not after I understood the regular workflow of broadcasting video): no stable live video. 

The solution is a camera-as-client architecture, which bypasses the need for port forwading and makes things simpler overall.

## General architecture
On the camera side, its main loop consists of polling a web server in regular intervals (maybe constantly). There are 2 states possible '1' meaning take a picture and send it to the server and '0' meaning do nothing.

On the web server side there'll be 2 routes (or maybe 1 that accepts 'GET' and 'POST'). One route is the route that sends the current state the camera should be in. The other is the route that receives an image through regular HTTP and processes it.

This is it.

## Lower level plan

## TODO:
* Hard-code the wifi ssid and password such that there's no need to set the camera up if it turns off - say for its power source going out.

* Change rtsp code to the http routine I described


