import random
import string


class Encryption():

    def __init__(self, seed):

        # Set a random seed and a self.seed attribute
        random.seed(seed)
        self.seed = seed

        # Create an empty string attribute to hold the encrypted phrase
        self.encrypted_phrase = ''

        # Use the string and random libraries to create two attributes
        # One is the correct alphabet, another is a shuffled alphabet (hint: random.sample())
        self.true_alphabet = list(string.ascii_lowercase)
        self.rand_alphabet = random.sample(self.true_alphabet, len(self.true_alphabet))

    def encryption(self, message):
        '''
        This method will take in a string message and encrypt it. Check the video or 
        the instructions above in the markdown for full description of how your
        decryption method should work.

        '''
        output = ''

        ################################################################
        ### STEP 1: REPLACE EVERY OTHER LETTER WITH A RANDOM LETTER ###
        ##############################################################

        for i in range(len(message)):
            output += message[i]
            output += random.sample(self.true_alphabet, 1)[0]

        #################################################
        ### STEP 2: REVERSE THE STRING  ################
        ###############################################
        self.encrypted_phrase = output[::-1]

        ##########################################################################
        ##### STEP 3: USE THE RANDOM SHUFFLED ALPHABET FOR A CEASER CIPHER ######
        ########################################################################

        encrypted_phase_two = list(range(len(self.encrypted_phrase)))

        for i, letter in enumerate(self.encrypted_phrase.lower()):

            if letter in self.true_alphabet:
                index = self.true_alphabet.index(letter)
                encrypted_phase_two[i] = self.rand_alphabet[index]

            else:
                encrypted_phase_two[i] = letter

        self.encrypted_phrase = ''.join(encrypted_phase_two)

        return self.encrypted_phrase

    def decryption(self, message, seed):
        '''
        This method takes in a messsage and a seed for the random shuffled alphabet.
        It then returns the decrypted alphabet.
        '''

        random.seed(seed)
        session_rand_alphabet = random.sample(self.true_alphabet, len(self.true_alphabet))

        decrypted_message = list(range(len(message)))

        # First undo the randomized ceaser cipher
        for i, letter in enumerate(message.lower()):

            if letter in self.true_alphabet:
                index = session_rand_alphabet.index(letter)
                decrypted_message[i] = self.true_alphabet[index]

            else:
                decrypted_message[i] = letter

        # Join back list into a string
        decrypted_message = ''.join(decrypted_message)[::-1][::2]

        return decrypted_message