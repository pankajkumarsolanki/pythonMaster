import string


def encrypt(text, shift):
    originalMessage = list(text.lower())

    #Shifted Version of the alphabets
    alphabet = string.ascii_lowercase
    newalphabet = list(alphabet[shift:] + alphabet[:shift])
    newallist=list(newalphabet)

    newMessage = []
    for a in originalMessage:
        if a not in alphabet:
        # if we want only the space to be considered(skip punctuations), then just replace "a not in alphabet" above with 'a == '''
            newMessage.append(a)
        else:
            for n in newallist:
                if a == n:
                    index=alphabet[newallist.index(n)]
                    newMessage.append(index)
    encryptedMessage = (''.join(newMessage))
    return encryptedMessage


