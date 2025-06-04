from random import randint
from trie import Trie
from data_handler import DataHandler

class Generator:

    def __init__(self, source, degree:int = 2, word_length:int = 8):
        self.trie = Trie(degree)
        self.data_handler = DataHandler(source)
        self.degree = degree
        self.word_length = word_length

    def train(self):
        """
        Commits the training data to the trie structure and updates the trie node frequencies.
        """
        #DataHandlerin process() avaa kohteen, puhdistaa datan, palauttaa listan sanoja
        #Trie add() lisää sanat listasta, päivittää frekvenssit nodeittain. 
        data = self.data_handler.process()

        for word in data:
            self.trie.add(word)

    def choose(self, nodes:dict):
        """
        Chooses the following character based on given node dictionary based on frequency of the character.
        Args:
            nodes (dict): a dictionary of Node-type objects.
        """

        total_weight_of_nodes = 0
        selection_ranges = {}

        # Assigning to the selection_range dict each node value, a string, as key value and
        # the selection range as a tuple, as value.
        # Calculate total weight of the nodes to have a selection range.
          
        for key, node in nodes.items():
            selection_ranges[node.value] = (total_weight_of_nodes+1, total_weight_of_nodes+node.frequency)
            total_weight_of_nodes += node.frequency
        
        # Randomly choose an integer in the range of 1 to the total weight of nodes, to use
        # as weighted random sampling.

        choice = randint(1, total_weight_of_nodes)
        
        # Select the matching key (a string) in which the selection range matches. E.g. if choice is 1 (out of 1-10),
        # we select the key that has the matching selection range, e.g. (1,3) as 1<= 2 <= 3.
        # Return the last character of the string, e.g. if string is "eac" in a 2 degree chain, the selected
        # character is "c" as it follows from the previous states "ea", so we return "c".

        for key, node in selection_ranges.items():
            if node[0] <= choice <= node[1]:
                character = key
                return character[-1:]
        

    def generate(self,n:int=5):
        """
        Generates a list of words using a Markov chain.
        Args: 
            n (int): the n number of words to be returned, default is 5.
        """
        generated_words = []
        words_to_generate = n
        desired_word_length = self.word_length 

        while words_to_generate > 0:
            word = ""
            
            while len(word) < desired_word_length:
   
                if len(word) >= self.degree:
                    #If the length of the string is sufficient for full utilization of Markov
                    #degree, we use that string to search for candidates for following character,
                    # e.g. in a 2 degree Markov chain we would search with two characters.

                    search_key = word[len(word)-self.degree:]

                else:
                    # If the string is not long enough for full Markov degree utilization, we
                    # use the whole string as a search parameter. If the string is empty, trie.search()
                    # returns the starting node of the trie

                    search_key = word
                
                node = self.trie.search(search_key)

                #If there are no children for the current search key, we abort the 
                # generation and start over as we can't select the next character.
                # More common in shorter training datasets and high degree chains.
                if not node or node.children == {}:
                    break

                # Send node children to choose() which selects the following character
                word += self.choose(node.children)
   
            # Check if the generated string matches specifications and is not a duplicate.
            if (word in generated_words) or (len(word) < desired_word_length):
                continue

            generated_words.append(word)
            words_to_generate -=1
            
        return generated_words

if __name__ == "__main__":
    print("Dev testing:\n")
    print()

    test = Generator("testing.txt", 3)
    test.trie.add("kaikkivoipa")
    test.trie.add("asiaa")
    test.trie.add("tervahammas")
    test.trie.add("sekalainen")
    test.trie.add("asianhaara")
    test.trie.add("kukkanen")
    #test.trie.add("elämä")
    test.trie.add("tappava ")
    #test.trie.add("turvasatama")
    #test.trie.add("eläkeläinen")

    #print(test.trie.starting_node)
    #print(test.trie.search(""))
    #print(test.trie.starting_node)
    words = test.generate(2)
    
    for word in words:
        print(word)