import abc 

class GOtsu(metaclass = abc.ABCMeta):

    @abc.abstractclassmethod
    def otsu_instance(self):
        'You should instance single otsu class'
        return NotImplementedError
    @abc.abstractmethod
    def otsu_collection(self,threshold):
        'When you go into gotsu, u should do otsu_collection first'
        return NotImplemented
    
    @abc.abstractclassmethod
    def otsu_collection_scanning(sekf, start, end):
        'When you go into gotsu, u should do some otsu_collection first'
        return NotImplemented
    
    @abc.abstractclassmethod
    def global_objective_input_different_number(self,list):
        'When u go into gotsu, put manu numbers in one time'
        return NotImplemented
