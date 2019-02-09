# Following function generates the 
# key matrix for the key string 
def getKeyMatrix(key, keyMatrix): 
	k = 0
	for i in range(3): 
		for j in range(3): 
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1

# Following function encrypts the message 
def encrypt(messageVector, cipherMatrix, keyMatrix): 
	for i in range(3): 
		for j in range(1): 
			cipherMatrix[i][j] = 0
			for x in range(3): 
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j]) 
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipherEncrypt(message, keyMatrix, messageVector, cipherMatrix):
    for i in range(3): 
        messageVector[i][0] = ord(message[i]) % 65

	# Following function generates 
	# the encrypted vector 
    encrypt(messageVector, cipherMatrix, keyMatrix) 
    
    CipherText = ""
    
    for i in range(3): 
        CipherText += (chr(cipherMatrix[i][0] + 65)) 


    return CipherText



def HillCipherEncryptWrapper(message, key):
    keyMatrix = [[0] * 3 for i in range(3)] 

    # Generate vector for the message 
    messageVector = [[0] for i in range(3)]

    
    # cipherVector = [[0] for i in range(3)] 
    # Generate vector for the cipher 
    cipherMatrix = [[0] for i in range(3)] 

    
    # message = "SYMCA"
	# Get the key 
    # key = "BACABDBAF"
    print (message)

    getKeyMatrix(key, keyMatrix) # For Encryption


    if len(message) <= 0:
        print ('Error. Insufficent length of the message.')
        raise ValueError("Error. Insufficent length of the message.")
    else:
        mod3 = len(message) % 3
        if mod3 != 0:
           message += 'Q' * (3 - mod3)
        message = [message[start:start+3] for start in range(0, len(message), 3)]
    print (message)
    
    ciphertext = ""

    for m in message:    
        ciphertext += HillCipherEncrypt(m, keyMatrix, messageVector, cipherMatrix)
    return ciphertext