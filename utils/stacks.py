class Stack:
    def __init__(self):
        self.__array = [] # hiding the data using double underscore

    def push(self,element):
        self.__array.append(element)
        return self.__array

    def pop(self):
        return self.__array.pop()
    
    def export_dict(self):
        dictionary = dict()
        for i in enumerate(self.__array):
            dictionary[i[0]]=i[1]
        return dictionary

    def __repr__(self):
        return str(self.__array[::-1]) # must be converted to string before printing