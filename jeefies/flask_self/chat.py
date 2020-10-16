import os


class Chatting:

    def __init__(self, name, path=os.getcwd()):
        '''
        name: room name or the filename
        '''
        self.name = os.path.join(path, '.' + name + ".txt")
        self.content = list(self.context)

    def add(self, name, *context):
        '''
        add some data for one line
        '''
        with open(self.name, 'a', encoding="utf-8") as f:
            print(name, *context, sep='@#', end='&#', file=f)
        self.content.append([name, *context])

    def update(self):
        with open(self.name, 'w', encoding='utf-8') as f:
            for con in self.content:
                print(*con, sep='@#', end='&#', file=f)

    def reset(self):
        '''
        clean the data
        '''
        try:
            os.remove(self.name)
        except:
            pass
        f = open(self.name, 'x')
        f.close()

    @classmethod
    def _analyze(cls, content):
        return content.strip().split('@#')

    @property
    def context(self):
        if not os.path.exists(self.name):
            with open(self.name, 'x', encoding='utf-8') as f:
                pass
            return tuple()
        with open(self.name, "r", encoding='utf-8') as f:
            con = f.read().split('&#')[:-1]
        self.content = tuple(self._analyze(line) for line in con)
        return self.content

    def __len__(self):
        l = len(self.content)
        if l % 50 == 0 and l != 0:
            l -= 1
        return l

    def pages(self):
        con = self.content.copy()[::-1]
        res = []
        while len(con) > 50:
            res.append(con[:50])
            con = con[50:]
        res.append(con)
        return res

    def page(self, num: int):
        con = self.content[::-1]
        return con[50 * (num-1): 50*num]

    def keep(self, page: int):
        res = []
        [res.extend(self.page(num)) for num in range(1, page+1)]
        self.content = res
        self.update()
