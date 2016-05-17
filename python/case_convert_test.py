import unittest
import case_convert


class Conversion(unittest.TestCase):
    def test_snake_to_camel(self):
        word = case_convert.snake_to_camel('snake_case')
        assert word == 'SnakeCase'

    def test_camel_to_snake(self):
        word = case_convert.camel_to_snake('CamelCase')
        assert word == 'camel_case'

    def test_normalize_to_list(self):
        word = case_convert.normalize_to_list('snake_case')
        assert word == ['snake', 'case']

    def test_word_list_to_snake(self):
        word = case_convert.word_list_to_snake(['camel', 'case'])
        assert word == 'camel_case'

    def test_word_list_to_camel(self):
        word = case_convert.word_list_to_camel(['happy', 'day'])
        assert word == 'HappyDay'

    def test_word_list_to_kebab(self):
        word = case_convert.word_list_to_kebab(['more', 'testing'])
        assert word == 'more-testing'

    def test_word_list_to_constant(self):
        word = case_convert.word_list_to_constant(['you', 'can\'t', 'handle', 'the', 'testing'])
        assert word == 'YOU_CAN\'T_HANDLE_THE_TESTING'
