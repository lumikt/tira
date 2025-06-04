import io

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

        #Tekstin käsittely haasteellista, jotain häikkää åäö-merkkien tunnistuksessa ja printtauksessa.
        for words in raw_words:
            clean_word = "".join([c for c in words if c not in "0123456789 -.,@_!#$%^&*()<>?/|}{~:[]"])
            if clean_word == "":
                continue
            self.data.append(clean_word.lower())
        

        return self.data

