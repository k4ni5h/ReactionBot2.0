# Mino-The-Friendly-Pet-Bot

Mino is a friendly pet bot for home automation that responds to you via facial emotions! 

# Abstract:

Mino is a friendly pet robot for indoor home automation and security. The most salient feature of Mino is its facial emotional response. The idea is to implement IOT at home. Smart interaction between Mino and the appliances at home to make the living comfortable and smooth.

# Pre-Requisites:

Hardware:

•	Raspberry Pi
•	ESP8266 wifi module
•	2 Servo motors
•	2 DC motors
•	Motor Driver
•	LEDs
•	Speaker
•	Jumper Wires
•	Voltage Regulators 
•	Potentiometer

Software:

•	Android Studio
•	Raspbian OS
•	Arduino 
•	Python with Watson Developer Cloud, Pygame, Bottle libraries

# Usage:

First of all you need a Watson Developer Cloud account and key to access the Alchemy API that provides us with the emotional response for any kind of sentences. The <b>testAL.py</b> file is the python script which is used as a python function to send sentences to the Alchemy API online and get values of 5 types of emotions : Happy, Sad, Angry, Fear and Disgust. The maximum value amongst these values is considered as the emotion of the sentence.

Then a bottle server is to be created on the wifi hotspot or router being used by the Raspberry Pi. The file <b>finalserver.py</b> is used for this purpose. It creates a bottle server to accept string from the Android Application. The string is sent to testAL.py file for getting the emotional response.
In this file we have other features for the bot to play music, respond to junk texts, respond to hello and bye, go to sleep, turn on or off lights and stop any music being played.

Once we get the emotional response we turn the servo motors in its face so as to create an emotion. The pyhton file called for this purpose is <b>funservo1.py</b>. Every emotion has a set angle of rotation for the motors of face and eyelid as shown in the video. Along with visual representation of emotions on the face, Mino also produces sounds according to the emotion which is played using the ppygame library in <b>audio.py</b>.

We can also move the bot in any direction. For this purpose <b>dc_motor.py</b> is used.

In the Android Application we have used http get request to send the input string to the Raspberry Pi. We can talk to the bot via both speech and text. The app can also be used to move the bot in all directions and tell it to go to sleep. 

We can instruct the bot to turn on or off the LED lights in a box that we have made in order to show home automation through the app as shown in the demonstration video. For this we need an ESP8266 module which gets the instruction to turn the lights on or off through wifi. All the lights can be switched off at once by waving your hands 3 time in front of the phone screnn while the app is on. This saves the time of switching off all the lights one by one.


# Applications, Results and Future Scope:

Refer to the link : <b>https://drive.google.com/drive/folders/0B_IBddZ5YQPSM1Bzb3Bwb21tNHM</b>
