import os
import sys
import random
from .. import rand
from .BaseSec import BaseSec

class FormatError(Exception):
    pass

class Hashsec(BaseSec):
    '''
    This is a function to encrypt some letter by unicode
    It mean's you can excrypt alomost every letter
    :encrypt
    :decrypt
    :fromFile
    :toFile
    :findFile
    !: not callable
    '''
    #__slots__ = ['encrypt', 'decrypt', '_encrypt', '_decrypt', 'fromFile', 'toFile', 'findFile']
    def __call__(sekf, *args, **kwargs):
        print('__call__ called')
        raise TypeError('Hashsec function is not callable')
    def __new__(cls, *args, **kwargs):
        raise TypeError('Hashsec function is not callable')

    @classmethod
    def encrypt(cls, iterable: (str, ('strings',), ['strings'])):
        '''
        def encrpyt(iterable)
            return a encrypted sentence
        !: every item in the iterable must be one length str or can change to str by __str__
        '''
        return ''.join(cls._encrypt(lt) for lt in iterable)

    @classmethod
    def decrypt(cls, iterable: (str, ('a letter',), ['a letter'])):
        '''
        def decrypt(iterable)
            return a sentence according to the iterable
        !: every item in the iterable must be one length str or can change to str by __str__
        '''
        try:
            res = tuple(''.join(iterable[o + a] for a in range(4)) for o in range(0, len(iterable), 4))
        except IndexError:
            raise TypeError('This ({}) is not a encrypted'.format(''.join(iterable)))
        return ''.join(cls._decrypt(one) for one in res)

    @classmethod
    def _encrypt(cls, lt):
        """
        def _encrypt(lt)
            encrypt one letter, just one, not many
        """
        lt = str(lt)
        if len(lt) != 1:
            raise TypeError('The letter in must be one length')
        n = bin(int(oct(ord(lt))[2:]))[2:].zfill(20)
        li = []
        for a in range(0, len(n), 5):
            res = ''
            try:
                for b in range(a, a+5):
                    res += n[b]
            finally:
                if res: li.append(int(res, base=2) + 68)
        res = (one if one > 68 else random.randint(32,68) for one in li)
        res = ''.join(chr(i) for i in res)
        return res

    @classmethod
    def _decrypt(cls, lt):
        """
        def _decrypt(lt)
           a function to decrypt one encrypted letter(for 4 length)
        """
        if not isinstance(lt, str) or not len(lt) == 4:
            raise FormatError
        li = tuple(ord(l) for l in lt)
        def f(x):
             if x <= 68:
                 return '0'.zfill(5)
             else:
                 return bin(x - 68)[2:].zfill(5)
        binary = ''.join(f(x) for x in li)
        res = int(str(int(binary, base=2)), base=8)
        return chr(res)


if __name__ == '__main__':
    sec = Hashsec
    print(sec.encrypt('和'))
    s65 = sec.encrypt('A')
    print(s65)
    print(sec.decrypt(s65))
    a = sec.encrypt('我是蜘蛛')
    print(a)
    print(sec.decrypt(a))

