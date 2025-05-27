#Work in progress, aikainen hahmotelma rakenteesta.


#Luokka nodelle joka tallentaa tiedot omista lapsistaan ja niiden suhteellisista esiintymiskerroista.
class Node:

    def __init__(self, character):
        self.value = character
        self.children = {} #dict jossa key on merkki ja arvo on suhteellinen yleisyys?
        self.frequency = 1

    def add(self, node):
        '''
        Assign children to the trie node as a tuple containing the child node and its frequency.
        '''

        self.children[node.value]=(node)

        return True


    def __str__(self):
        return f'Node: "{self.value}" with frequency {self.frequency}, children are {self.children}'
    
    def __repr__(self):
        return f'Node({self.value})'

#Luokka joka luo trie rakenteen alkaen tyhjästä alkunodesta, käyttäen hyväkseen Node luokkaa.
class Trie:
    def __init__(self, degree = 2):
        mock_active = False
        self.starting_node = Node('')
        self.degree = degree
        if mock_active:
            self.starting_node.add(Node("f"))
            self.starting_node.children["f"].add(Node("fo"))
            self.starting_node.children["f"].add(Node("fa"))
            self.starting_node.children["f"].children["fa"].add(Node("far"))

            self.starting_node.children["f"].children["fo"].add(Node("foo"))
            self.starting_node.children["f"].children["fo"].add(Node("foz"))


            self.starting_node.add(Node("b"))
            self.starting_node.children["b"].add(Node("ba"))
            self.starting_node.children["b"].children["ba"].add(Node("bar"))

    def add(self, word):

        for i in range(0,len(word)):
            new_node = word[i:i+self.degree+1]

            node = self.search(new_node[0])

            if not node:
                self.starting_node.add(Node(new_node[0]))
            else:
                #Update freq in node
                node.frequency += 1
            
            
            for j in range(1,len(new_node)):
                node_key = new_node[0:j]
                found_node = self.search(node_key)
                
                
                node_to_add = new_node[0:j+1]

                if node_to_add in found_node.children:
                    #To update freq in future
                    found_node.children[node_to_add].frequency += 1                    
                else:
                    found_node.add(Node(node_to_add))
            
            
    def search(self, key):

        node = self.search_helper(key, self.starting_node)

        return node

    def search_helper(self, key, node):

        if key in node.children:
            return node.children[key]


        for i in range(1, len(key)):
            if key[0:i] in node.children:
                return self.search_helper(key, node.children[key[0:i]])
        return None





    def __str__(self):
        return f'{self.starting_node}'


if __name__ == "__main__":
    print("Dev testing:\n")


    
    trie_test = Trie(3)

    trie_test.add("super")

    trie_test.add("succor")
    trie_test.add("sunset")
    trie_test.add("sundown")
    trie_test.add("ksuspop")

    print(trie_test.search("sund"))
    print(trie_test.search("su"))
    print(trie_test.search("s"))
    print(trie_test.search("k"))

