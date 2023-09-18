## NOTE: I already used discovery debugging to solve the below, so I am skipping challenge_three.

def make_cipher(key):
    #alphabet = [chr(i + 96) for i in range(1, 26)] #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'] 
    # #"z" is missing, fix below.
    alphabet = [chr(i + 96) for i in range(1, 27)]
    cipher_with_duplicates = list(key) + alphabet #['s', 'e', 'c', 'r', 'e', 't', 'k', 'e', 'y', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher #['s', 'e', 'c', 'r', 't', 'k', 'y', 'a', 'b', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'z']


def encode(text, key):
    cipher = make_cipher(key) #['s', 'e', 'c', 'r', 't', 'k', 'y', 'a', 'b', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'z']

    ciphertext_chars = []
    for i in text:
        #The below finds the index of the plaintext letter, adds it to 65 (A in unicode), converts it to a letter with char()
        ciphered_char = chr(65 + cipher.index(i)) #chr(65) is A; chr(90) is Z
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars) #Passes test.


def decode(encrypted, key):
    cipher = make_cipher(key) #['s', 'e', 'c', 'r', 't', 'k', 'y', 'a', 'b', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'z']

    plaintext_chars = []
    for i in encrypted:
        # For the below: we need to do the reverse of line 22 in encode():
        # 1) find the unicode of the hashed letter
        # 2) subtract 65 from the unicode for the index in the original cipher
        # 3) cipher[index]
        # plain_char = cipher[65 - ord(i)]
        plain_char = cipher[ord(i)-65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)



# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")

