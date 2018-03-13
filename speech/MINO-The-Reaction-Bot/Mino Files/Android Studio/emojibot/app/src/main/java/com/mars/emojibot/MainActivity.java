package com.mars.emojibot;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Context;
import android.content.Intent;
import android.os.ParcelUuid;
import android.os.StrictMode;
import android.provider.Settings;
import android.speech.RecognizerIntent;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.lang.reflect.Method;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.Locale;
import java.util.UUID;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.toolbox.Volley;
import com.ibm.watson.developer_cloud.alchemy.v1.AlchemyLanguage;
import com.ibm.watson.developer_cloud.alchemy.v1.AlchemyVision;
import com.ibm.watson.developer_cloud.alchemy.v1.model.DocumentEmotion;
import com.ibm.watson.developer_cloud.alchemy.v1.model.DocumentSentiment;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import android.content.Context;
import android.content.SharedPreferences;
import android.provider.Settings.Secure;
import android.telephony.TelephonyManager;

import java.io.UnsupportedEncodingException;
import java.util.UUID;



import com.ibm.watson.developer_cloud.alchemy.v1.AlchemyLanguage;
import com.ibm.watson.developer_cloud.alchemy.v1.model.DocumentSentiment;
import com.ibm.watson.developer_cloud.util.CredentialUtils;

import org.apache.http.client.HttpClient;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

//import org.json.simple.JSONObject;



public class MainActivity extends AppCompatActivity implements SensorEventListener{

    String text3;
    EditText input1,input2,input3;
    TextView out1;
    String switcharray[];
    String comm;

    private SensorManager mSensorManager;
    private Sensor mProximity;
    private static final int SENSOR_SENSITIVITY = 2;
    int i=0;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        out1 = (TextView) findViewById(R.id.textView);
        input1 = (EditText) findViewById(R.id.editText);
        input2 = (EditText) findViewById(R.id.ip);
        input3 = (EditText) findViewById(R.id.ip2);
        Button button = (Button) findViewById(R.id.button);
        Button button2 = (Button) findViewById(R.id.button2);       //Sleep
        Button button3 = (Button) findViewById(R.id.button3);       // motion forward
        Button button4 = (Button) findViewById(R.id.button4);            // motion reverse
        Button button5 = (Button) findViewById(R.id.button5);               //motion left
        Button button6 = (Button) findViewById(R.id.button6);            //motion right
        Button buttonR = (Button) findViewById(R.id.buttonR);
        Button sbutton = (Button) findViewById(R.id.sbutton);
        final Animation alpha = AnimationUtils.loadAnimation(this,R.anim.alpha);

        mSensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        mProximity = mSensorManager.getDefaultSensor(Sensor.TYPE_PROXIMITY);



        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                v.startAnimation(alpha);

                InputMethodManager imm = (InputMethodManager) getSystemService(
                        INPUT_METHOD_SERVICE);
                imm.hideSoftInputFromWindow(getCurrentFocus().getWindowToken(), 0);

                int flag =0;

                String load = "Loading.....";
                String fail = "Failed! :( ";

                out1.setText(String.valueOf(load));
                //Log.d("httpget", load);

                String text1 = input1.getText().toString();
                String ip = input2.getText().toString();
                String ip2 = input3.getText().toString();



                StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                StrictMode.setThreadPolicy(policy);



                try{

                    // URLEncode user defined data

                    String val1  = URLEncoder.encode(text1, "UTF-8");



                    // Create http cliient object to send request to server

                    HttpClient Client = new DefaultHttpClient();

                    // Create URL string

                    String URL = "http://" + ip +":8080/querytest?param1="+val1;

                    Log.i("httpget", URL);

                    try
                    {
                        String SetServerString = "";

                        // Create Request to server and get response

                        long startTime = System.currentTimeMillis(); //fetch starting time
                        while(false||(System.currentTimeMillis()-startTime)<10000)
                        {    if (flag==1)
                            {
                               break;
                            }

                            HttpGet httpget = new HttpGet(URL);

                            ResponseHandler<String> responseHandler = new BasicResponseHandler();

                            SetServerString = Client.execute(httpget, responseHandler);
                            flag = 1;
                           }

                        // Show response on activity

                        if(SetServerString.equals("")) {

                            Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                        }

                        else{
                            out1.setText(SetServerString);

                            SetServerString = SetServerString.toLowerCase();

                            switcharray = SetServerString.split(" ");  // switching on switch 1
                            Log.d("switch",switcharray[0]);

                            if(switcharray[0].equals("switching")) {

                                if (switcharray[3].equals("1")) {

                                    if (switcharray[1].equals("on")) {
                                        comm = "11";
                                    } else {
                                        comm = "10";
                                    }

                                }
                                else if (switcharray[3].equals("2")) {

                                    if (switcharray[1].equals("on")) {
                                        comm = "21";
                                    } else {
                                        comm = "20";
                                    }

                                }
                                else if (switcharray[3].equals("3")) {

                                    if (switcharray[1].equals("on")) {
                                        comm = "31";
                                    } else {
                                        comm = "30";
                                    }

                                }

                                int flag2 =0;

                                try {

                                    String val2 = URLEncoder.encode(comm, "UTF-8");

                                    // Create http cliient object to send request to server

                                    HttpClient Client2 = new DefaultHttpClient();

                                    // Create URL string

                                    String URL2 = "http://" + ip2 + "/" + val2;
                                    Log.i("httpget", URL2);

                                    try {
                                        String SetServerString2 = "";

                                        // Create Request to server and get response

                                        long startTime2 = System.currentTimeMillis(); //fetch starting time
                                        while (false || (System.currentTimeMillis() - startTime2) < 10000) {
                                            if (flag2 == 1) {
                                                break;
                                            }

                                            HttpGet httpget2 = new HttpGet(URL2);

                                            ResponseHandler<String> responseHandler2 = new BasicResponseHandler();

                                            SetServerString2 = Client.execute(httpget2, responseHandler2);
                                            flag2 = 1;
                                        }

                                        if (SetServerString2.equals("")) {

                                            Toast.makeText(MainActivity.this, "Switches are unreachable :(", Toast.LENGTH_SHORT).show();
                                        } else {
                                            out1.setText(SetServerString2);
                                        }

                                    } catch (Exception ex) {

                                    }


                                } catch (Exception ex) {
                                    out1.setText("Could Not Connect to Switch");
                                }
                            }
                        }

                    }
                    catch(Exception ex)
                    {
                        out1.setText(fail);
                        Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                    }
                }
                catch(UnsupportedEncodingException ex)
                {
                    out1.setText(fail);
                    Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                }



            }
        });



        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                input1.getText().clear();

                int flag =0;

                String load = "Loading.....";
                String fail = "Failed! :( ";

                out1.setText(String.valueOf(load));
                //Log.d("httpget", load);

                //String text1 = input1.getText().toString();
                String ip = input2.getText().toString();



                StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                StrictMode.setThreadPolicy(policy);



                try{

                    // URLEncode user defined data

                    String val1  = URLEncoder.encode("Sleep", "UTF-8");



                    // Create http cliient object to send request to server

                    HttpClient Client = new DefaultHttpClient();

                    // Create URL string

                    String URL = "http://" + ip +":8080/querytest?param1="+val1;

                    Log.i("httpget", URL);

                    try
                    {
                        String SetServerString = "";

                        // Create Request to server and get response

                        long startTime = System.currentTimeMillis(); //fetch starting time
                        while(false||(System.currentTimeMillis()-startTime)<10000)
                        {    if (flag==1)
                        {
                            break;
                        }

                            HttpGet httpget = new HttpGet(URL);

                            ResponseHandler<String> responseHandler = new BasicResponseHandler();

                            SetServerString = Client.execute(httpget, responseHandler);
                            flag = 1;
                        }

                        // Show response on activity

                        if(SetServerString.equals("")) {

                            Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                        }

                        else{
                            out1.setText(SetServerString);
                        }

                    }
                    catch(Exception ex)
                    {
                        out1.setText(fail);
                        Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                    }
                }
                catch(UnsupportedEncodingException ex)
                {
                    out1.setText(fail);
                    Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                }



            }
        });


        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                input1.getText().clear();

                int flag =0;

                String load = "Loading.....";
                String fail = "Failed! :( ";

                out1.setText(String.valueOf(load));
                //Log.d("httpget", load);

                //String text1 = input1.getText().toString();
                String ip = input2.getText().toString();



                StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                StrictMode.setThreadPolicy(policy);



                try{

                    // URLEncode user defined data

                    String val1  = URLEncoder.encode("motion forward", "UTF-8");



                    // Create http cliient object to send request to server

                    HttpClient Client = new DefaultHttpClient();

                    // Create URL string

                    String URL = "http://" + ip +":8080/querytest?param1="+val1;

                    Log.i("httpget", URL);

                    try
                    {
                        String SetServerString = "";

                        // Create Request to server and get response

                        long startTime = System.currentTimeMillis(); //fetch starting time
                        while(false||(System.currentTimeMillis()-startTime)<10000)
                        {    if (flag==1)
                        {
                            break;
                        }

                            HttpGet httpget = new HttpGet(URL);

                            ResponseHandler<String> responseHandler = new BasicResponseHandler();

                            SetServerString = Client.execute(httpget, responseHandler);
                            flag = 1;
                        }

                        // Show response on activity

                        if(SetServerString.equals("")) {

                            Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                        }

                        else{
                            out1.setText(SetServerString);
                        }

                    }
                    catch(Exception ex)
                    {
                        out1.setText(fail);
                        Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                    }
                }
                catch(UnsupportedEncodingException ex)
                {
                    out1.setText(fail);
                    Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                }



            }
        });


        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                input1.getText().clear();

                int flag =0;

                String load = "Loading.....";
                String fail = "Failed! :( ";

                out1.setText(String.valueOf(load));
                //Log.d("httpget", load);

                //String text1 = input1.getText().toString();
                String ip = input2.getText().toString();



                StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                StrictMode.setThreadPolicy(policy);



                try{

                    // URLEncode user defined data

                    String val1  = URLEncoder.encode("motion reverse", "UTF-8");



                    // Create http cliient object to send request to server

                    HttpClient Client = new DefaultHttpClient();

                    // Create URL string

                    String URL = "http://" + ip +":8080/querytest?param1="+val1;

                    Log.i("httpget", URL);

                    try
                    {
                        String SetServerString = "";

                        // Create Request to server and get response

                        long startTime = System.currentTimeMillis(); //fetch starting time
                        while(false||(System.currentTimeMillis()-startTime)<10000)
                        {    if (flag==1)
                        {
                            break;
                        }

                            HttpGet httpget = new HttpGet(URL);

                            ResponseHandler<String> responseHandler = new BasicResponseHandler();

                            SetServerString = Client.execute(httpget, responseHandler);
                            flag = 1;
                        }

                        // Show response on activity

                        if(SetServerString.equals("")) {

                            Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                        }

                        else{
                            out1.setText(SetServerString);
                        }

                    }
                    catch(Exception ex)
                    {
                        out1.setText(fail);
                        Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                    }
                }
                catch(UnsupportedEncodingException ex)
                {
                    out1.setText(fail);
                    Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                }



            }
        });


        button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                input1.getText().clear();

                int flag =0;

                String load = "Loading.....";
                String fail = "Failed! :( ";

                out1.setText(String.valueOf(load));
                //Log.d("httpget", load);

                //String text1 = input1.getText().toString();
                String ip = input2.getText().toString();



                StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                StrictMode.setThreadPolicy(policy);



                try{

                    // URLEncode user defined data

                    String val1  = URLEncoder.encode("motion left", "UTF-8");



                    // Create http cliient object to send request to server

                    HttpClient Client = new DefaultHttpClient();

                    // Create URL string

                    String URL = "http://" + ip +":8080/querytest?param1="+val1;

                    Log.i("httpget", URL);

                    try
                    {
                        String SetServerString = "";

                        // Create Request to server and get response

                        long startTime = System.currentTimeMillis(); //fetch starting time
                        while(false||(System.currentTimeMillis()-startTime)<10000)
                        {    if (flag==1)
                        {
                            break;
                        }

                            HttpGet httpget = new HttpGet(URL);

                            ResponseHandler<String> responseHandler = new BasicResponseHandler();

                            SetServerString = Client.execute(httpget, responseHandler);
                            flag = 1;
                        }

                        // Show response on activity

                        if(SetServerString.equals("")) {

                            Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                        }

                        else{
                            out1.setText(SetServerString);
                        }

                    }
                    catch(Exception ex)
                    {
                        out1.setText(fail);
                        Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                    }
                }
                catch(UnsupportedEncodingException ex)
                {
                    out1.setText(fail);
                    Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                }



            }
        });



        button6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                input1.getText().clear();

                int flag =0;

                String load = "Loading.....";
                String fail = "Failed! :( ";

                out1.setText(String.valueOf(load));
                //Log.d("httpget", load);

                //String text1 = input1.getText().toString();
                String ip = input2.getText().toString();



                StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                StrictMode.setThreadPolicy(policy);



                try{

                    // URLEncode user defined data

                    String val1  = URLEncoder.encode("motion right", "UTF-8");



                    // Create http cliient object to send request to server

                    HttpClient Client = new DefaultHttpClient();

                    // Create URL string

                    String URL = "http://" + ip +":8080/querytest?param1="+val1;

                    Log.i("httpget", URL);

                    try
                    {
                        String SetServerString = "";

                        // Create Request to server and get response

                        long startTime = System.currentTimeMillis(); //fetch starting time
                        while(false||(System.currentTimeMillis()-startTime)<10000)
                        {    if (flag==1)
                        {
                            break;
                        }

                            HttpGet httpget = new HttpGet(URL);

                            ResponseHandler<String> responseHandler = new BasicResponseHandler();

                            SetServerString = Client.execute(httpget, responseHandler);
                            flag = 1;
                        }

                        // Show response on activity

                        if(SetServerString.equals("")) {

                            Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                        }

                        else{
                            out1.setText(SetServerString);
                        }

                    }
                    catch(Exception ex)
                    {
                        out1.setText(fail);
                        Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                    }
                }
                catch(UnsupportedEncodingException ex)
                {
                    out1.setText(fail);
                    Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                }



            }
        });


        buttonR.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                InputMethodManager imm = (InputMethodManager) getSystemService(
                        INPUT_METHOD_SERVICE);
                imm.hideSoftInputFromWindow(getCurrentFocus().getWindowToken(), 0);

                input1.getText().clear();
                out1.setText(" ");

            }
        });


        sbutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                input1.getText().clear();
                out1.setText(" ");

                Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
                intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Talk to Mino");
                intent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 1);
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.ENGLISH);
                startActivityForResult(intent, 1);

            }
        });



            }


    @Override
    public void onActivityResult(int requestCode,int resultCode, Intent data){

        try {
            if (requestCode == 1) {

                ArrayList<String> results;
                results = data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                text3 = results.get(0).replace(",", "");

                input1.setText("Speech Sent");

                InputMethodManager imm = (InputMethodManager) getSystemService(
                        INPUT_METHOD_SERVICE);
                imm.hideSoftInputFromWindow(getCurrentFocus().getWindowToken(), 0);

                int flag =0;


                String load = "Loading.....";
                String fail = "Mino can't hear you! :( ";

                out1.setText(String.valueOf(load));
                //Log.d("httpget", load);

                String text1 = input1.getText().toString();
                String ip = input2.getText().toString();
                String ip2 = input3.getText().toString();



                StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                StrictMode.setThreadPolicy(policy);



                try{

                    // URLEncode user defined data

                    String val1  = URLEncoder.encode(text3, "UTF-8");



                    // Create http cliient object to send request to server

                    HttpClient Client = new DefaultHttpClient();

                    // Create URL string

                    String URL = "http://" + ip +":8080/querytest?param1="+val1;

                    Log.i("httpget", URL);

                    try
                    {
                        String SetServerString = "";

                        // Create Request to server and get response

                        long startTime = System.currentTimeMillis(); //fetch starting time
                        while(false||(System.currentTimeMillis()-startTime)<10000)
                        {    if (flag==1)
                        {
                            break;
                        }

                            HttpGet httpget = new HttpGet(URL);

                            ResponseHandler<String> responseHandler = new BasicResponseHandler();

                            SetServerString = Client.execute(httpget, responseHandler);
                            flag = 1;
                        }

                        // Show response on activity

                        if(SetServerString.equals("")) {

                            Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                        }

                        else{
                            out1.setText(SetServerString);

                            SetServerString = SetServerString.toLowerCase();

                            switcharray = SetServerString.split(" ");  // switching on switch 1
                            Log.d("switch",switcharray[0]);

                            if(switcharray[0].equals("switching")) {

                                if (switcharray[3].equals("1")) {

                                    if (switcharray[1].equals("on")) {
                                        comm = "11";
                                    } else {
                                        comm = "10";
                                    }

                                }
                                else if (switcharray[3].equals("2")) {

                                    if (switcharray[1].equals("on")) {
                                        comm = "21";
                                    } else {
                                        comm = "20";
                                    }

                                }
                                else if (switcharray[3].equals("3")) {

                                    if (switcharray[1].equals("on")) {
                                        comm = "31";
                                    } else {
                                        comm = "30";
                                    }

                                }

                                int flag2 =0;

                                try {

                                    String val2 = URLEncoder.encode(comm, "UTF-8");

                                    // Create http cliient object to send request to server

                                    HttpClient Client2 = new DefaultHttpClient();

                                    // Create URL string

                                    String URL2 = "http://" + ip2 + "/" + val2;
                                    Log.i("httpget", URL2);

                                    try {
                                        String SetServerString2 = "";

                                        // Create Request to server and get response

                                        long startTime2 = System.currentTimeMillis(); //fetch starting time
                                        while (false || (System.currentTimeMillis() - startTime2) < 10000) {
                                            if (flag2 == 1) {
                                                break;
                                            }

                                            HttpGet httpget2 = new HttpGet(URL2);

                                            ResponseHandler<String> responseHandler2 = new BasicResponseHandler();

                                            SetServerString2 = Client.execute(httpget2, responseHandler2);
                                            flag2 = 1;
                                        }

                                        if (SetServerString2.equals("")) {

                                            Toast.makeText(MainActivity.this, "Switches are unreachable :(", Toast.LENGTH_SHORT).show();
                                        } else {
                                            out1.setText(SetServerString2);
                                        }

                                    } catch (Exception ex) {

                                    }


                                } catch (Exception ex) {
                                    out1.setText("Could Not Connect to Switch");
                                }
                            }
                        }

                    }
                    catch(Exception ex)
                    {
                        out1.setText(fail);
                        Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                    }
                }
                catch(UnsupportedEncodingException ex)
                {
                    out1.setText(fail);
                    Toast.makeText(MainActivity.this, "Connection timed out!", Toast.LENGTH_SHORT).show();
                }



            }
        }
        catch(Exception ex){
            /*out1.setText("");
            input1.setText("");*/
        }

    }

    @Override
    protected void onResume() {
        super.onResume();
        mSensorManager.registerListener(this, mProximity, SensorManager.SENSOR_DELAY_NORMAL);
    }

    @Override
    protected void onPause() {
        super.onPause();
        mSensorManager.unregisterListener(this);
    }

    @Override
    public void onSensorChanged(SensorEvent event) {

        if (event.sensor.getType() == Sensor.TYPE_PROXIMITY ) {

            if (event.values[0] >= -SENSOR_SENSITIVITY && event.values[0] <= SENSOR_SENSITIVITY ) {
                //near

                //Toast.makeText(getApplicationContext(), "near", Toast.LENGTH_SHORT).show();
                if(i>=2){
                   // box.setText("near");

                    InputMethodManager imm = (InputMethodManager) getSystemService(
                            INPUT_METHOD_SERVICE);
                    imm.hideSoftInputFromWindow(getCurrentFocus().getWindowToken(), 0);

                    String ip2 = input3.getText().toString();


                    StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                    StrictMode.setThreadPolicy(policy);

                    int flag2 =0;
                    int flag3 =0;
                    int flag4 =0;

                    try {

                        String val2 = URLEncoder.encode("10", "UTF-8");
                        String val3 = URLEncoder.encode("20", "UTF-8");
                        String val4 = URLEncoder.encode("30", "UTF-8");
                        // Create http cliient object to send request to server

                        HttpClient Client2 = new DefaultHttpClient();
                        HttpClient Client3 = new DefaultHttpClient();
                        HttpClient Client4 = new DefaultHttpClient();

                        // Create URL string

                        String URL2 = "http://" + ip2 + "/" + val2;
                        Log.i("httpget", URL2);

                        String URL3 = "http://" + ip2 + "/" + val3;
                        Log.i("httpget3", URL3);

                        String URL4 = "http://" + ip2 + "/" + val4;
                        Log.i("httpget4", URL4);


                        try {
                            String SetServerString2 = "";
                            String SetServerString3 = "";
                            String SetServerString4 = "";

                            // Create Request to server and get response

                            long startTime2 = System.currentTimeMillis(); //fetch starting time
                            while (false || (System.currentTimeMillis() - startTime2) < 10000) {
                                if (flag2 == 1) {
                                    break;
                                }

                                HttpGet httpget2 = new HttpGet(URL2);
                                ResponseHandler<String> responseHandler2 = new BasicResponseHandler();
                                SetServerString2 = Client2.execute(httpget2, responseHandler2);

                                HttpGet httpget3 = new HttpGet(URL3);
                                ResponseHandler<String> responseHandler3 = new BasicResponseHandler();
                                SetServerString3 = Client2.execute(httpget3, responseHandler3);


                                HttpGet httpget4 = new HttpGet(URL4);
                                ResponseHandler<String> responseHandler4 = new BasicResponseHandler();
                                SetServerString4 = Client2.execute(httpget4, responseHandler4);

                                flag2 = 1;
                            }

                            Log.d("ESP return 2",SetServerString2);


                            if (SetServerString2.equals("") || SetServerString3.equals("") || SetServerString4.equals("")) {

                                Toast.makeText(MainActivity.this, "Some lights are still ON :(", Toast.LENGTH_SHORT).show();
                            } else {
                                String s  = "All lights are now OFF :)";
                                out1.setText("All lights are now OFF :)");
                                Toast.makeText(getApplicationContext(), "All lights are now OFF :)", Toast.LENGTH_SHORT).show();
                            }

                        } catch (Exception ex) {
                            out1.setText("Could Not Connect to Switch");
                        }


                    } catch (Exception ex) {
                        out1.setText("Could Not Connect to Switch");
                    }

                    i=0;}

                else{
                    i=i+1;
                   // box.setText("far");
                }

            } else {
                //far
                //Toast.makeText(getApplicationContext(), "far", Toast.LENGTH_SHORT).show();
                //box.setText("far");
            }
        }

    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }




}


