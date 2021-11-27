from Hash_funcs.Hash_funcs import *


class HashTableDoubleHashing:
    def __init__(self, size=10):
        self.__size__ = size
        self.__data__ = [None for _ in range(self.__size__)]

        self.__number_of_elements__ = 0

        self.__hash_function1__ = HashFunctionTrivial(self.__size__)
        self.__prime_for_hash2__ = 5
        self.__hash_function2__ = HashFunctionTrivialPrimeNumber(self.__prime_for_hash2__)

        self.__MAX_OCCUPANCY_RATE__ = 0.7
        self.__RESIZE_MULTIPLIER__ = 2

    def insert(self, key, value):
        hash_key1 = self.__hash_function1__(key)

        # if cell is empty, just insert in it
        if self.__data__[hash_key1] is None:
            self.__data__[hash_key1] = (key, value)
        else:
            hash_key2 = self.__hash_function2__(key)

            i = 1
            while i < self.__size__:
                new_ind = (hash_key1 + i * hash_key2) % self.__size__
                if not self.__data__[new_ind]:
                    self.__data__[new_ind] = (key, value)
                    break
                i += 1
            else:
                pass

    def __resize__(self):
        pass

    def get_table_info(self):
        text = f"---------------Table info--------------\n" \
               f"Table size: {self.__size__}\n" \
               f"Number of elements: {self.__number_of_elements__}\n" \
               f"Cells free: {self.__size__ - self.__number_of_elements__}\n" \
               f"Hash function 2 prime number: {self.__prime_for_hash2__}\n" \
               f"----------------------------------------------\n"
        return text


if __name__ == "__main__":
    hs = HashTableDoubleHashing(10)
    print(hs.get_table_info())
    arr = [(i, i) for i in range(1, 39, 3)]
    for a in arr:
        hs.insert(a[0], a[1])
    print(hs.__data__)

