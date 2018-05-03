class Node():
    def __init__(self, c=None, word=None):
        self.c = c
        self.word = word
        self.childs = []


class Trie():
    def __init__(self):
        self.root = Node()


    def findc(self, node, c):
        childs = node.childs
        len_ = len(childs)
        if len_ == 0:
            return -1
        for i in range(len_):
            if childs[i].c == c:
                return i

        return -1

    # add a word to the tree
    def add(self, word):
        node = self.root
        for c in word:
            pos = self.findc(node, c)

            if pos < 0:
                node.childs.append(Node(c))
                node.childs.sort(key=lambda child: child.c, reverse=False)

                pos = self.findc(node, c)
            node = node.childs[pos]
        node.word = word

    def preOrder(self, node):
        result = []
        if node.word:
            result.append(node.word)

        for child in node.childs:
            result.extend(self.preOrder(child))

        return result

    def search(self, node, word):
        result = False

        for child in node.childs:
            if result is False:
                if child.word == word:
                    result = True

                else:
                    result = self.search(child, word)
        return result


if __name__=="__main__":
    trie = Trie()
    trie.add('apple')
    trie.add('banana')
    trie.add('begin')
    trie.add('return')
    trie.add('go')

    preorderOutput = trie.preOrder(trie.root)
    print(preorderOutput)

    print(trie.search(trie.root, 'apple'))
    print(trie.search(trie.root, 'hi'))