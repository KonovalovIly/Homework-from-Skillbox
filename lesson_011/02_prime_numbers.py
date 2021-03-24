# -*- coding: utf-8 -*-

# создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.prime_numbers = []
        self.n = n
        self.num = 0

    def __iter__(self):
        self.num = 1
        return self

    def _get_next_prime_or_none(self):
        self.num += 1
        for prime in self.prime_numbers:
            if self.num % prime == 0:
                return None
        self.prime_numbers.append(self.num)
        return self.num

    def __next__(self):
        value = None
        while value is None:
            value = self._get_next_prime_or_none()
        if self.num < self.n:
            return value
        else:
            raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)
