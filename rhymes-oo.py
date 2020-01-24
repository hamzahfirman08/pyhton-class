"""
    File    : rhymes-oo.py
    Author  : Hamzah Firman
    Purpose : The purpose of this program is to find all the words which rhyme with
    some given input word from the user by matching its stressed vowel
    (the primary stress) and phoneme with other words in a file.
    Course  : CSC 120 / section 1A / Spring 2019
    
    """
class Word:
    """
        CLASS: An instance of this class represents a word
    """
    
    def __init__(self, word, pronounce):
        """
            METHOD: This method intializes attitibutes within this class
                    such as 'word' is a string and a collection of (list) of
                    pronounciations for the word.
            PARAMATETS: a.) word - A string of a word b.) pronounce - A list of
                        pronounciations for the word
            RETURNS: None.
            Pre-Condition: word is a string and pronounce is a list of lists
            Post-Condition: None.
                                  
        """
        self._word = word
        self._pronounce = [pronounce]
  
    def add(self, pro):
        """
            METHOD: This method adds pronounciation for the word into a list
            PARAMATETS: a.) pro - A list of pronounciation for the word
            RETURNS: None.
            Pre-Condition: word is a string and pronounce is a list of lists.
            Post-Condition: None.
            
        """
        self._pronounce.append(pro)
 
    def word(self):
        return self._word
 
    def pronounce(self):
        return self._pronounce

    def __eq__(self, word_2):
        """
            METHOD: This method checks if an input word and word from the file
                    , other than input word, form a perfect rhyme when their
                    pre- phoneme (prior to primary stress) are different and
                    both phonemes from primary stress to the end are the same.
            PARAMATETS: a.) word_2 - A string or a new instance
            RETURNS: True if both input word and a word from the
                     file, other than the input word, equal each other or form a
                     perfect rhyme. False otherwise
            Pre-Condition: word is a string and pronounce is a list of strings
            Post-Condition: True will be returned if both words form perfect rhyme
            
        """
        for pron in self._pronounce:
            index_stress = index_finder(pron)
            if index_stress == -1: # No primary stress phoneme
                continue
            if index_stress == 0: # Primary stress phoneme in the beginning
                pre_phon = None # Pre_phon is a phoneme before the primary stress Phoneme
            else:
                pre_phon = pron[index_stress - 1]
            tail = pron[index_stress:] # The rest of phonemes from primary to the end
            for pron2 in word_2._pronounce:
                index_stress2 = index_finder(pron2)
                if index_stress2 == -1:  # No primary stress phoneme
                    continue
                if index_stress2 == 0:   # Primary stress phoneme in the beginning
                    pre_phon2 = None
                else:
                    pre_phon2 = pron2[index_stress2 - 1]
                tail2 = pron2[index_stress2:]
                if pre_phon != pre_phon2 and tail == tail2:
                        return True
        return False


    def __str__(self):
        return "{:d}:{:d}".format(self._word, self._pronounce)


class WordMap:
    """
        CLASS:  An instance of this class represents data structures
                and methods to associate words (strings) with the
                corresponding Word objects
        """
    def __init__(self):
        """
            METHOD: This method initializes a dictionary
            PARAMATETS: None.
            RETURNS: None.
            Pre-Condition: None.
            Post-Condition: None.
            
            """
        self._word_dict = {}
    
    def dict_word(self):
        return self._word_dict
    
    def read_in_pronoun(self):
        """
        METHOD: This method reads in a pronounciation dictionary and use
                this to set the mapping from strings to Word objects
        PARAMATETS: None.
        RETURNS: None.
        Pre-Condition: None.
        Post-Condition: None.
        """
        # Error handles the pronunciation dictionary cannot be read
        try:
            filename = input()
            file = open(filename).readlines()
        except:
            print("ERROR: Could not open file " + filename ) # Error Mesage
            exit(1) # Termination
        for line in file:
            word = line.upper().strip().split()
            the_word = word[0].lower()  # Lower case word
            pronounce = word[1:]        # A list of pronounciation for the word
            if the_word in self._word_dict:                 # Appending/adding into a list
                self._word_dict[the_word].add(pronounce)
            else:                                           # Creating a new Word object
                self._word_dict[the_word] = Word(word, pronounce)

    def read_in_words(self):
        """
            METHOD: This method reads in a word (string) and prints out all
                    the words that rhyme with it
            PARAMATETS: None.
            RETURNS: None.
            Pre-Condition: None.
            Post-Condition: Print out all the words that rhyme with input word
        """
        word_input = input().lower()
        if word_input in self._word_dict:
            word_obj = self._word_dict[word_input]
            for word in self._word_dict:
                if self._word_dict[word] == word_obj:
                    print(word)
        else: # Error when the input word is not in the pronounciation dictionary
            print("ERROR: the word input by the user is not in the pronunciation dictionary " + word_input)




def main():
    """
        FUNCTION: This function calls both WordMap and Word classes
        PARAMATETS: None.
        RETURNS: None.
        Pre-Condition: None.
        Post-Condition: Print out all the words that rhyme with input word
    """
    w = WordMap()
    w.read_in_pronoun()
    w.read_in_words()


def index_finder(pron):
    """
        FUNCTION: This function finds the primary stress phoneme if the pronouciation
                  list of a word.
        PARAMATETS: a.) pron - A list of pronounciation of the word.
        RETURNS: The index i will be return if a primary stress is found and -1,
                the last index element of the list,otherwise.
        Pre-Condition: Pron is a list of list .
        Post-Condition: The returns values are index i (if a primary stress is found) and
                        -1 otherwise
    """
    
    for i in range(len(pron)):
        if '1' in pron[i]: # A primary stress phoneme is found
            return i       # Index
    return -1 # Last element of the list

main()
