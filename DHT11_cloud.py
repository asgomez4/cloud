from time import sleep
import http.client, urllib
from dhtxx import DHT11, DHT22

# Adjust pin (BCM) for your needs !
dht11 = DHT11(14)

while True:
 # Retries 'max_tries' from DHT11 to get a valid result
 r = dht11.get_result(max_tries=10)  # 'max_tries' defaults to 5
 if r:
  print('Temp: {0:0.1f} C Humidity; {1:0.1f} %'.format(r[0], r[1]))
  params = urllib.parse.urlencode({'field1': r[0],'field2': r[1], 'key':'OFQ8BD9IPMZKRWFQ'})
  headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
  conn = http.client.HTTPConnection("api.thingspeak.com:80")
  try:
   conn.request("POST", "/update", params, headers)
   response = conn.getresponse()
   print(response.status, response.reason)
   data = response.read()
   conn.close()
  except:
   print("connection failed")
  sleep(2)
 else:
  print('Failed to get result !')