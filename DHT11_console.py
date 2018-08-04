from time import sleep
from dhtxx import DHT11, DHT22

# Adjust pin (BCM) for your needs !
dht11 = DHT11(14)

while True:
 # Retries 'max_tries' from DHT11 to get a valid result
 r = dht11.get_result(max_tries=10)  # 'max_tries' defaults to 5
 if r:
  print('Temp: {0:0.1f} C Humidity; {1:0.1f} %'.format(r[0], r[1]))
 else:
  print('Failed to get result !')
 sleep(1)