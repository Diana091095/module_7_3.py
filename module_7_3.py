class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                all_words[name] = file.read().lower().split()
        return all_words

    def find(self, word):
        all_words2 = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                all_words2[name] = words.index(word.lower())+1
        return all_words2

    def count(self, word):
        all_words3 = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                all_words3[name] = words.count(word.lower())
        return all_words3


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего