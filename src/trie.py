#Work in progress, aikainen hahmotelma rakenteesta.


#Luokka nodelle joka tallentaa tiedot omista lapsistaan ja niiden suhteellisista esiintymiskerroista.
class Node:

    def __init__(self, character):
        self.value = character
        self.children = {} #dict jossa key on merkki ja arvo on suhteellinen yleisyys?
        pass


    def add(self, character):
        '''
        Assign children to the trie node as a tuple containing the child node and its frequency.
        '''

        pass


    def calculate_frequency(self):
        pass


#Luokka joka luo trie rakenteen alkaen tyhjästä alkunodesta, käyttäen hyväkseen Node luokkaa.
class Trie:
    def __init__(self):
        self.starting_node = Node('')


    def add(self, word):
        starting_character = word[0]

        if starting_character not in self.starting_node.children:
            self.starting_node.add(starting_character)

        for i in range(1, len(word)):
            node = self.search(word[i-1])

            node.add(word[i])
            
            
        pass

    def search(self,search_value, node):

        if node.value == search_value:
            return node

