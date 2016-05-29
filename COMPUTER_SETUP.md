# Preparing the Ubuntu machine
### initial steps
```
sudo apt-get install openssh-server
cd ~/
mkdir "Emotional Mirror"
cd "Emotional Mirror"
git clone https://github.com/random-quark/emotional-mirror-backend.git
```

### to allow sessions to leave after you logged out
```
sudo apt-get install screen
```

### to be able to control the settings on the PSeye3 camera
```
sudo apt-get install qv4l2
run qv4l2 and go to 3rd panel to turn off automatic exposure
```

### to make sure it doesn't stop running
```
install supervisord
setup supervisord config (see example in emotional-mirror-backend/utilities/ folder)
add supervisord to startup applications (ensure it's alphabetically after previous command)
Also open /etc/crontab and add this line below:`*/20 *	* * *	root	supervisorctl restart emotionalMirrorFrontend`
```

### to rotate the screen 90 degrees
```
add xrandr --output HDMI1 --rotate right to startup applications
```

### to make sure machine boots after power failure:
```
Wake up on power (from bios)
```
