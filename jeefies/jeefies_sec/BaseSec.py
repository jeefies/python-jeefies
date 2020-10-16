import os
import sys

_basedir = os.path.dirname(__file__) + os.sep


class ModError(Exception):
    pass


class BaseSec:
    '''
    The base class of the secret modules or functions
    '''
    @classmethod
    def fromFile(cls, filename: (str, open(_basedir + 'example.txt')), coding: str = 'utf-8', mod: ('en', 'de', 'encrypt', 'decrypt') = 'encrypt') -> tuple:
        '''
        def fromFile(filename, coding='uft-8', mod='encrypt'):
            filename: the filename of the file needs to read or one opened file
            coding: the coding mod of the read file
            mod: 'encrypt' or 'en', 'decrypt' or 'de'
        '''
        con = cls.findFile(filename, coding)

        def f(x):
            if mod in ('en', 'encrypt'):
                return cls.encrypt(x)
            elif mod in ('de', 'decrypt'):
                return cls.decrypt(x)
            else:
                raise ModError('No such mod')
        return tuple(f(x) for x in con)

    @classmethod
    def findFile(cls, file: (str, open(_basedir + 'example.txt')), coding: str = 'utf-8') -> list:
        '''
        def findFile(filename, coding='utf-8')
            file: to find the file by the name, also can be the absolute path of the file.One opened file is also ok
            coding: the coding of the read file
        '''
        if isinstance(file, type(open('example.txt'))):
            filename = file.name
        else:
            filename = file
        if os.path.isabs(filename):
            with open(filename, encoding=coding) as f:
                con = f.readlines()
        else:
            base = os.getcwd()
            if os.path.exists(base + filename):
                path = os.path.join(base, filename)
            else:
                for root, paths, files in os.walk(base):
                    if filename in files:
                        path = os.path.join(root, filename)
                        break
                    else:
                        pass
                else:
                    raise FileNotFoundError(
                        'No such file or it\'s a directory')
            with open(path, encoding=coding) as f:
                con = f.readlines()
        return con

    @classmethod
    def toFile(cls, outfile: str, lines: (list, tuple) = None, infile: ('filename', open(_basedir + 'example.txt')) = None, coding: str = 'utf-8', mod: ('encrypt', 'en', 'decrypt', 'de') = 'encrypt'):
        '''
        def toFile(outfile, lines, infile, coding, mod)
            outfile: the outfile name, you can give the absolute path or the path would be the work path
            lines or infile:
                You can choose between lines or infile or the lines will be ignore
                lines: This function would do nothing with the lines but just write them into the outfile
                infile: The file would be read and be encrypted or decrypted and write in the outfile
            coding: the coding of the openfile
            mod: 'encrypt' or 'en', 'decrypt' or 'de'
        '''
        if os.path.isabs(outfile):
            path = outfile
        else:
            path = os.path.join(os.getcwd(), outfile)

        if infile:
            con = cls.fromFile(infile, coding=coding, mod=mod)
            with open(path, 'w', encoding=coding) as f:
                print(*con, file=f, sep='\n')
            return con
        elif lines:
            with open(path, 'w', encoding=coding) as f:
                print(*lines, file=f, sep='\n')
            return lines
        raise TypeError('Missing 1 argument in lines or infile')


if __name__ == '__main__':
    sec = BaseSec
    print(sec.findFile('hexsec.py'))
    sec.toFile('test.txt', lines=['a', 'kjg'])
