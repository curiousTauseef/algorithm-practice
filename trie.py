from collections import defaultdict


def create_dict():
    return defaultdict(create_dict)


class Trie(object):
    def __init__(self):
        self.trie = {}

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
