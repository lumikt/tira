from trie import Trie
from data_handler import DataHandler

class Generator:

    def __init__(self, source):
        self.trie = MockTrie()
        self.data_handler = DataHandler(source)

    def train(self):
        #DataHandlerin process() avaa kohteen, puhdistaa datan, palauttaa listan sanoja
        #Trie add() lisää sanat listasta, päivittää frekvenssit nodeittain. 
        data = self.data_handler.process()

        for word in data:
            self.trie.add(word)
    

    def generate(self,n=5, degree=1):
        generated_words = []
        # PSEUDOCODE for basic markov chain

        # Create storage for word, list

        #Sequence 1
        #1. Go to starting node
        #   Randomly select starting character
        #       - Weighted by probability of that character occurring
        #   Store character

        #2. Go to selected characters node
        #   Randomly select next character from child list
        #       - Weighted by probability of that character occurring
        #   Store character

        #3. REPEAT nr 2 until "END" character is selected
        
        #4. Add created string to list
        #
        #Repeat Sequence 1 until n words are created
        #Return list of n words to user 

        return generated_words
