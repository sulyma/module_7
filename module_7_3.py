import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                words = []
                for line in f:
                    cleaned_line = line.lower().translate(str.maketrans('', '', string.punctuation))
                    words.extend(cleaned_line.split())
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        positions = {}

        for file_name, words_list in all_words.items():
            if word in words_list:
                positions[file_name] = words_list.index(word) + 1

        return positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        counts = {}

        for file_name, words_list in all_words.items():
            counts[file_name] = words_list.count(word)
        return counts


