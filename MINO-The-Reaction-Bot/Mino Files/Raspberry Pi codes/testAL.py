
import json
from watson_developer_cloud import AlchemyLanguageV1


def alchemyL(p):
	alchemy_language = AlchemyLanguageV1(api_key='')       // key obtained from watson developer cloud

	inp = p;
	#print(inp);

	str = json.dumps(
	  alchemy_language.emotion(
	    text=inp),
	  indent=0);
	  
	#print(str);
	strarray = str.split();
	#print strarray;

	#print(len(str));  

	emot = ['000','000','000','000','000'];
	value = [0,0,0,0,0];

	j = 0;

	for i in range(0,len(strarray)):
	        
	        if (strarray[i] == '"anger":' or 
	        strarray[i] == '"joy":' or 
	        strarray[i] == '"fear":' or 
	        strarray[i] == '"sadness":' or 
	        strarray[i] == '"disgust":'):

	                ch='"';
	                l=2;
	                emot[j]=strarray[i+1][1];
	                #print strarray[i+1];

	                while l>=0:
	                        if(strarray[i+1][l]==ch):
	                                break;
	                        emot[j]+=strarray[i+1][l];
	                        l=l+1;
	                #print(emot[j]);
	                
	                #emot[j] = str[i+5]+str[i+6]+str[i+7]+str[i+8]+str[i+9]; #7to9
	                value[j] = float(emot[j]);
	                j = j+1;
	                #print(value[j-1]);

	                

	maxEmot = max(value);
	emotion = 0.000;

	if (maxEmot==0):
	        print('I am Neutral');
		a = 'I am Neutral';
		emotion = 5;
	else:
	        for k in range(0,4):

	                if(value[k] == maxEmot):
	                       emotion = k;                  #can be used for motor
	                       break;

	        #print(emotion);

	        if(emotion == 0):
	                print('I am Angry');
	                a = 'I am Angry'
	        
	        elif(emotion == 1):
	                print('I am Happy');
	                a = 'I am Happy'
	        
	        elif(emotion == 2):
	                print('I am Scared');
	                a = 'I am Scared'
	        
	        elif(emotion == 3):
	                print('I am Sad');
	                a = 'I am Sad'
	                
	        elif(emotion == 4):
	                print('I am Disgusted');
	                a = 'I am Disgusted'




	return a,emotion
alchemyL("hello")