__author__ = "Sergey Koniukhovskiy"


# some settings
script_url = 'http://lamp/php_playground/grabr/up.php'
storage_url = 'http://lamp/php_playground/grabr/up/%s'

from os import system
import pycurl
from getpass import getuser
from datetime import datetime

def shot():
	filename = '%s_%s.png' % (getuser(),datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
	filepath = '/tmp/%s' % filename
	system('scrot -s %s' % filepath)
	return filename, filepath

def clip(text):
	
	system('echo "%s" | xsel -b -i' % text)

def up(filepath):
	c = pycurl.Curl()
	c.setopt(pycurl.URL, script_url)
	c.setopt(pycurl.POST, True)
	c.setopt(c.HTTPPOST, [("file", (c.FORM_FILE, filepath)),("pass","qwerty")])
	c.perform()
	c.close()
	
if __name__ == "__main__":
	filename, filepath = shot()
	clip(storage_url % filename)
	up(filepath)

