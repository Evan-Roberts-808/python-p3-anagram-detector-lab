class Anagram:
    def __init__(self, word):
        self.sorted_word = sorted([letter for letter in word])
        print(self.sorted_word)

    def match(self, word_list):
        return [word for word in word_list if sorted(word) == self.sorted_word]
        