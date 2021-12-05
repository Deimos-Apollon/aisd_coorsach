from collections import Counter

from Hash_funcs.Hash_funcs import HashFunctionTrivial, HashFunctionPolynomial
from random import randint


class HashTableSepChain:
    def __init__(self, size=8):
        self.__size__ = size
        self.__data__ = tuple([] for _ in range(self.__size__))

        self.number_of_elements = 0
        self.occupied_cells = 0

        self.__hash_function__ = HashFunctionTrivial(self.__size__)

        self.__MAX_OCCUPANCY_RATE__ = 0.7
        self.__MAX_SIZE__ = 200000
        self.__RESIZE_MULTIPLIER__ = 2
        self.COLLISIONS_DETECTED = 0

    def resize(self, new_size):
        new_size = int(new_size)

        if new_size > self.__MAX_SIZE__:
            if self.__size__ == self.__MAX_SIZE__:
                print('Cant resize table - reached max table size!')
                return

        old_size = self.__size__
        self.__size__ = new_size
        if new_size == old_size:
            return

        self.__hash_function__.change_table_size(new_size)
        old_data = self.__data__
        self.__data__ = tuple([] for _ in range(new_size))
        self.COLLISIONS_DETECTED = 0
        self.number_of_elements = 0
        self.occupied_cells = 0

        for elem_list in old_data:
            if elem_list:
                for key, value in elem_list:
                    self.insert(key, value)

    def insert(self, key, value):
        if self.number_of_elements / self.__size__ >= self.__MAX_OCCUPANCY_RATE__:
            self.resize(self.__size__ * self.__RESIZE_MULTIPLIER__)

        key_hash = self.__hash_function__(key)

        list_hash = self.__data__[key_hash]

        # if list is empty - just append element to it
        if not list_hash:
            list_hash.append((key, value))
            self.occupied_cells += 1
            self.number_of_elements += 1
        else:
            # TODO MIND O(1)
            for index, elem_pair in enumerate(list_hash):
                if elem_pair[0] == key:
                    list_hash[index] = (key, value)
                    break
            # if key is not in table - just append it
            else:
                self.number_of_elements += 1
                self.COLLISIONS_DETECTED += 1
                list_hash.append((key, value))

    def get_value(self, key):
        key_hash = self.__hash_function__(key)

        list_hash = self.__data__[key_hash]

        if list_hash is None:
            return None
        for elem_pair in list_hash:
            if elem_pair[0] == key:
                return elem_pair[1]

        return None

    def pop(self, key):
        key_hash = self.__hash_function__(key)

        list_hash = self.__data__[key_hash]

        if list_hash is None:
            return None
        for index, elem_pair in enumerate(list_hash):
            if elem_pair[0] == key:
                list_hash.pop(index)
                self.number_of_elements -= 1
                if not list_hash:
                    self.occupied_cells -= 1
                return elem_pair
        return None

    def find(self, key):
        key_hash = self.__hash_function__(key)

        list_hash = self.__data__[key_hash]

        if list_hash is None:
            return None
        for index, elem_pair in enumerate(list_hash):
            if elem_pair[0] == key:
                return elem_pair
        return None

    def hash_list_of_pairs(self, arr):
        for elem in arr:
            self.insert(elem[0], elem[1])

    def get_table_info(self):
        text = f"-------Separate Chain table info---------\n" \
               f"Table size: {self.__size__}\n" \
               f"Cells Occupied: {self.occupied_cells}\n" \
               f"Cells free: {self.__size__ - self.occupied_cells}\n" \
               f"Total number of elements: {self.number_of_elements}\n" \
               f"Collisions detected: {self.COLLISIONS_DETECTED}\n" \
               f"----------------------------------------------\n"
        return text

    def clear(self):
        self.__data__ = tuple([] for _ in range(self.__size__))
        self.__size__ = 8
        self.__hash_function__.change_table_size(8)

        self.number_of_elements = 0
        self.occupied_cells = 0

        self.COLLISIONS_DETECTED = 0


if __name__ == "__main__":
    hs = HashTableSepChain(size=5)
    print(hs.__data__)
    arr = [(randint(0, 100), randint(0, 10 ** 4)) for i in range(18)]
    hs.hash_list_of_pairs(arr)
    print(hs.get_table_info())
    print(hs.__data__[:15])

    c = Counter()
    for index, list_elem in enumerate(hs.__data__):
        c[index] = len(list_elem)

    print(c.most_common(10))
