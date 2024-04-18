from dataclasses import dataclass

@dataclass
class Disciplina:

    idDisciplina:int
    numeDisciplina:str
    profesor : str

    def __str__(self):
        return f"idDisciplina:{self.idDisciplina},numeDisciplina:{self.numeDisciplina},numeProf:{self.profesor}"


'''
class Disciplina:
    def __init__(self,idDisciplina,numeDisciplina,profesor):
        self.__idDisciplina=idDisciplina
        self.__numeDisciplina=numeDisciplina
        self.__profesor=profesor


    def getIdDisciplina(self):
        return self.__idDisciplina

    def getNumeDisciplina(self):
        return self.__numeDisciplina

    def getprofesor(self):
        return self.__profesor

    def setIdDisciplina(self,idDisciplina):
        self.__idDisciplina=idDisciplina

    def setnumeDisciplina(self,numeDisciplina):
        self.__numeDisciplina=numeDisciplina

    def setprofesor(self,profesor):
        self.__profesor=profesor
'''