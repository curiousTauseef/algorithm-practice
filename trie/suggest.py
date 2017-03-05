import re
from trie import Trie





def parse_words(text):
    return re.findall(r'\w+', text.lower())


with open('big.txt') as f:
    words = parse_words(f.read())


def trie_with_all_words():
    t = Trie()
    for w in words:
        t.add(w)
    return t


if __name__ == '__main__':
    t = trie_with_all_words()
    print(t.lookup('recur'))
