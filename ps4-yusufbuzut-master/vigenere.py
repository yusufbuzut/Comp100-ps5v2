import string


### HELPER CODE ###
def load_words(file_name):
    '''
  file_name (string): the name of the file containing
  the list of words to load

  Returns: a list of valid words. Words are strings of lowercase letters.

  Depending on the size of the word list, this function may
  take a while to finish.
  '''
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    return wordlist


def is_word(word_list, word):
    '''
  Determines if word is a valid word, ignoring
  capitalization and punctuation

  word_list (list): list of words in the dictionary.
  word (string): a possible word.

  Returns: True if word is in word_list, False otherwise

  For Example: is_word(word_list, 'bat') returns True
  and is_word(word_list, 'asdf') returns False
  '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        '''
    Initializes a Message object

    text (string): the message's text

    a Message object has two attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
    '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
          #delete this line and replace with your code here

    def get_message_text(self):
        '''
    Used to safely access self.message_text outside of the class
    Returns: self.message_text
    '''

        return self.message_text
        #delete this line and replace with your code here

    def get_valid_words(self):
        '''
    Used to safely access a copy of self.valid_words outside of the class.
    This helps you avoid accidentally mutating class attributes.

    Returns: a COPY of self.valid_words
    '''

        return self.valid_words.copy()
          #delete this line and replace with your code here

    def shift_letter(self, letter, key):
        '''
    letter (string of length 1)
    key (an integer)
    shifts the letter by key and returns the shifted letter
    '''
        lowerletters = string.ascii_lowercase * 2
        upperletters = string.ascii_uppercase * 2
        punctuation = list(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        if letter in lowerletters[:26]:
            letter2 = lowerletters[lowerletters.index(letter) + key]
        if letter in upperletters[:26]:
            letter2 = upperletters[upperletters.index(letter) + key]
        if letter in punctuation:
            letter2 = letter
        return letter2

        #delete this line and replace with your code here

    def apply_vigenere(self, key):
        '''
    Applies the Vigenere Cipher to self.message_text with the input key.
    Creates a new string that is self.message_text such that each letter
    has been shifted by some number of characters determined by key.
    Uses the shift_letter method above.

    key (list of integers): the key to encrypt the message.

    Returns: the message text (string) encrypted by key
    '''
        encrypted_message = []
        for i, let in enumerate(self.message_text):
            let2 = self.shift_letter(let, (key[i % len(key)]))
            encrypted_message.append(let2)
        return ''.join(encrypted_message)
        #delete this line and replace with your code here


class PlaintextMessage(Message):
    def __init__(self, text, key):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        key (list of integers): the key associated with this message

        A PlaintextMessage object inherits from Message and has four attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.key (list of integers, determined by input key)
            self.message_text_encrypted (string, created using self.message_text and self.key)

        '''
        Message.__init__(self,text)
        
        self.message_text_encrypted =self.apply_vigenere(key)
        self.key = key

          #delete this line and replace with your code here

    def get_key(self):
        '''
    Used to safely access self.key outside of the class

    Returns: a COPY of self.key
    '''
        return self.key  #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
    Used to safely access self.message_text_encrypted outside of the class
    Returns: self.message_text_encrypted
    '''
        return self.message_text_encrypted  #delete this line and replace with your code here

    def change_key(self, key):
        '''
    Changes self.key of the PlaintextMessage and updates other
    attributes determined by key.

    key (list of integers): the new key that should be associated with this message.

    Returns: nothing
    '''
         
        self.message_text_encrypted =self.apply_vigenere(key)
        self.key = key  #delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
    Initializes a CiphertextMessage object

    text (string): the message's text

    a CiphertextMessage object has two attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
    '''
        
        Message.__init__(self,text)
     
       #delete this line and replace with your code here

    def decrypt_message(self):
        '''
      Decrypt self.message_text by trying every possible key value
      and find the "best" one. We will define "best" as the key that
      creates the maximum number of real words when we use apply_vigenere(key)
      on the message text. If [k0, k1, k2, ...] is the original key used to
      encrypt the message, then we would expect [26-k0, 26-k1, 26-k2,...] to
      be the best key for decrypting it.

      IMPORTANT NOTE1: FOR THIS PART, ONLY CONSIDER THE KEYS WITH LENGTH UP TO 3. ALSO ASSUME THAT EACH VALUE IN THE KEY IS NOT GREATER THAN 12.
      OTHERWISE IT WILL TAKE VERY VERY LONG TIME TO FINISH.

      IMPORTANT NOTE2: RETURN THE SHORTEST FORM OF A KEY. FOR EXAMPLE THE KEYS
      [2,2,2] AND [2] ARE EQUAL. AND IN SUCH CASES YOU SHOULD RETURN THE SHORTER
      ONE.

      Note: if multiple keys are equally good such that they all create
      the maximum number of valid words, you may choose any of those key
      (and their corresponding decrypted messages) to return

      Returns: a tuple of the best key used to decrypt the message
      and the decrypted message text using that key
      '''
        word_list = self.get_valid_words()
        decryptedmessage = []
        decryptedmessage2 = []
        possible=[]
        for s in range (14,26):
          for y in range (14,26):
            for z in range (14,26):
              possible.append((s,y,z))
        for i in possible:
          decrypted= self.apply_vigenere(i)
          dewords= decrypted.split()
          for word in dewords:
            if is_word(word_list,word):
              decryptedmessage.append(1)
            else:
              decryptedmessage.append(0)
          decryptedmessage2.append((sum(decryptedmessage),i,decrypted))
          del decryptedmessage[0:len(decryptedmessage)]
        best_key=max(decryptedmessage2)
        answer= best_key[1]
        message= best_key[2]
        answer3=list(answer)
        answer2=[]
        for i in answer3:
          answer2.append(26-i)
        if answer2[0]==answer2[1]==answer2[2]:
          
          
          return ([answer2[0]],message)
        else:

          return (answer2,message)
      
      
      
      
      
        
        #delete this line and replace with your code here


if __name__ == '__main__':
    '''
  Can you find out what this hidden message says?
  Uncomment the next lines to find out!
  '''
    # ciphertext = CiphertextMessage('"Drmu spna vwvu bz ay nbmhd zmqlxbpcbz boo dkg dpli ky ay nbmhd teapmqhxa kvk ijdwyc, mqcstpjiaswu epvt tctz ay arm xmed sodlv" [Jysiu Oyomuo]')
    # decrypted = ciphertext.decrypt_message()
    # print(decrypted[1])
    pass
