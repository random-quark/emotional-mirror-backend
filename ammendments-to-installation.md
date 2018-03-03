#security 7105

# install pip
sudo apt-get install python-pip


### DUPLICATE
virtualenv venv
source venv/bin/activate


export CONSUMER_KEY="Y8wL0a8Fpr4FoofyEddqhZEIa"
export CONSUMER_SECRET="BvWilCUhMy4pZt20KotKYRNHiCB4c411JRD9KnTPHFzjn8BiTK"
export ACCESS_TOKEN="245278880-s5WGEzgRcxyv22dztCWMNaJYRhR51umMbFnKjB8F"
export ACCESS_TOKEN_SECRET="ly6kAhL3fqVu1gAcYnVfTkJYIn1E4ackCIMMNu8ub8JP6"

# PREPARE REQUIREMENTS.txt file

# not the case - we track both
 At the moment the last command should be ran for a little bit only just to get a few data (say 100 or so). Then, open the twitterEmoSpider.py and change the words_to_track variable from sad to happy. I plan to make this process smarter. For the moment leave it as is.


####################
FRONT END
###################

https://github.com/armadillu/ofxFboBlur.git

ofxCv
git checkout stable

ofxFaceTracker
remeber to copy the models.

# supervisor
apt-get install supervisor
# in settings file of supervisor
autostart = false (so that it does not start on startup via this process)
# but then you put it in the startup applications as
supervisorctl restart emotionalMirrorFrontend
with a delay of 3 (seconds)
# system settings -> panel (autohide)
# desktop -> hide all icons

############# DID NOt MANAGE
sudo apt-get install qv4l2

# HDMI2 instead of 1
xrandr --output HDMI2 --rotate right

NEEDED?
# to run xandr (for screen rotation)
sudo aptitude install x11-xserver-utils


# ssh connecting
ssh randomquark@10.100.9.54

# autologin
* settings -> login -> autologin for selected user

#turn off screensaver

#restart mirror every 30 minutes
add this: */30 *	* * *	root	supervisorctl restart emotionalMirrorFrontend
to this: /etc/crontab
then this to restart cron: sudo service cron restart

# BOOT ON POWER in bios
press F2 to enter bios in NUC

# change camera settings (manual vs. auto)
open from applications: QT V4L2


# ISSUES######################
* we used to start mongod from supervisord. What happens now if mongo crashes?
