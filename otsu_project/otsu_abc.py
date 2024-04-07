import abc 


class Otsu(metaclass = abc.ABCMeta):
    def __init__(self):
        self.var = []
        self.otsu = []
        self.podition = []
        self.result = {i: {} for i in range(256)}
        
    @abc.abstractmethod
    def otsu_variance(self, threshold):
        'When you put a dataset calculate single value variance'
        return NotImplemented
    
    @abc.abstractmethod    
    def otsu_scanning_threshold(self, start, end):
        'When you put a dataset calculate betweens the start and end'
        return NotImplemented

    @abc.abstractmethod
    def calculation(self, threshold):
        'Here to put different calculate methods'
    
        return NotImplemented


    @abc.abstractmethod
    def calculation_scanning_threshold(self, start, end):
        'When you put a dataset calculate the different methods betweens the start and end'
        return NotImplemented
    
    @abc.abstractmethod
    def result(self):
        'if u want build a summary list'
        return NotImplemented
    