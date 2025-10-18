import sys

sys.setrecursionlimit(10000)

class DSUParity:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.parity = [0]*n  # parity[x] = xor from x to parent[x]

    def find(self, x):
        if self.parent[x] != x:
            root = self.find(self.parent[x])
            self.parity[x] ^= self.parity[self.parent[x]]
            self.parent[x] = root
        return self.parent[x]

    # get parity from x to its root (after find)
    def get_parity(self, x):
        self.find(x)
        return self.parity[x]

    # unite a and b with relation: parity_a xor parity_b = val
    # returns True if merged/consistent, False if contradiction
    def unite(self, a, b, val):
        ra = self.find(a)
        rb = self.find(b)
        pa = self.get_parity(a)
        pb = self.get_parity(b)
        # we need pa xor pb == val after union
        if ra == rb:
            # check consistency
            return ((pa ^ pb) == val)
        # attach smaller rank to larger
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
            pa, pb = pb, pa
        # make rb child of ra
        self.parent[rb] = ra
        # set parity[rb] such that pa xor parity_rb_to_ra xor pb == val
        # parity_rb_to_ra = pa xor pb xor val
        self.parity[rb] = pa ^ pb ^ val
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

def solve_one_test(n, m, queries):
    # компрессируем позиции l-1 и r
    coords = {}
    coord_list = []
    def add_coord(x):
        if x not in coords:
            coords[x] = len(coord_list)
            coord_list.append(x)
    for (l, r, _) in queries:
        add_coord(l-1)
        add_coord(r)
    dsu = DSUParity(len(coord_list))
    for i, (l, r, parity_word) in enumerate(queries, start=1):
        val = 0 if parity_word == 'even' else 1
        a = coords[l-1]
        b = coords[r]
        ok = dsu.unite(a, b, val)
        if not ok:
            return i-1
    return m

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    outputs = []
    while True:
        try:
            x = next(it)
        except StopIteration:
            break
        n = int(x)
        if n == -1:
            break
        m = int(next(it))
        queries = []
        for _ in range(m):
            l = int(next(it))
            r = int(next(it))
            word = next(it)
            # normalize word: input says "even" or "odd"
            queries.append((l, r, word))
        res = solve_one_test(n, m, queries)
        outputs.append(str(res))
    sys.stdout.write("\n".join(outputs))

if __name__ == "__main__":
    main()
