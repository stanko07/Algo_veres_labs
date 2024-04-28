import unittest

from src.wedding_2_groups import DisjoinSet


class TestUnionFind(unittest.TestCase):
    def test_union_find_2(self):
        union_find = DisjoinSet([1, 8, 3, 4, 5, 6, 7, 2])
        pairs = []

        pair1 = union_find.union(1, 2)
        pair2 = union_find.union(3, 4)
        pair3 = union_find.union(5, 6)
        pair4 = union_find.union(7, 8)
        pair5 = union_find.union(2, 3)

        pairs.append(pair1)
        pairs.append(pair2)
        pairs.append(pair3)
        pairs.append(pair4)
        pairs.append(pair5)
        result = union_find.wedding(pairs)

        self.assertEqual(result, (10,
                                  [(8, 1),
                                   (8, 3),
                                   (8, 5),
                                   (2, 5),
                                   (2, 7),
                                   (4, 5),
                                   (4, 7),
                                   (6, 1),
                                   (6, 3),
                                   (6, 7)]))

    def test_union_find(self):
        union_find = DisjoinSet([1, 2, 3, 4, 5, 8, 10])
        pairs = []

        pair1 = union_find.union(1, 2)
        pair2 = union_find.union(2, 4)
        pair3 = union_find.union(1, 3)
        pair4 = union_find.union(3, 5)
        pair5 = union_find.union(8, 10)

        pairs.append(pair1)
        pairs.append(pair2)
        pairs.append(pair3)
        pairs.append(pair4)
        pairs.append(pair5)

        result = union_find.wedding(pairs)

        self.assertEqual(result, (6, [
            (8, 1),
            (8, 3),
            (8, 5),
            (10, 1),
            (10, 3),
            (10, 5)]))

    def test_union_find_empty(self):
        union_find = DisjoinSet([])
        pairs = []
        result = union_find.wedding(pairs)
        self.assertEqual(result, (0, []))

    def test_union_find_no_pairs(self):
        union_find = DisjoinSet([1, 2, 3, 4])
        pairs = []
        result = union_find.wedding(pairs)

        self.assertEqual(result, (0, []))


if __name__ == '__main__':
    unittest.main()
