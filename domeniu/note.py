from dataclasses import dataclass
@dataclass
class note:
    idNota : int
    idStudent: int
    idDisciplina : int
    Valoarea : int
    def __str__(self):
        return f"idNota:{self.idNota},idSudent:{self.idStudent},idDisciplina:{self.idDisciplina},ValoareaNotei:{self.Valoarea}"


'''
class note:
    def __init__(self,idNota,idStudent,idDisciplina,Valoarea):
        self.__idNota=idNota
        self.__idStudent=idStudent
        self.__idDisciplina=idDisciplina
        self.__Valoarea=Valoarea

    def getIdStudent(self):
        return self.__idStudent

    def getIdDisciplina(self):
        return self.__idDisciplina

    def getIdNota(self):
        return self.__idNota

    def getIdValoare(self):
        return self.__Valoarea

    def setNota(self,Valoarea):
        self.__Valoarea=Valoarea

    def __str__(self):
        return f"idNota:{self.__idNota},idSudent:{self.__idStudent},idDisciplina:{self.__idDisciplina},ValoareaNotei:{self.__Valoarea}"
'''