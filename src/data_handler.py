import io
from string import ascii_lowercase
class DataHandler:

    def __init__(self, source):
        self.source = source
        self.data = []

    def read(self):
        '''
        Handles opening and reading the source file.
        '''

        with io.open(self.source,"r", encoding="utf-8") as file:
            raw_data = file.read()

        return raw_data

    def process(self):
        '''
        Processes the given file into a list of words, separated by spaces. Removes non-letter characters.
        '''

        raw_data = self.read()

        raw_words = raw_data.split()

        # Sets allowed chars to full list of ascii (english alphabet) + åäö to allow
        # populating with finnish words.
        allowed_chars = ascii_lowercase
        allowed_chars += "åäö"
        
        # Clean the words from any extra characters and assign them to lower case

        for words in raw_words:
            lower_case_word = words.lower()
            clean_word = "".join([c for c in lower_case_word if c in allowed_chars])
            if clean_word == "":
                continue
            self.data.append(clean_word.lower())
        
        # Return a list of words to populate the trie with
        return self.data

