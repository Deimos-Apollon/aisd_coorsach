class HashFunctionTrivial:
    def __init__(self, table_size):
        self.table_size = table_size

    def change_table_size(self, new_size):
        self.table_size = new_size

    def __call__(self, element):
        return element % self.table_size


class HashFunctionTrivialPrimeNumber:
    def __init__(self, prime, table_size):
        self.prime = prime
        self.table_size = table_size

    def change_table_size(self, table_size):
        self.table_size = table_size

    def __call__(self, element):
        return (self.prime - element % self.prime) % self.table_size


class HashFunctionNearestOddNumber:
    def __init__(self, table_size):
        self.table_size = table_size

    def change_table_size(self, table_size):
        self.table_size = table_size

    def __call__(self, element):
        elem_hash = element if element % 2 == 1 else element - 1
        return elem_hash % self.table_size


class HashFunctionPolynomial:
    def __init__(self, prime_number, argument, table_size):
        self.prime_number = prime_number
        self.argument = argument
        self.table_size = table_size
        # TODO

    def change_table_size(self, new_size):
        self.table_size = new_size

    def __call__(self, element):
        pass
