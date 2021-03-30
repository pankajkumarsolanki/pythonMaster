import enCrypt
import deCrypt

#Ceaser Cipher
Message = 'Get this message to the main server!'
shift = 13

print("Original Message: "+Message)

encryptedMessage = enCrypt.encrypt(Message, shift)
print("Encrypted Message: " + encryptedMessage)

decryptedMessage = deCrypt.decrypt(encryptedMessage, shift)
print("Decrypted Message: "+decryptedMessage)

#When shift range is not supplied
for i in range(0, 27):
    print("Using Shift Value: {}".format(i))
    print("Decrypted Message: "+deCrypt.decrypt(encryptedMessage,i))
    print("\n")


print(range(len(Message)))