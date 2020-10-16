import time

class strtime:
    """
    strtime class, use for some simple time use
    just a package packed the time module
    :The default 
    :str(time object, ft(time format)):return a sting time by the format
    :fromStr(string, ft(format)): return a time object by the string and the format
    :now(ft(format)): return a str time for now
    :compare, compare two strtime, (1,0) stands for '>',
    (0,1) stands for '<'
    """
    tf = '%Y %j %H %M %S' #Full year, fullday, hour, min, sec
    
    @classmethod
    def str(cls, stime: time, ft: 'format' =None) -> str:
        """
        return a string form the stime according to the ft
        """
        if not ft:
            ft = cls.tf
        return time.strftime(ft, stime)

    @classmethod
    def fromStr(cls, string: str, ft: 'format'=None):
        """
        analyze then return a time object from the string according to the ft
        """
        if not ft:
            ft = cls.tf
        return time.strptime(string, ft) if isinstance(string, str) else string


    @classmethod
    def now(cls, ft: 'format'=None) -> time:
        """return a string for now according to the ft"""
        if not ft:
            ft = cls.tf
        return time.strftime(ft)
    
    @classmethod
    def compare(cls, one: str, two: str, ft: (str, tuple((str, str)), [str, str])=None):
        """compare two strtime string, (0,1) stands for smaller, (1,0) stands for bigger"""
        if not ft:
            ft1, ft2 = cls.tf
        if isinstance(ft, (tuple, list)) and len(ft) == 2:
            ft1, ft2 = ft
        elif not isinstance(ft, str):
            raise TypeError("Please give the strtime")
        if one > two:
            return (1,0)
        elif one < two:
            return (0,1)
        else:
            return (0,0)

    @classmethod
    def time_out(cls, strt, ft: 'foamt'=None, sec=86400):
        """
        A function to check if the strtime is out of time
        sec stands for the time out time by seconds
        """
        if not ft:
            ft = cls.tf
        t = cls.fromStr(strt, ft)
        dayago = time.localtime(time.time() - sec)
        if t >= dayago:
            return False
        else:
            return True
