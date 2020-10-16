from .complexity_function import O_test as fib_O


class fibonacci:
    '''
    a program to show how fibonacci function work
    users can set the arguments to make the function speicial
    '''

    def __init__(self, num, fibonacci_list=True, *, add_times=2, O_test=None):
        '''
        prepare for the program
        :num means the results place in the list of fibonacci numbers
        :add_times means the numbers of the add numbers hehind
        :fibonacci_list stands for if the result start form the first 1
        '''
        #print('add times=%d' % add_times)
        if fibonacci_list:
            num = num - add_times + 1
        self.num = num
        self.fibonacci_list = fibonacci_list
        self.add_times = add_times
        if not O_test:
            O_test = fib_O()
        if add_times == 1:
            self.result = 1
        else:
            self.result = fibonacci.fibonacci(num, add_times, O_test)
        self.O_test = O_test

    def complexity(self):
        '''return the not true complexity, just a joke'''
        return self.O_test.O

    def __iter__(self):
        self.__li = ([1 for _ in range(self.add_times-1)] if self.fibonacci_list else []) + \
            [fibonacci.fibonacci(n, self.add_times, self.O_test)
             for n in range(1, self.num+1)]
        self.__pl = -1
        return self

    def __next__(self):
        if self.__pl >= len(self.__li)-1:
            raise StopIteration
        self.__pl += 1
        return self.__li[self.__pl]

    def __getitem__(self, num: (int, float)) -> int:
        '''
        num can be int or float
        if isinstance(num, int)
            return fibonacci.fibonacci(num, add_times = 2)
        else:
            num = int(num)
            add_times = num%1*1(the useful munber behind the dot is the add_times)
        '''
        if isinstance(num, float):
            number, add_times = str(num).split('.')
            number, add_times = int(number), int(add_times)
        else:
            number = num
            add_times = 2
        return fibonacci.fibonacci(number, add_times)

    def __setitem__(self, name, val):
        raise TypeError('fibonacci object does not support item assignment')

    @staticmethod
    def fibonacci(num, add_times, O_test=fib_O()):
        '''
        speicial fibonacci which can set by users
        also can analyze the complexity of the function
        '''
        O_test.O += 1
        if num <= 1:
            return 1
        elif add_times == 2:
            return fibonacci.fib(num, O_test)
        else:
            results = 0
            for n in range(1, add_times+1):
                results += fibonacci.fibonacci(num-n, add_times, O_test)
            return results

    @staticmethod
    def fib(num, O_test=fib_O()):
        '''
        the normal fibonacci function
        '''
        O_test.O += 1
        if num <= 1:
            return 1
        else:
            return fibonacci.fib(num-1)+fibonacci.fib(num-2)

    def __str__(self):
        return str(self.result)


class iterator_fibonacci:
    '''a simple iterable class iterator_fibonacci'''

    def __init__(self, O=fib_O()):
        self.num = 1
        self.O = O
        self.complex = O

    def complexity(self):
        return self.complex.o

    def fib(self, num):
        self.O.o += 1
        if num <= 1:
            return 1
        else:
            return self.fib(num-1) + self.fib(num-2)

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 1:
            self.O.o += 1
            res = 1
        else:
            res = self.fib(self.num)
        self.num += 1
        return res


def generate_fibonacci():
    '''A generator function to make fibonacci num list'''
    s, e = 0, 1
    yield 1
    while True:
        r = s+e
        yield r
        s, e = e, r


if __name__ == '__main__':
    fib1 = fibonacci(7)
    fib2 = fibonacci(7, add_times=4)
    fib3 = fibonacci(7, 0, add_times=3)
    print(fib1, fib1.complexity())
    print(fib2, fib2.complexity())
    print(fib3, fib3.complexity())
    print(fib1[3])
    print(fib2[3.4])
    print(tuple(fib1), tuple(fib2), tuple(fib3))
    fib = generate_fibonacci()
    li = [next(fib) for _ in range(7)]
    print(li)
    #print(fib.complex, li)
