class O_test:
    '''
    a function to help fibonacci to analyze complexity
    '''
    
    
    def __init__(self, *args, **kwargs):
        self.O = 0
        self.o = 0
        for name in args:
            self.__dict__[name] = 0
        for (k, v) in kwargs.items():
            self.__dict__[k] = v
    
    def __set__(self, name, val):
        self.__dict__[name] = val
        
    def __str__(self):
        return str(self.O) if self.O != 0 else str(self.o)
