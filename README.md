# sensit_web_callback (or the IoT doorbell)
A simple Flak app to react to sensit.io callbacks 

## 0. What is this?

A [Sens'it](https://sensit.io) is a wireless Internet of Things device, using the [Sigfox](http://www.sigfox.com) network. It provides 4 sensors :
 * temperature
 * motion
 * sound
 * a button

Sensit website provides some possibilities to trigger a callback URL wheb some actions are completed.
For instance, you can have a request on your webserver when you press the button, when a new temperature is sent, or when anything is send from the device. The website also provides more advanced functions, for instance, you get a request when a measure leave some threshold for instance. 

For a better explaination of the API, check [sensit website](https://api.sensit.io/v1/) 

This project aims to show how we can react to this requests and send a notification each time you press the button using [Pushbullet](http://www.pushbullet.com)

## 1. Activate the callbacks in sensit.io configuration

1. Log in
2. Click on the "My sens'it" tab  (https://sensit.io/home)
3. Find the button menu and click on "Notifications"
4. Add a new notification, each time the button is pressed, with the callback you want (you can notice you can also send mails)

## 2. Pushbullet

1. Create an account
2. Install it on your smartphone
3. Get your API Token (go to the website, log in, then settings -> accounts -> your token)

## 3. Put the app on your server

0. you may want to change your webserver config to add a reverse proxy. Here is a quick and dirty configuration for nginx

```nginx
server {                                                                    
  listen 80 ;                                                             
  listen [::]:80;                                                         
  
  server_name CALLBACK.URL.IN.THE.SENSIT.CONFIG;                                           
  
  location / {                                                            
    proxy_pass http:YOUR.SERVER.URL:31415;                                  
  }                                                                      
}  
```

1. clone the repo
2. install the dependancies : `pip install -r requirement.txt`

4. Change the token with your real token
5. Launch the app : `python app/app.py` 
6. Test : press the button or go directly go to the adress in your brower (your.URL/button:31415)

## Enjoy !
You now have a connected doorbell ! 
You can use it to know on your smartphone when guest are coming in your mansion.
SO MUCH SWAG

You can improve it with different notifications, for example put your Sens'it in sound mode, put it in baby's room and send a notif each time you have a noise (you will need to change the app code, and react to another callback URL). BAM you have made a connected babyphone (disclaimer: buy a real baby phone ;) ) 

Imagination is your only limit !
