
class Trie(object):
    def __init__(self, trie=None):
        self.trie = trie or {}

    def add(self, term):
        def recursive_add(tree, term):
            if not term:
                return
            node = tree.setdefault(term[0], {})
            if len(term) == 1:
                node['$'] = None
            else:
                recursive_add(node, term[1:])
        recursive_add(self.trie, term)

    def lookup(self, prefix):
        node = self.trie
        for c in prefix:
            if c in node:
                node = node[c]
            else:
                return []
        return [prefix + w for w in Trie(node).allwords()]

    def allwords(self):
        if not self.trie:
            return []
        else:
            words = [''] if '$' in self.trie else []
            return words + [
                k + w
                for k in self.trie
                for w in Trie(self.trie[k]).allwords()
            ]
