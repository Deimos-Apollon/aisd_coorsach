from Hash_funcs.Hash_funcs import *


class HashTableDoubleHashing:
    def __init__(self, size=8):  # TODO soze = 2^n , h_2(k) - нечётные значения
        self.__size__ = size
        self.__data__ = [None for _ in range(self.__size__)]

        self.__number_of_elements__ = 0

        self.__hash_function1__ = HashFunctionTrivial(self.__size__)
        self.__hash_function2__ = HashFunctionNearestOddNumber(self.__size__)

        self.__MAX_OCCUPANCY_RATE__ = 0.7
        self.__MAX_SIZE__ = 200000
        self.__RESIZE_MULTIPLIER__ = 2
        self.COLLISIONS_DETECTED = 0

    def insert(self, key, value):
        if self.__number_of_elements__ / self.__size__ >= self.__MAX_OCCUPANCY_RATE__:
            self.__resize__(self.__size__ * self.__RESIZE_MULTIPLIER__)

        hash_key1 = self.__hash_function1__(key)

        # if cell is empty, just insert in it
        if self.__data__[hash_key1] is None:
            self.__data__[hash_key1] = (key, value)
            self.__number_of_elements__ += 1
        # if in cell is deleted element (empty tuple)
        elif not self.__data__[hash_key1]:
            self.__data__[hash_key1] = (key, value)
            self.__number_of_elements__ += 1
        # if keys is equal - change value
        elif self.__data__[hash_key1][0] == key:
            self.__data__[hash_key1] = (key, value)
            return
        else:
            hash_key2 = self.__hash_function2__(key)

            i = 1
            while i < self.__size__:
                new_ind = (hash_key1 + i * hash_key2) % self.__size__
                # if cell is empty or has deleted elem
                if not self.__data__[new_ind]:
                    self.__data__[new_ind] = (key, value)
                    self.__number_of_elements__ += 1
                    self.COLLISIONS_DETECTED += 1
                    break
                # if keys is equal to current key
                elif self.__data__[new_ind][0] == key:
                    self.__data__[new_ind] = (key, value)
                    break
                i += 1

    def hash_from_list_of_pairs(self, list_of_pairs):
        for pair in list_of_pairs:
            self.insert(pair[0], pair[1])

    def __resize__(self, new_size):
        new_size = int(new_size)

        if new_size > self.__MAX_SIZE__:
            if self.__size__ == self.__MAX_SIZE__:
                print('Cant resize table - reached max table size!')
                return

        old_size = self.__size__
        self.__size__ = new_size
        if new_size == old_size:
            return

        self.__hash_function1__.change_table_size(new_size)
        self.__hash_function2__.change_table_size(new_size)

        old_data = self.__data__
        self.__data__ = [None for _ in range(new_size)]
        self.__number_of_elements__ = 0
        self.COLLISIONS_DETECTED = 0
        for elem in old_data:
            # if element is None or is deleted elem - skip it
            if elem:
                self.insert(elem[0], elem[1])

    def find(self, key):
        hash_key1 = self.__hash_function1__(key)
        if self.__data__[hash_key1] is None:
            return None
        elif self.__data__[hash_key1] and self.__data__[hash_key1][0] == key:
            return self.__data__[hash_key1][1]
        else:
            hash_key2 = self.__hash_function2__(key)
            i = 1
            while i < self.__size__:
                new_ind = (hash_key1 + i * hash_key2) % self.__size__
                # if cell is empty
                if self.__data__[new_ind] and self.__data__[new_ind][0] == key:
                    return self.__data__[new_ind][1]
                i += 1
        return None

    def pop(self, key):
        hash_key1 = self.__hash_function1__(key)
        if self.__data__[hash_key1] is None:
            return None
        elif self.__data__[hash_key1] and self.__data__[hash_key1][0] == key:
            ret_value = self.__data__[hash_key1][1]
            self.__data__[hash_key1] = tuple()
            return ret_value
        else:
            hash_key2 = self.__hash_function2__(key)
            i = 1
            while i < self.__size__:
                new_ind = (hash_key1 + i * hash_key2) % self.__size__
                # if cell is empty
                if self.__data__[new_ind] and self.__data__[new_ind][0] == key:
                    ret_value = self.__data__[hash_key1][1]
                    self.__data__[hash_key1] = tuple()
                    return ret_value
                i += 1
        return None

    def copy(self):
        new_ht = HashTableDoubleHashing(size=self.__size__)
        for elem in self.__data__:
            if elem:
                new_ht.insert(elem[0], elem[1])
        return new_ht

    def get_table_info(self):
        deleted_elements_count = sum(1 if not i and i is not None else 0 for i in self.__data__)
        text = f"---------Double hashing Table info------------\n" \
               f"Table size: {self.__size__}\n" \
               f"Cells free: {self.__size__ - self.__number_of_elements__}\n" \
               f"Number of elements: {self.__number_of_elements__}\n" \
               f"Collisions detected: {self.COLLISIONS_DETECTED}\n" \
               f"Deleted elements: {deleted_elements_count}\n" \
               f"----------------------------------------------\n"
        return text


if __name__ == "__main__":
    hs = HashTableDoubleHashing()
    arr = [(i, i) for i in range(1, 130, 3)]
    for a in arr:
        hs.insert(a[0], a[1])
    print(hs.__data__)
    print(hs.get_table_info())
    for a in arr[:10]:
        hs.pop(a[0])
    print(hs.get_table_info())
    print(hs.__data__)
    for a in [(i, i) for i in range(130, 200, 3)]:
        hs.insert(a[0], a[1])
    print(hs.get_table_info())
    print(hs.__data__)
