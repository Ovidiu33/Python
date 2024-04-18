from dataclasses import dataclass


@dataclass

class Student:

    idStudent : int
    nume : str

    def __str__(self):
        return f"id:{self.idStudent},nume:{self.nume}"


'''
class Student:
    def __init__(self,idStudent, nume):
        self.__idStudent= idStudent
        self.__nume=nume
'''




