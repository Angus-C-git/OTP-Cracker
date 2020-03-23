
common_words = [
	'the',
	'The',
	'be',
	'to',
	'of',
	'and',
	'a',
	'in',
	'that',
	'have',
	'I',
	'it',
	'for',
	'not',
	'on',
	'with',
	'he',
	'as',
	'you',
	'do',
	'at',
	'this',
	'but',
	'his',
	'by',
	'form',
	'they',
	'we',
	'say',
	'her'
	'she',
	'or'
]

def hexStr(string):
	hex_str = ''
	for letter in string:
		hex_str += hex(ord(letter))[2:]
	return hex_str

def xorStrings(str1, str2):
	 decimal_string1 = int(str1, 16)
	 decimal_string2 = int(str2, 16)
	 xored_string = hex(decimal_string1 ^ decimal_string2)

	 return(xored_string)


def beginDecodeCycle(guess, xored_cipher_txt):
	guess_hex = hexStr(guess)
	hex_decode_result = xorStrings(xored_cipher_txt[:len(guess_hex)], guess_hex)[2:]
	print("Hex Decode:", hex_decode_result)
	asccii_result = bytearray.fromhex(hex_decode_result).decode()
	print("Recoved ASCII Str:", asccii_result)
	guess = str(input("Guess word, pass(P) or return decrypted text (r): "))

	if guess == 'p':
		return
	elif guess == 'r':
		return asccii_result
	else:
		beginDecodeCycle(guess, xored_cipher_txt)


def checkReadability(hex_str, xored_cipher_txt):
	ascii_val = bytearray.fromhex(hex_str).decode()
	print("Recoved ASCII txt:", ascii_val)
	guess = str(input("Guess word or pass(p): "))

	if guess == 'p':
		return
	else:
		return (beginDecodeCycle(guess, xored_cipher_txt))

def generateEncryptedMessage(key, plaintext):
	hex_encrypted_msg = ''

	for char in range(len(plaintext)):
		char_xor = ord(plaintext[char]) ^ ord(key[char])
		hex_encrypted_msg += hex(char_xor)[2:].zfill(2)

	return hex_encrypted_msg


def decryptOTP(key, cipher_text):
	return xorStrings(key, cipher_text)


def crackROTP(cipher_text1, cipher_text2):
	#Stored result
	cracked_OTP = ''

	#XOR chipher texts
	xored_cipher = xorStrings(cipher_text1, cipher_text2)[2:]
	print(xored_cipher)
	
	for word in common_words:
		print("Current Guess:", word)
		
		# Generate Crib
		crib = ''
		for letter in word:
			crib += hex(ord(letter))[2:]
		
		# Drag the Crib
		drag_index = 0
		dragged_xor = ''
		for drag in range(int(len(xored_cipher)/len(crib))):
			dragged_xor = xorStrings(xored_cipher[drag_index:drag_index + len(crib)], crib)[2:]
			print("xoring:", xored_cipher[drag_index:drag_index + len(crib)],"with crib:",crib, "produced:", dragged_xor)
			cracked_OTP = checkReadability(dragged_xor, xored_cipher)
			print(cracked_OTP)
			# if cracked_OTP != 'None':
			#	return cracked_OTP
			drag_index += len(crib)
	return cracked_OTP

def main():
	print("-- Select Opperation --\n\n ~ (1) Encrypt Plaintext \n ~ (2) Decrypt Cipher Text \n ~ (3) Crack Resycled OTP Message")
	choice = str(input("~> "))
	if (choice == '1'):
		key = str(input("Enter pad: "))
		plaintext = str(input("\nEnter Plaintext: "))
		if len(key) >= len(plaintext):
			print("Genrated Message _>", generateEncryptedMessage(key, plaintext))
		else:
			print("The pad is too short for the message")
			main()
	elif (choice =='2'):
		key = str(input("Enter key: "))
		otp = str(input("Enter encrypted text: "))
		print("Decrypted text:", decryptOTP(key, otp))
	elif (choice == '3'):
		cipher_text1 = str(input("Enter the first cipher: ")).lower()
		cipher_text2 = str(input("Enter the second cipher: ")).lower()
		print("Recovered Plaintext: ", crackROTP(cipher_text1, cipher_text2))
	else:
		print("\nPlease enter a number shown above!")
		main()
main()

# 746865
# 746865

#3c0d094c1f523808000d09
#3c0d094c1f523808000d09