# aes
CS361 assignment

Rinchen Tsering (rt24456)
Briana Vargas (blv473)

main():

	Encryption:
		Reads in message to encrypt from provided input file.
		Pads data using CMS padding with a call to pad().
		Calls aes_encrypt with 16-byte sections of padded data until all data is encrypted.
		Writes to outputfile.
		
	Decryption:
		Reads in message to decrypt from provided input file.
		Calls aes_decrypt with 16-byte sections of datat until all data is decrypted.
		Removes padding from decrypted data.
		Writes to output file.


aes_encrypt():

	Takes in 16-byte message to encrypt, key of size either 128 or 256, size of key.
	Initializes empty state array.
	Sets number of words in key schedule and number of rounds of encryption based on keysize.
	Calls fill_first_round() to place the first 4 (for 128) or 8 (for 256) words in the key schedule.
	Calls either key_expansion_128() or key_expansion_256() to fill the rest of the key schedule.
	Initialize the round key with call to add_round_key_init().
	Calls sub_bytes(), shift_rows(), mix_columns(), and get_sub_keys(), and add_round_key() for appropriate amount of rounds based on keysize to perform actual encryption.
	Calls methods again without mix_columns() for final round, returns the final round key as encrypted message.

aes_decrypt():
	
	Takes in 16-byte message to decrypt, key of size either 128 or 256, size of key.
	Initializes empty state array.
	Sets number of words in key schedule and number of rounds of decryption based on keysize.
	Calls fill_first_round() to place the first 4 (for 128) or 8 (for 256) words in the key schedule.
	Calls either key_expansion_128() or key_expansion_256() to fill the rest of the key schedule.
	Gets appropriate key set.
	Runs the first add_round_key method.
	Loop through appropriate number of rounds and applies inv_shift_rows(), inv_sub_bytes(), add_round_key() and inv_mix_columns() respectively.
	For the last round, in_mix_columns is skipped.
	
xor():
	
	Since each word is saved in an array of 4 bytes, this method is used to xor each byte of a word with each byte of another word.

fill_first_round():
	
	Place the first 4 (for 128) or 8 (for 256) words in the key schedule.

key_expansion_128():
	
	A recursive method that expands the key schedule by adding to 40 additional words from the intial 4 words placed. 
	temp0 is initialized by rotating orig3 (the last word in the previous column), substituting each byte with values from s_box with a call to get_sub_word(), and xor-ing itself with its corresponding rcon value.
	Each temp value is then filled in by calling xor() with the previous temp value (temp0 uses itself) and its corresponding orig value from the previous column.
	This goes on for 10 rounds and the values are stored in keySchedule as hex strings.

key_expansion_256():
	
	This method behaves simalarly to key_expansion_128() except that it creates 8 words at a time with 7 rounds rather than 4 words at a time with 10 rounds.
	The final round of the expansion will only create 4 words instead of eight.
	temp0, or the first word created, is created simalarly to the first word in the 128 keysize expansion, but there is also a special case in 256 for the 5th word (temp4). It must be substituted with s_box values before being xor-ed.

get_stateHex():
	
	converts and returns state elements to hexadecimal type.

sub_bytes():
	
	substitute state bytes from corresponding s_box

inv_sub_bytes():
	
	substitute state bytes from corresponding inv_s_box

shift_rows():
	
	created an empty temp list of size 16
	filled the temp list with the appropriate state value
	filled the state array with the temp values so that the state array has all its elements in the shifted positions.  

inv_shift_rows():
	
	created an empty temp list of size 16
	filled the temp list with the appropriate state value
	filled the state array with the temp values so that the state array has all its elements in the shifted positions.

mix_columns():
	
	created an empty temp list of size 16
	filled the temp list with the appropriate result from the operations described below
	each temp variable is a result of xor applied on the words and appropriate bytes converted to correct product using galois field multiplication look up table of mul2 and mul3.  

inv_mix_columns():
	
	created an empty temp list of size 16
	filled the temp list with the appropriate result from the operations described below.
	each temp variable is a result of xor applied on the words and appropriate bytes converted to correct product using galois field multiplication look up table of mul9, mul11, mul13 and mul14.

add_round_key_init():
	
	xor's the appropriate key with the initial state

add_round_key():
	
	xor's the appropriate key with the current state

add_round_key_final():
	
	xor's the appropriate key with the final state

get_sub_keys(): 
	
	creates and returns a key set from the appropriate array slice of keySchedule 

get_stateInt():
	
	converts and returns state elements to int type.

pad():
	
	Uses CMS padding to pad message into an array of a multiple of 16. Adds 16 if it was already a multiple.

remove_padding():
	
	Remove CMS padding by looking at the value of the last byte and removing that many bytes from the end of the data array







