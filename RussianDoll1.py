class Doll(object):

    def __init__(self, envelop):
        self.w = envelop[0]
        self.h = envelop[1]

    def __lt__(self, other):
        return self.w < other.w and self.h < other.h

    def __gt__(self, other):
        return return self.w > other.w and self.h > other.h


class DollNode(object):

    def __init__(self, doll):
        self.doll = doll
        self.next = None


class DollList(object):

    def __init__(self):
        self.root = None
        self.len = 0

    def insert(self, envelop):
        if self.root is None:
            self.root = DollNode(Doll(envelop))
        else:
            doll = Doll(envelop)
            self._insert(root, root.next, doll)

    def _insert(self, prev_node, node, doll):
        if node is None:
            node = DollNode(doll)
            self.len += 1
            return
        elif node.doll > doll:
            self._insert(node, node.next, doll)
        elif node.doll < doll:
            _doll = node.doll
            node.doll = doll
            tmp_node = DollNode(_doll)
            tmp_node.next = node.next
            node.next = tmp_node
            self.len += 1
            return
        else:
            raise ValueError
        return

    def __len__(self):
        return self.len


def get_max_doll(dolls):
    return max([len(doll) for doll in dolls])


class Solution(object):
    @classmethod
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        dolls = [DollList()]
        for envelop in envelopes:
            not_put = True
            for doll in dolls:
                try:
                    doll.insert(envelop)
                except ValueError:
                    not_put = True
            if not_put:
                dolls.append(DollList().insert(envelop))
        return get_max_doll(dolls)

if __name__ == "__main__":
    inp = input()
    envelopes = eval(inp)
    print(Solution.maxEnvelopes(envelopes))
