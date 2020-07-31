# Instructions from Raspberry Pi Foundation Below Line

## UML Class Diagram: https://app.lucidchart.com/documents/edit/9139b485-20e8-424b-907a-794a6da237ff

Design Pattern: Observer

 * Publisher: Data from Environmental Sensor
 * Subscriber(s): Git Pages, Alexa Interface

	- read_all() function returns measurements taken
	- driver contains read_all(), initializes Publisher Object w/ the returned items from read_all function

__________________________________________________________________________________________


# Raspberry Pi Oracle Weather Station

## Installation

Follow the guides and tutorials at [https://github.com/raspberrypilearning/weather\_station\_guide](https://github.com/raspberrypilearning/weather_station_guide) (published at [www.raspberrypi.org/weather-station](https://www.raspberrypi.org/weather-station/))

## Version

This repo contains the updated version of the software, re-engineered for the [Stretch version of Raspbian](https://www.raspberrypi.org/blog/raspbian-stretch/). If you are an existing Weather Station owner and are using a Pi running the Jessie version of Raspbian, then this code will not work without modification. You should flash your SD card with the [latest Raspbian image](https://www.raspberrypi.org/downloads/raspbian/) and perform a fresh install of this software (you may wish to take a copy of your local MYSQL database first).

----------
