'''
Implementation of a caesar cipher with options to encrypt/decrypt a user given message with a user given key or run through all possible keys to brute force decrypt the message text. 

Does not translate non alphabetic characters. 
'''



# Ask user is they want to encrypt or decrypt a message

def get_mode():
	while True:
		print 'Do you wish to encrypt, decrypt, or brute force your message?'
		mode = raw_input().lower()
		if mode in  'encrypt e decrypt d brute b'.split(' '):
			return mode
		else:
			print "Please enter 'encrypt' or 'e', 'decrypt' or 'd', or 'brute' or 'b'"




# Ask user for the message

def get_message():
	print 'Please enter your message text'
	message = raw_input('message text:')
	return message




# Ask user for key

def get_key():
	key = 0
	while True:
		print 'Please enter the key you wish to use'
		key = int(raw_input('key:'))
		if key > 0 and key <= 26:
			return key
		else:
			print 'Please enter a value between 1 and 26'

		



# Define translate (encryption or decryption) function

def translate(mode, message, key):
	if mode[0] == 'd':			#if the mode is decrypt get the negative value of key
		key = -key
	translated = ''				# set translated variable

	for x in message:			# for every symbol in message
		if x.isalpha():			# if the symbol is part of the alphabet
			num = ord(x)		# get the ASCII value
			num += key		# and add the key given by the user

			if x.isupper():			# if the letter is uppercase
				if num > ord('Z'):	# and the number is > 90 or < 65
					num -= 26	# subtract or add 26 so that the shift
				elif num < ord('A'):	# remains correct and doesn't translate to a lowercase value
					num += 26
				
			
			elif x.islower():		# Same logic as for uppercase
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			translated += chr(num) 		# get the corresponding ASCII character after the key shift is applied

		else:					# if the symbol is not alphabetic, 
			translated += x			# keep the symbol as is in the translated message

	return translated

# Return the message


def main():
	
	mode = get_mode()
	message = get_message()	
	if mode[0] != 'b':
		key = get_key()
	print 'Your translated message is:'
	
	if mode[0] != 'b':	
		print translate(mode, message, key)
	else:
		for key in range(1, 27):
			print key, translate('decrypt', message, key)



if __name__ == '__main__':
	main()
















