def encrypt(phrase, key):
	assert isinstance(phrase, str) and isinstance(key, str)
	key = key.lower()
	phrase = phrase.lower()
	new_phrase = ''
	key_idx = 0

	# increment through the characters of the phrase
	for i in range(len(phrase)):
		# if it is a letter of the alphabet encode it
		if phrase[i].isalpha():
			# converting letters to what number letter they are in the alphabet
			key_char_num = ord(key[key_idx]) - ord('a')
			phrase_char_num = ord(phrase[i]) - ord('a')
			# add the current key character to the current phrase character
			new_phrase_char_num = (phrase_char_num + key_char_num) % 26
			# convert the number into the new character
			new_phrase += chr(new_phrase_char_num + ord('a'))
			# increment the key
			key_idx = (key_idx + 1) % len(key)
		# if it is not a letter of the alphabet, leave it alone
		else:
			new_phrase += phrase[i]

	return new_phrase

def decrypt(phrase, key):
	assert isinstance(phrase, str) and isinstance(key, str)
	key = key.lower()
	phrase = phrase.lower()
	new_phrase = ''
	key_idx = 0
	
	# increment through the characters of the phrase
	for i in range(len(phrase)):
		# if it is a letter of the alphabet encode it
		if phrase[i].isalpha():
			# converting letters to what number letter they are in the alphabet
			key_char_num = ord(key[key_idx]) - ord('a')
			phrase_char_num = ord(phrase[i]) - ord('a')
			# subtract the current key character to the current phrase character
			new_phrase_char_num = (phrase_char_num - key_char_num) % 26
			# convert the number into the new character
			new_phrase += chr(new_phrase_char_num + ord('a'))
			# increment the key
			key_idx = (key_idx + 1) % len(key)
		# if it is not a letter of the alphabet, leave it alone
		else:
			new_phrase += phrase[i]

	return new_phrase
