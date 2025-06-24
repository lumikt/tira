import unittest

from trie import Trie,Node

class TrieTest(unittest.TestCase):

    def setUp(self):
        self.trie = Trie(3)

    
    def test_trie_adding_single_character(self):
        self.trie.add("w")

        self.assertTrue("w" in self.trie.starting_node.children)


    def test_trie_search(self):
        self.trie.add("w")
        node = self.trie.search("w").value

        self.assertEqual("w", node)


    def test_trie_adding_a_word(self):
        self.trie.add("triumphant")
        test_case = self.trie.search("tri")

        self.assertNotEqual(None,test_case)
    

    def test_trie_search_multiple_nodes(self):
        trie = Trie(3)

        trie.add("super")
        trie.add("alakazam")
        trie.add("downpour")
        trie.add("excited")

        self.assertEqual(trie.search("ala").value, "ala")
        self.assertEqual(trie.search("pou").value, "pou")
        self.assertEqual(trie.search("exc").value, "exc")
        self.assertEqual(trie.search("per").value, "per")
        self.assertEqual(trie.search("dow").value, "dow")
    

    def test_trie_variable_degrees(self):
        word = "califragilisticexpialidocious"
        its_ok = True
        for i in range(1,10):
            trie = Trie(i)
            trie.add(word)

            node = trie.search(word[0:i])
            if node == None:
                its_ok = False
                break
        
        self.assertTrue(its_ok)


    def test_trie_frequency_updates(self):

        trie = Trie(3)

        trie.add("sunset")

        node_freq = trie.search("sun").frequency
        self.assertEqual(1,node_freq)
        
        trie.add("sunset")
        trie.add("sunset")

        node_freq = trie.search("sun").frequency
        self.assertEqual(3,node_freq)


    def test_trie_structure(self):
        trie = Trie(2)
        trie.add("sunset")
        trie.add("testset")
        trie.add("sunlight")

        nodes = []
        node = trie.starting_node

        correct_string = ['', 's', 'su', 'sun', 'se', 'set', 'st', 'sts', 'u', 'un', 'uns', 'unl',
            'n', 'ns', 'nse', 'nl', 'nli', 'e', 'et', 'es', 'est', 't', 'te', 'tes', 'ts', 'tse', 'l',
            'li', 'lig', 'i', 'ig', 'igh', 'g', 'gh', 'ght', 'h', 'ht']


        self.print_helper(node,nodes)
        self.assertEqual(nodes, correct_string)

        correct_node_amount = 37
        self.assertEqual(len(nodes), correct_node_amount)    
    

    def print_helper(self, node, nodes):
        nodes.append(node.value)

        if node.children == {}:
            return 
        
        for child in node.children:
            self.print_helper(node.children[child], nodes)        

        return