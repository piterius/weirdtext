import unittest
from weirdtext import encode, decode


class WeirdTextTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.main_string = 'This is a long looong test sentence,\nwith some big (biiiiig) words!'
        self.separator = '\n---weird---\n'
        super().__init__(*args, **kwargs)

    def test_main_example_encode_length(self):
        self.assertEqual(len(encode(self.main_string).split(self.separator)[1]), len(self.main_string))

    def test_main_example_decode_length(self):
        self.assertEqual(len(decode(encode(self.main_string))), len(self.main_string))

    def test_main_example_encoded_words(self):
        words = 'long looong sentence some test This with words'
        self.assertEqual(encode(self.main_string).split(self.separator)[2], words)

    def test_main_example_encode_decode(self):
        self.assertEqual(decode(encode(self.main_string)), self.main_string)

    def test_another_example_encode_decode(self):
        string = "Friends will be friends\nWhen you're in need of love they give you care and attention\n" \
                 "Friends will be friends\nWhen you're through with life and all hope is lost\nHold out your hand\n'Cause friends will be friends\nRight 'til the end"
        self.assertEqual(decode(encode(string)), string)


if __name__ == '__main__':
    unittest.main()