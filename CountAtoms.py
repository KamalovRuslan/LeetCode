from collections import Counter
import re


class AtomCounter(Counter):

    def __imul__(self, val):
        for key in self.keys():
            self[key] *= val
        return self

    def __str__(self):
        return ''.join([atom + str(self[atom]) if self[atom] > 1 else
                        atom for atom in sorted(self)])


class Solution(object):

    def countOfAtoms(self, formula):
        tokens = re.split('([A-Z]{1}[a-z]?|\(|\)|\d+)', formula)
        tokens = list(filter(None, tokens))
        n = len(tokens)
        stack = [AtomCounter()]
        i = 0
        while i < n:
            token = tokens[i]
            if token == '(':
                stack.append(AtomCounter())
            else:
                count = 1
                if i + 1 < n and tokens[i + 1].isdigit():
                    count, i = int(tokens[i + 1]), i + 1
                atoms = stack.pop() if token == ')' else AtomCounter([token])
                atoms *= count
                stack[-1] += atoms
            i += 1
        return stack[-1]


if __name__ == "__main__":
    formula = input()
    solution = Solution()
    print(solution.countOfAtoms(formula))
