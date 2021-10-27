class HashTable:
    # O(1)
    # modified from zybooks hash example
    def __init__(self, capacity = 10):
        self.map = []
        for i in range(capacity):
            self.map.append([])
            

    def _get_hash(self, key):
        buck = int(key) % len(self.map)
        return buck
    
    # O(n) -> add new package into hash table
    def add(self, key, value):
        # index value
        hash_key = self._get_hash(key)
        # what we want to insert
        key_value = [key, value]
        
        # check to see if cell is empty
        if self.map[hash_key] is None:
            # if it contains none, we can add to our map
            self.map[hash_key] = list([key_value])
            return True
        else:
            # check to see if it's already existing
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
                # IF not, then we append to list
            self.map[hash_key].append(key_value)
            return True
        
         # O(n)
    def update(self, key, value):
        hash_key = self._get_hash(key)
        
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('ERROR updating key ---> ' + key)
        
        # O(n) -> get value from hash table
    def get(self, key):
        hash_key = self._get_hash(key)
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    # O(n)
    def delete(self, key):
        hash_key = self._get_hash(key)
        
        if self.map[hash_key] is None:
            return False
        for i in range(0, len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)
                return True
            