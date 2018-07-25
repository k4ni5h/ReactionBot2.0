# Reaction Bot 2.0

 # Abstract:

A Human-Computer Interaction Bot is a Humanoid Bot and the second version of previous year's Reaction Bot. It can give output/reactions according to the environment and can be used as friendly pet and extended for home automation & Indoor Security.  It can read facial emotion of the person and can do actions based on that.This year we updated a lot of new features in the bot like 3D motion for its face, removed the mobile interference, used cam reaction api and sound source localization, etc.

# Acknowledgement:

We would like to express our special thanks of gratitude to our mentor Mr. Nikhil Kumar (ECE 3rd year) who gave us the golden opportunity to do this wonderful project  which helped us in doing a lot of research and we came to know about so many new things.

# Motivation:

Humanoid Robotics

Like as a human being it is really very easy for us give a reactions over a thing and give a specific output as over mind is trained on a very large dataset. But as far a machine is concern it is really gonna difficult when you have limited dataset or zero dataset. Then you have the only thing on which you can rely and it is web APIs.

Locate a Sound Source

Localize a sound source is actually not a easy task as you have a lot of noise in sound. So first of all you have to filter your input and also your input should be very precise with time then only you can use any calculation but in real world scenerio it is not so. So it is really very challenging to locate the sound source.

# Hardware:

The mechanical design of the bot includes:

1)	Stepper  Motor (12 volt)(2):</p><div><img src="https://raw.githubusercontent.com/marsiitr/Chess-Playing-Bot/master/images/Page-3-Image-2.jpg"></div></li>
2)	Servo Motor (6 volt)(3):</p><div><img src="https://raw.githubusercontent.com/marsiitr/Chess-Playing-Bot/master/images/Page-4-Image-3.jpg"></div></li>
3)	Raspberry Pi 3(1):</p><div><img src="https://www.raspberrypi.org/app/themes/mind-control/images/home-products-cta__image.png"></div></li>
4)	Logic Level Converter:</p><div><img src="https://cdn.sparkfun.com//assets/parts/8/5/2/2/12009-07.jpg"></div></li>
5)	L298 Motor Drivers(1):</p><div><img src="https://raw.githubusercontent.com/marsiitr/Chess-Playing-Bot/master/images/Page-5-Image-6.jpg"></div></li>
6)	Gears:</p><div><img src="https://raw.githubusercontent.com/marsiitr/Chess-Playing-Bot/master/images/Page-5-Image-7.jpg"></div></li>
7)	Combination of LM317 and potentiometer  for voltage regulation:</p><div><img src="https://raw.githubusercontent.com/marsiitr/Chess-Playing-Bot/master/images/Page-6-Image-8.jpg"></div></li>
 8) Castor Wheels(3):</p><div><img src="https://raw.githubusercontent.com/marsiitr/Chess-Playing-Bot/master/images/Page-6-Image-9.jpg"></div></li>


# Work:

Description of Mechanical Part:

The face of the bot is build by 3D printer and other parts are made of plyboard, rod.

Description on code is as follows:

Code is basically divided in 3 parts

1. Sound - Kanish
2. Camera - Anant Singh
3. Motion - Anand Kumar

Explanation

1. Sound part is basically divided into 2 parts. First is to get sentiment/ work according to sound input. For this, we use Google API to process the sound into text. After that, we use google translate API to translate input into English text. Then with the use of 'IBM Watson Tone Analyzer', we got the sentiment. We successfully implement this in file `tone.py` inside `speech` folder. Second is to locate the sound source. So firstly we find the time gap between two sound inputs (its multiplication with sound speed gives the distance gap) and amplitude ratio (amplitude inversely proportional to the distance) can give the exact angle of the sound source with respect to the bot. It is implemented in `code2.py` inside the `speech` folder.

2. camera - The camera used in the bot is picam and it takes pictures of the person which is sent to the Sightcorp face api to get its emotion.

3. Motion - The face and the body of bot moves as per the environment. The face uses 3 Servo Motors to show reaction of bot and it uses 2 stepper motors to walk.

# Future improvements:

1. We can connect this bot with mobile and after that user will be notified if bot found something uncommon thing is happening at your place.

2. There are many issues with the mechanical model like the motor of the neck is not perfectly coupled. Due to which we got a lot of issue during exhibition like it is not localizing the source but neck is not rotating according to that value.

3. The bot can be used as a music player,to do home automation and indoor security as it can make ,take video/pictures , understand environment and act accordingly.

# Team members:

<ul>
<li ><a href="https://github.com/k4ni5h">Kanish</a></li>
<li><a href="https://github.com/anantiitrk">Anant Singh</a></li>
<li><a href="https://github.com/rjanand1816">Anand Kumar</a></li>
<li><a href="https://facebook.com/mayur.naik.58511">Naik Mayur Ravidas</a></li>
<li><a href="https://facebook.com/vikashkumar.meel">Vikash Choudhary</a></li>
</ul>

# Mentors:

<ul>
<li><a href="https://github.com/nikhil1198">Nikhil Kumar</a></li>
<li><a href="https://github.com/palnabarun">Nabarun Pal</a></li>
</ul>

# Special Credit:

<ul>
<li><a href="https://www.facebook.com/Shivamsrivastava1912">Shivam Srivastava</a></li>
[Models And Robotics Section Secretary 2017-2018.]
</ul>

# Thank You!!!!
