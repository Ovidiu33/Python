from domeniu.disciplina import Disciplina
class DisciplinaRepository:
    def __init__(self):
        self.__disciplina={}

    def getAllDiscipline(self):
        '''
        returneaza lista de discipline
        :return: o lista de obiecte de tipul disciplina
        '''
        return list(self.__disciplina.values())

    def getById(self,idDisciplina):
        '''
            returneaza disciplina cu id-ul dat
            :param Disciplina: string
            :return: un obiect de tipul Disciplina, daca exista unul cu id-ul dat, altfel None
        '''
        if idDisciplina in self.__disciplina:
            return self.__disciplina[idDisciplina]
        return None

    def adauga(self,disciplina):
        '''
            adaua o disciplina in dictionar
            :param angajat:
            :return:obiect de tipul disciplina
        '''
        if self.getById(disciplina.idDisciplina) is not None :
            raise KeyError("Exista deja un stiudent cu id ul acesta")
        self.__disciplina[disciplina.idDisciplina] = disciplina

    def modifica(self,disciplinaNoua):
        '''
            modifica o disciplina dupa id
            :param : disciplinaNoua
            :return:obiect de tipul Disciplina
            '''
        if self.getById(disciplinaNoua.idDisciplina) is None:
            raise KeyError("Nu exista nici o disciplina cu id ul introdus")
        self.__disciplina[disciplinaNoua.idDisciplina]=disciplinaNoua

    def sterge(self,idDisciplina):
        '''
        sterge o disciplina data
        :param idDisciplina:
        :return:
        '''
        if self.getById(idDisciplina) is None:
            raise KeyError("Nu exista nici-o disciplina cu id ul dat")
        self.__disciplina.pop(idDisciplina)

    def cauta(self,iDCautat):
        '''
        cauta o disciplina dupa id
        :param iDCautat:
        :return: obiect de tipul disciplina
        '''
        if self.getById(iDCautat) is None:
            raise KeyError("nu exista nici-o disciplina cu id ul acesta")
        return self.getById(iDCautat)

    def write(self):
        save_file = open("disciplina.txt", "w")

        lista = []

        for disciplina in self.getAllDiscipline():
            lista.append(disciplina.__dict__)

        save_file.write(str(lista))

    def read(self):
        save_file = open("disciplina.txt", "r")
        self._disciplina = {}
        lista = list(eval(save_file.read()))

        for std in lista:
            self._disciplina[std["_Disciplina__idDisciplina"]] = Disciplina(std["_Disciplina__idDisciplina"], std["_Disciplina__numeDisciplina"], std["_Disciplina__profesor"])

