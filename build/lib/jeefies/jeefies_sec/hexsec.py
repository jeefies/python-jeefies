import os
import sys
import random
from .BaseSec import BaseSec

class Hexsec(BaseSec):
    '''
    This is a function to encrypt a file or a sentence or a letter
    Does't support Chinese words
    :__init__(self, sentence=None)
    :encrypt(iterable)
    :decrypt(iterable)
    :fromFlie(filename, coding='utf-8', mod)
        mod can be 'encrypt' or 'decrypt', default encrypt ('en', 'de' are also ok)
    :toFile(outfile, lines, infile, coding='utf-8', mod)
        You can choose lines or infile to write in
        If your choose infile to read and write in outfile,
        you can choose mod in 'decrypt' or 'encrypt'('en', 'de' are also ok)
    ''' 
    __nums = list(range(1, 35))
    __tos = 'abcdefghijklmnopqrstuvwxyz,.?!\'\" :'
    _lower = 'abcdefghijklmnopqrstuvwxyz'
    _lts = {a:b for a,b in zip(list(__tos), __nums)}
    _ns  = {b:a for a,b in zip(__tos, __nums)}
    def __new__(cls, *arg, **kwargs):
        raise TypeError("Hexsec fuction is not callable")

    """
    @classmethod
    def fromFile(cls, filename, coding = 'utf-8', mod = 'encrypt'):
        '''
        def fromFile(filename, coding='utf-8', mod='encrypt')
            filename: the filename of the file should read
            coding: the coding of the read file
            mod: 'encrypt' or 'en', 'decrypt' or 'de'
        '''
        con = cls.findFile(filename, coding)
        def f(x):
            if mod == 'en' or mod == 'encrypt':
                return cls.encrypt(x) + '\n'
            elif mod == 'de' or mod == 'decrypt':
                return cls.decrypt(x)
        return [f(x) for x in con]

    def __str__(self):
        return self.encrypt(self.ins)

    @staticmethod
    def findFile(filename, coding = 'utf-8'):
        '''
        def findFile(filename, coding='utf-8')
            filename: to find the file by the name from the basedir
            coding: the coding of the read file
        '''
        basedir = os.getcwd()
        try:
            with open(filename, encoding=coding) as f:
                con = f.readlines()
        except:
            for root, paths, files in os.walk(basedir):
                if filename in files:
                    with open(root + filename) as f:
                        con = f.readlines()
                    break
            else:
                raise FileNotFoundError('No such file or it\'s a director')
        return con

    @classmethod
    def toFile(cls, outfile, lines = None, infile=None, coding = 'utf-8', mod='encrypt'):
        '''
        def toFile(outfile, lines=None, infile=None, coding='utf-8', mod='encrypt')
            outfile: you can give a absolute path or relative path with the filenam in the end
            lines: you can choose lines or infile to write in the outfile
                if the lines are given, this function would do nothing but just write the lines in to the file
            infile: you can give the infile to encrypt or decrypt, it depends on the mod
                if infile argument is giving, the lines wouldn't be used
                do not give the opened file, just give the filename and this 
                    function would use findFile function to find the file
            !; do not give both lines or infile, or there would be and error
            coding: the coding of the open file
            mod: 'encrypt' or 'en', 'decrypt' or 'de'
        '''
        if os.path.isabs(outfile):
            path = outfile
        else:
            path = os.path.join(os.getcwd(), outfile)
        if infile and lines:
            raise TypeError('Do not give both the lines argument and the infile argument')
        if infile:
            con = cls.fromFile(infile, mod=mod)
            with open(path, 'w', encoding = coding) as f:
                f.writelines(con)
            return con
        elif lines:
            with open(path, 'w', encoding = coding) as f:
                f.writelines(lines)
            return lines
        else:
            raise FileNotFoundError('No contents to write in')
    """

    @classmethod
    def encrypt(cls, iterable):
        '''
        def encrypt(iterable)
            return a sentence concat by each letter in the iterable arguments
        !: every item in the iterable shuold be one letter or there would be something wrong
        '''
        return ''.join([cls._encrypt(lt) for lt in iterable])

    @classmethod
    def decrypt(cls, iterable):
        '''
        def decrypt(iterable)
            retrun a sentence decrypt from the arguments in
        !: every item in the iterable should be one letter or there would be something wrong, but no error raised
        '''
        li = ''.join(map(str, iterable)).strip()
        #print(li)
        li = tuple(li)
        result = []
        pl = 0
        while pl < len(li):
            if li[pl] == '!':
                result.append(''.join([li[pl + b] for b in range(1,5)]))
                pl += 5
            else:
                result.append(''.join([li[pl + b] for b in range(3)]))
                pl += 3
        return ''.join([cls._decrypt(lt) for lt in result])

    @classmethod
    def _decrypt(cls, lt):
        '''
        def _decrypt(lt):
            decrypt one letter's passwd
        '''
        if len(lt) == 3:
            pl = int(lt[::-1][1:], base=8)
            res = cls._ns[pl]
            if int(lt[-1]) % 2 == 1:
                res = res.upper()
            return res
        else:
            return chr(int(lt) // 7) if int(lt[0]) % 2 == 0 else chr(int(lt) // 7).upper()

    @classmethod
    def _encrypt(cls, lt):
        '''
        def _encrypt(lt)
            encrypt one letter
        '''
        if not isinstance(lt, str):
            lt = str(lt)
        if len(lt) > 1:
            raise TypeError('The argument in must be one letter')
        if lt.lower() in cls.__tos:
            up = 0 if lt in cls.__tos else 1
            #print(lt, up)
            sec = cls._lts[lt.lower()]
            h = oct(sec)[2:].zfill(2)
            return str(h)[::-1] + str(random.randint(0,4)* 2 + up)
        else:
            return '!'+str(ord(lt) * 7).zfill(4)

    @classmethod
    def sec(cls, lt):
        return cls._encrypt(lt)

if __name__ == '__main__':
    print(os.getcwd())
    sec = Hexsec
    print(sec('Iwalkaround'))
    print(sec.sec(','))
    print(list(sec.fromFile('place.py')))
    print(sec.toFile('test.txt', infile = 'place.py'))
    print(sec.decrypt(sec.encrypt('aaaa')))
    print(sec.fromFile('test.txt', mod='de'))
