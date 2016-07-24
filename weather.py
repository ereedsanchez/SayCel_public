import pyowm
import subprocess


owm = pyowm.OWM('db1195d9a23fe8e7fb99acb4370025c9')  # You MUST provide a valid API key

fc = owm.daily_forecast('Bluefields,ni', limit=6)
f = fc.get_forecast()

humidity = w.get_humidity() 
temp_max =  w.get_temperature(unit='celsius').get('temp_max') 
temp_min = w.get_temperature(unit='celsius').get('temp_min')
sunset = w.get_sunset_time('iso') 
for weather in f:
      print (weather.get_reference_time('iso'),weather.get_status())


# text = "Good Morning, today the temperature has a high of " + str(temp_max) + " and a low of " + str(temp_min) + ". There is currently " + str(humidity) + " percent humidity"



# subprocess.call([
#     "curl",
#     "--data",
#     "text="+text+"&btype=all", 
#     "http://127.0.0.1:8085/sms/send_broadcast"
# ])
