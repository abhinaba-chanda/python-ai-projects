"""Autocomplete with a simple trie."""


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def suggest(self, prefix, limit=5):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return []
            node = node[ch]
        results = []

        def walk(n, path):
            if len(results) >= limit:
                return
            if "$" in n:
                results.append(prefix + path)
            for ch in sorted(k for k in n if k != "$"):
                walk(n[ch], path + ch)

        walk(node, "")
        return results


if __name__ == "__main__":
    t = Trie()
    for w in ["python", "pytest", "pandas", "java"]:
        t.insert(w)
    print(t.suggest("py"))
