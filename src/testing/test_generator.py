import unittest

from generator import Generator

TEST_CONTENT = ["alkometri",
                "banaani",
                "couscous",
                "diletantti",
                "ensikertalainen",
                "faarao",
                "graafikko",
                "hitsaaja",
                "insinööri",
                "joukkue",
                "kerhotila",
                "luokkakokous",
                "mansikka",
                "noukkia",
                "ostoslista",
                "paviaani",
                "quisling",
                "rakkaus",
                "sydänvärinä",
                "torvi",
                "universaali",
                "vauhdikas",
                "wokki",
                "xylofoni",
                "ympäristöystävällinen",
                "zebra",
                "ångström",
                "ärjyä",
                "örkki"]

class GeneratorTest(unittest.TestCase):

    def setUp(self):
        self.degree = 3

        self.generator = Generator("placeholder_file_path.txt", self.degree, 8)
        
        for word in TEST_CONTENT:
            self.generator.trie.add(word)

    
    def test_generation_length(self):

        generated_words = self.generator.generate(5)

        self.assertEqual(5, len(generated_words))

    def test_generated_words_length(self):

        generated_words = self.generator.generate(100)

        words_long_enough = True

        for word in generated_words:
            if len(word) != 8:
                words_long_enough = False
                break
        
        self.assertTrue(words_long_enough)

    def test_generation_sequence_validity(self):

        words = self.generator.generate(20)

        allowed_sequences = "".join(TEST_CONTENT)

        for word in words:
            for i in range(0,len(words)+1-self.degree):
                self.assertTrue(word[i:i+self.degree] in allowed_sequences)

    
    def test_no_infinite_loop(self):

        generator = Generator("placeholder_file_path.txt", 4, 8)
        for word in ["too", "short"]:
            generator.trie.add(word)
        
        return_error_msg = generator.generate(1000)

        correct_error_msg = ["Too many iterations, generation aborted.\n",
                "Please try changing either degree or word amount.", 
                "It appears the training dataset doesn't contain \nenough words for your desired generation."]

        self.assertEqual(return_error_msg, correct_error_msg)