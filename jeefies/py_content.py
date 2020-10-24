import os
import sys
#from threading import Thread


class Content:
    '''
    a class to manage some infomation
    You must give the work directory or this function wouldn't now where to do the orders
    '''

    def __init__(self, work_place: 'path', name: str = ''):
        '''
        You must give the wrok place, and it's a directory
        name: the content main topic, if not give, the topic is None, and it might be all used
        '''
        if os.path.isdir(work_place):
            self.pl = work_place
        else:
            raise TypeError('The work place must be a directory')
        self.file = os.path.join(work_place, '.con{}.txt'.format(name))
        # print(self.file)
        self.content = {}
        self.read()
        #self.update()

    def reset(self):
        '''
        To clean tha datas
        '''
        try:
            os.remove(self.file)
        except:
            pass
        f = open(self.file, 'x')
        f.close()
        self.read()

    def read(self):
        '''
        Read from the data file in another thread
        '''
        def r():
            try:
                f = open(self.file, encoding='utf-8')
                lines = f.read().split(chr(1136))[:-1]
                # print(lines)
                content = {}
                for x in lines:
                    l = x.split(chr(1138))
                    content.update({l[0]: l[1:]})
            except:
                content = {}
            return {**self.content, **content}
        #return Thread(target=r).start()
        # print(self.content)
        self.content = r()

    def update(self):
        '''
        To uodate the data file according to the content
        '''
        with open(self.file, 'w', encoding='utf-8') as f:
            for key, val in self.content.items():
                print(key, *val, sep=chr(1138), file=f, end=chr(1136))
        # print(self.content)
        self.read()

    def get(self, index):
        '''
        To get the infomation by the index
        '''
        self.read()
        res = self.content.get(index, None)
        if res:
            return index, res
        return None

    def add(self, index: (str, int), values: (list, tuple)):
        """
        add new content by the index
        """
        with open(self.file, 'a', encoding='utf-8') as f:
            print(index, *values, sep=chr(1138), end=chr(1136), file=f)
        self.read()

    def set(self, index: (str, int), value: (list, tuple)):
        """
        rset the index content
        """
        self.add(index, value)

    def all(self):
        """return all values exclude index"""
        self.read()
        return self.content.values()

    def allname(self):
        """return all index exclude values"""
        self.read()
        return self.content.keys()

    def allitem(self):
        """return all index with values"""
        self.read()
        return self.content.items()

    def rm(self, index: (str, int)):
        """remove(delete) a index"""
        res = self.content.pop(index, None)
        self.update()
        self.read()
        return res

    def has(self, index):
        """if the index exists, return True, else, Flase"""
        if self.get(index):
            return True
        else:
            return False

    def __str__(self):
        return self.pl

"""
class LongContent:
    '''A class to manage more than one hundred lines of content, it's more faster to analze the larger data'''
    def __init__(work_place: 'path', name: str = None):
        self.place = work_place
"""

if __name__ == '__main__':
    con = Content(os.getcwd())
    con.add('key', ['one'])
    print(con.get('key'))
    con.add('new', ['so', 'many'])
    print(con.get('new'))
    print(con.content)
    con.rm('key')
    print(con.content)
    con.add('line', ['a sentences for a'])
    print(con.content)
    # con.rm('line')
    print(con.content)
