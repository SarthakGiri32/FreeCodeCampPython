class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key_str):
        return sum([ord(character) for character in key_str])

    def add(self, key, value):
        key_hash_value = self.hash(str(key))
        if key_hash_value not in self.collection:
            self.collection[key_hash_value] = {}
        self.collection[key_hash_value][key] = value

    def remove(self, key):
        key_hash_value = self.hash(str(key))
        if key_hash_value in self.collection and key in self.collection[key_hash_value]:
            del self.collection[key_hash_value][key]
            if not self.collection[key_hash_value]:
                del self.collection[key_hash_value]

    def lookup(self, key):
        key_hash_value = self.hash(str(key))
        if key_hash_value in self.collection and key in self.collection[key_hash_value]:
            return self.collection[key_hash_value][key]
        else:
            return None


def main():
    hash_table = HashTable()
    print(f"hash_table.hash(\"golf\"): {hash_table.hash("golf")}")

    print("\nAdding keys...")
    hash_table.add("golf", "sport")
    hash_table.add("dear", "friend")
    hash_table.add("read", "book")

    print("\nTesting hash table ops:")
    print(f"hash_table.collection: {hash_table.collection}")
    print(f"hash_table.lookup(\"golf\"): {hash_table.lookup("golf")}")
    print("\nRemoving keys...")
    hash_table.remove("golf")
    print(f"hash_table.lookup(\"golf\"): {hash_table.lookup("golf")}")
    print(f"hash_table.collection: {hash_table.collection}")

    print("\nAdding more keys...")
    hash_table.add("fcc", "coding")
    print(f"hash_table.lookup(\"cfc\"): {hash_table.lookup("cfc")}")
    print(f"hash_table.collection: {hash_table.collection}")
    hash_table.add("rose", "flower")
    print(f"hash_table.collection: {hash_table.collection}")
    hash_table.add("cfc", "chemical")
    print(f"hash_table.collection: {hash_table.collection}")

    print("\nRemoving keys:")
    hash_table.remove("rose")
    print(f"hash_table.collection: {hash_table.collection}")
    hash_table.remove("dear")
    print(f"hash_table.collection: {hash_table.collection}")

if __name__ == "__main__":
    main()
