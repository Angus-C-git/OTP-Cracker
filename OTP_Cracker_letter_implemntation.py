letter_codec = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5,
	'f': 6,
	'g': 7,
	'h': 8,
	'i': 9,
	'j': 10,
	'k': 11,
	'l': 12,
	'm': 13,
	'n': 14,
	'o': 15,
	'p': 16,
	'q': 17,
	'r': 18,
	's': 19,
	't': 20,
	'u': 21,
	'v': 22,
	'w': 23,
	'x': 24,
	'y': 25,
	'z': 26
}


reverse_letter_codec = {
	1: 'a',
	2: 'b',
	3: 'c',
	4: 'd',
	5: 'e',
	6: 'f',
	7: 'g',
	8: 'h',
	9: 'i',
	10: 'j',
	11: 'k',
	12: 'l',
	13: 'm',
	14: 'n',
	15: 'o',
	16: 'p',
	17: 'q',
	18: 'r',
	19: 's',
	20: 't',
	21: 'u',
	22: 'v',
	23: 'w',
	24: 'x',
	25: 'y',
	26: 'z'
}

common_words = [
	'the',
	'be',
	'to',
	'of',
	'and',
	'a',
	'in',
	'that',
	'have',
	'i',
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
	'her',
	'she',
	'or'
]


def generateKey(cipher, guess):
	key = ''
	index = 0

	for letter in guess:
		letter_calc = letter_codec[cipher[index]] - letter_codec[letter]
		if letter_calc <= 0:
			letter_calc += 26
		key += reverse_letter_codec.get(letter_calc)
		index += 1
	print("\nProduced key:", key, "from: ", guess)
	return key


def crackMTP(cipher1, cipher2):
	for word in common_words:
		attempted_key_fragment = generateKey(cipher1, word)

		recovered_plaintext = ''
		index = 0
		for char in cipher2:
			if index == len(attempted_key_fragment):
				index = 0
				recovered_plaintext += ' '
			char_value = letter_codec.get(char) - letter_codec.get(attempted_key_fragment[index])
			if char_value <= 0:
				char_value += 26

			recovered_plaintext += reverse_letter_codec.get(char_value)
			index += 1
		
		print("Recovered plain txt:", recovered_plaintext)


def main():
	cipher1 = str(input("Enter cipher text 1: ")).lower()
	cipher2 = str(input("Enter cipher text 2: ")).lower()
	crackMTP(cipher1, cipher2)


main()

