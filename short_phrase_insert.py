import pytest

class TestPhraseLength:
    def test_phrase_len(self):
        phrase = input("Set a phrase: ")
        j = len(phrase)

        assert j<15, "phrase is more then 15 characters"
        # if j < 15:
        #     print(f"phrase lenh")
        # else:
