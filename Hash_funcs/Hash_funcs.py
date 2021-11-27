
class HashFunctionTrivial:
    def __init__(self, table_size):
        self.table_size = table_size

    def change_table_size(self, new_size):
        self.table_size = new_size

    def __call__(self, element):
        return element % self.table_size


class HashFunctionTrivialPrimeNumber:
    def __init__(self, prime):
        self.prime = prime

    def change_prime_number(self, prime):
        self.prime = prime

    def __call__(self, element):
        return self.prime - element % self.prime


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
