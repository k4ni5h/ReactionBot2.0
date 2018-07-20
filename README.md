# Reaction Bot 2.0
 
 # Abstract:

A Human-Computer Interaction Bot is a Humanoid Bot and the second version of previous year's Reaction Bot. It can gives output/reactions according to the environment and can be used as home automation & Indoor Security. This year we includes a lot of new features in the bot like 3D motion, remove the mobile interference, use cam reaction api and sound source localization, etc.

# Acknowledgement:

We would like to express our special thanks of gratitude to our mentor Nikhil Kumar (EE 3rd year) who gave us the golden opportunity to do this wonderful project  which helped us in doing a lot of research and we came to know about so many new things.

# Motivation:

Humanoid Robotics

Like as a human being it is really very easy for us give a reactions over a thing and give a specific output as over mind is trained on a very large dataset. But as far a machine is concern it is really gonna difficult when you have limited dataset or zero dataset. Then you have the only thing on which you can rely and it is web APIs.

Locate a Sound Source

Localize a sound source is actually not a easy task as you have a lot of noise in sound. So first of all you have to filter your input and also your input should be very precise with time then only you can use any calculation but in real world scenerio it is not so. So it is really very challenging to locate the sound source.

# Hardware:

The mechanical design of the bot includes:
1)	Servo Motor (6 volt)(x3):</p><div><img src="https://raw.githubusercontent.com/marsiitr/Chess-Playing-Bot/master/images/Page-4-Image-3.jpg"></div></li>
 
# Work:

Description of Mechanical Part:

x y z

Description on code is as follows:

Code is basically divided in 3 parts

1. Sound - Kanish
2. Camera - Anant Singh
3. Motion - Anand Kumar

1. Sound part is basically divided into 2 parts. First is to get sentiment/ work according to sound input. For this, we use Google API to process the sound into text. After that, we use google translate API to translate input into English text. Then with the use of 'IBM Watson Tone Analyzer', we got the sentiment. We successfully implement this in file `tone.py` inside `speech` folder. Second is to locate the sound source. So firstly we find the time gap between two sound inputs (its multiplication with sound speed gives the distance gap) and amplitude ratio (amplitude inversely proportional to the distance) can give the exact angle of the sound source with respect to the bot. It is implemented in `code2.py` inside the `speech` folder.

# Future improvements:

1. We can connect this bot with mobile and after that user will be notified if bot found something uncommon thing is happening at your place.

2. There are many issues with the mechanical model like the motor of the neck is not perfectly coupled. Due to which we got a lot of issue during exhibition like it is not localizing the source but neck is not rotating according to that value.

# Team members:

<ul>
<li ><a href="https://github.com/k4ni5h">Kanish</a></li>
<li><a href="https://github.com/anantiitrk">Ankit Singh</a></li>
<li><a href="https://www.facebook.com/rjanand1816">Anand Kumar Singh</a></li>
</ul>

# Mentors:

<ul>
<li><a href="https://github.com/nikhil1198">Nikhil Kumar</a></li>
</ul>

# Special Credit:

<ul>
</ul>

# Thank You!!!!