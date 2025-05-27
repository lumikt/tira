from numpy import random as npr
from trie import Trie
from data_handler import DataHandler

class Generator:

    def __init__(self, source, degree = 2):
        self.trie = Trie(degree)
        self.data_handler = DataHandler(source)
        self.degree = degree

    def train(self):
        #DataHandlerin process() avaa kohteen, puhdistaa datan, palauttaa listan sanoja
        #Trie add() lisää sanat listasta, päivittää frekvenssit nodeittain. 
        data = self.data_handler.process()

        for word in data:
            self.trie.add(word)
    

    def generate(self,n=5):
        #TODO: Split & clean up function. Working version 1.

        generated_words = []
        words_to_generate = n
        DESIRED_WORD_LENGTH = 10 #TEMPORARY CONST

        while words_to_generate > 0:
            word = ""
            starting_nodes = []
            total_count_of_characters = 0    

            selection_nodes = []
            selection_freqs = []
            node_freq = 0
            
            for key, node in self.trie.starting_node.children.items():
                starting_nodes.append(node)
                total_count_of_characters +=node.frequency     

            for node in starting_nodes:
                selection_freqs.append(round(node.frequency/total_count_of_characters,4))
                selection_nodes.append((node.value))


            test = npr.multinomial(1, selection_freqs, size=1)

            for i in range(0, len(test[0])):
                if test[0][i] == 1:
                    word += selection_nodes[i]

            
            while len(word) < DESIRED_WORD_LENGTH:
                word_length = len(word) 
                
                if len(word) >= self.degree:
                    search_key = word[word_length-self.degree:]
                else:
                    search_key = word

                node = self.trie.search(search_key)
                if not node or node.children == {}:
                    break
                
                available_nodes = []
                selection_nodes = []
                selection_freqs = []
                
                node_freq = 0

                for key, node in node.children.items():
                    available_nodes.append(node)
                    total_count_of_characters +=node.frequency     

                for node in available_nodes:
                    selection_freqs.append(round(node.frequency/total_count_of_characters,4))
                    selection_nodes.append((node.value))


                test = npr.multinomial(1, selection_freqs, size=1)

                for i in range(0, len(test[0])):
                    if test[0][i] == 1:
                        word += selection_nodes[i][-1:]

            if len(word)< DESIRED_WORD_LENGTH:
                continue
            generated_words.append(word)
            words_to_generate -=1
            
        #print(test)
        return generated_words

if __name__ == "__main__":
    print("Dev testing:\n")
    print()

    test = Generator(3)
    test.trie.add("kaikkivoipa")
    test.trie.add("asiaa")
    test.trie.add("tervahammas")
    test.trie.add("sekalainen")
    test.trie.add("asianhaara")
    test.trie.add("kukkanen")
    #test.trie.add("elämä")
    test.trie.add("tappava")
    #test.trie.add("turvasatama")
    #test.trie.add("eläkeläinen")

    #print(test.trie.starting_node)
    #print(test.trie.search(""))
    words = test.generate(20)
    for word in words:
        print(word)