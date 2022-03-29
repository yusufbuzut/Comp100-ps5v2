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

  Example:
  >>> is_word(word_list, 'bat') returns
  True
  >>> is_word(word_list, 'asdf') returns
  False
  '''
  word = word.lower()
  word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
  return word in word_list


### END HELPER CODE ###


WORDLIST_FILENAME = 'words.txt'

def get_permutations(sequence):
  '''
  sequence (string): a string
  returns all permutations of sequence in a list
  
  You CAN use your code from the PS3.5
  '''
  if len(sequence) == 1:
        return [sequence]
  list = []
  for i, letter in enumerate(sequence):
        for y in get_permutations(sequence[:i]+sequence[i+1:]):
            list = list + [letter + y]
  return list #delete this line and replace with your code here


class SubMessage(object):
  def __init__(self, text):
    '''
    Initializes a SubMessage object
            
    text (string): the message's text

    A SubMessage object has two attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
    '''
    self.message_text = text
    self.valid_words = load_words(WORDLIST_FILENAME) #delete this line and replace with your code here
  
  def get_message_text(self):
    '''
    Used to safely access self.message_text outside of the class
    
    Returns: self.message_text
    '''
    return self.message_text #delete this line and replace with your code here

  def get_valid_words(self):
    '''
    Used to safely access a copy of self.valid_words outside of the class.
    This helps you avoid accidentally mutating class attributes.
    
    Returns: a COPY of self.valid_words
    '''
    return self.valid_words.copy() #delete this line and replace with your code here
              
  def build_transpose_dict(self, letters_permutation):
    '''
    letters_permutation (string): a string containing a permutation of letters (e, t, a, o, i, n)
    
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to an
    uppercase and lowercase letter, respectively. (e, t, a, o, i, n) are shuffled 
    according to letters_permutation. The first letter in letters_permutation 
    corresponds to e, the second to t, and so on in the order e, t, a, o, i, n.
    The other letters remain the same. The dictionary should have 52 
    keys of all the uppercase letters and all the lowercase letters.

    Example: When input "anotei":
    Mapping is e->a, t->n, a->o, o->t, i->e, n->i
    and "Nice To Meet You!" maps to "Ieca Nt Maan Ytu!"

    Returns: a dictionary mapping a letter (string) to 
              another letter (string). 
    '''
    lowerletters = string.ascii_lowercase 
    upperletters = string.ascii_uppercase
    x="etaoin"
    y="ETAOIN"
    punc = list(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    dictionary={}
    for i,letter in enumerate(letters_permutation.lower()):
        dictionary[x[i]]= letter
    for i,letter in enumerate(letters_permutation.upper()):
        dictionary[y[i]]= letter
    for letter in lowerletters:
      if letter not in letters_permutation.lower():
        dictionary[letter]=letter
    for letter in upperletters:
      if letter not in letters_permutation.upper():
        dictionary[letter]=letter
    for i in punc:
      dictionary[i]= i 
    
    return dictionary #delete this line and replace with your code here
  
  def apply_transpose(self, transpose_dict):
    '''
    transpose_dict (dict): a transpose dictionary
    
    Returns: an encrypted version of the message text, based 
    on the dictionary
    '''
    encryptedmessage =[]
    for letter in self.message_text:
      encryptedmessage.append(transpose_dict[letter])
    
    return ''.join(encryptedmessage) #delete this line and replace with your code here

  def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
  
        if type(self) == type(other):
            return self.message_text == other.message_text \
                   and self.valid_words == other.valid_words
        else:
            return False   #delete this line and replace with your code here
      
class EncryptedSubMessage(SubMessage):
  def __init__(self, text):
    '''
    Initializes an EncryptedSubMessage object

    text (string): the encrypted message text

    An EncryptedSubMessage object inherits from SubMessage and has two attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
    '''
    SubMessage.__init__(self,text) #delete this line and replace with your code here
  
  def decrypt_message(self):
    '''
    Attempt to decrypt the encrypted message 
    
    Idea is to go through each permutation of the 'etaoin' and test it
    on the encrypted message. For each permutation, check how many
    words in the decrypted text are valid English words, and return
    the decrypted message with the most English words.
    
    If no good permutations are found (i.e. no permutations result in 
    at least 1 valid word), return the original string. If there are
    multiple permutations that yield the maximum number of words, return any
    one of them.

    Returns: the best decrypted message    
    '''
    transpose_dict_list=[]
    mssglist=[]
    permutationslist= get_permutations("etaoin")
    for i in permutationslist:
      transpose_dict_list.append(self.build_transpose_dict(i))
    for d in transpose_dict_list:
      encrypted= self.apply_transpose(d)
      mssglist.append(encrypted)
    

    word_list = self.get_valid_words()
    yusuf = []
    büzüt = []
    for message in mssglist:
          messagewords= message.split()
          for word in messagewords:
            if is_word(word_list,word):
              yusuf.append(1)
            else:
              yusuf.append(0)
          büzüt.append((sum(yusuf),message))
          del yusuf[0:len(yusuf)]
    bestsentence=max(büzüt)
    possiblemessage=[]
    for tuples in büzüt:
      if tuples[0]== bestsentence[0] and tuples[1] not in possiblemessage:
        possiblemessage.append(tuples[1])
    realmessage=''
    for y in possiblemessage:
      realmessage= realmessage+','+y
    return realmessage[1:]

    
     #delete this line and replace with your code here
  
  def __eq__(self, other):
    
        if not isinstance(other, type(self)):
            return NotImplemented
        
        if type(self) == type(other):
            return self.message_text == other.message_text \
                   and self.valid_words == other.valid_words
        else:
            return False#delete this line and replace with your code here
    

if __name__ == '__main__':
  '''
  Can you find out what this hidden message says?
  Uncomment the next lines to find out!
  '''
  # encrypted = EncryptedSubMessage('We re iryotg in prnve nurselves wrntg as quockly as pnssoble, because ntly ot ihai way cat we fotd prngress.  [Rochard Feytmat]')
  # print(encrypted.decrypt_message())

  pass