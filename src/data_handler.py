
class DataHandler:

    def __init__(self, source):
        self.source = source
        self.data = []

    def read(self):
        with open(self.source) as file:
            raw_data = file.read()

        return raw_data

    def process(self):

        raw_data = self.read()

        raw_words = raw_data.split()

        #Tekstin käsittely haasteellista, jotain häikkää åäö-merkkien tunnistuksessa ja printtauksessa.
        for words in raw_words:
            clean_word = "".join([c for c in words if c not in "@_!#$%^&*()<>?/|}{~:[]"])
        
            self.data.append(clean_word)
        

        return self.data


