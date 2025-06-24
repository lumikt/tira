import unittest
from unittest.mock import Mock

from data_handler import DataHandler


class DataHandlerTest(unittest.TestCase):

    def setUp(self):
        self.datahandler = DataHandler("string_placeholder.txt")


    def test_text_clean(self):

        string_to_clean = '''ab´|<>cD[e2    33FgHijk@££lmnO PQ ££   Rstu@£VW xyZ$@Å3Ä"ö#'''

        correct_list = ["abcde", "fghijklmno", "pq", "rstuvw", "xyzåäö"]

        self.datahandler.read = Mock(return_value = string_to_clean)

        cleaned_string = self.datahandler.process()
    
        self.assertEqual(cleaned_string, correct_list)
