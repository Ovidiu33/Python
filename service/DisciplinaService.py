from domeniu.disciplina import Disciplina
from repository.disciplinaRepository import DisciplinaRepository

class DisciplinaService:

    def __init__(self, disciplinaRepository: DisciplinaRepository):
        self.__disciplinaRepository = disciplinaRepository

    def getAllDiscipline(self):
        '''
        returneaza o lista de discipline
        :return: o lista de obiecte de tipul Disciplina
        '''
        return self.__disciplinaRepository.getAllDiscipline()

    def getbyId(self,idDisciplina):
        '''
        returneaza o lista de discipline dupa id
        :param idDisciplina:
        :return:
        '''
        return self.__disciplinaRepository.getById(idDisciplina)

    def adauga(self, id, nume, profesor):
        '''
        adauga o disciplina
        :param id:
        :param nume:
        :param profesor:
        :return:
        '''
        disciplina = Disciplina(id, nume, profesor)
        self.__disciplinaRepository.adauga(disciplina)

    def sterge(self, id):
        '''
        sterge o disciplina
        :param id:
        :return:
        '''
        self.__disciplinaRepository.sterge(id)

    def modifica(self, id, numeNou,profsesor_nou):
        '''
        modifica o disciplina
        :param id:
        :param numeNou:
        :param profsesor_nou:
        :return:
        '''
        disciplinaNouA =Disciplina(id, numeNou,profsesor_nou)
        self.__disciplinaRepository.modifica(disciplinaNouA)

    def cauta(self,idDisciplina):
        '''
        cauta o disciplina
        :param idDisciplina:
        :return:
        '''
        return self.__disciplinaRepository.cauta(idDisciplina)

    def write(self):
        self.__disciplinaRepository.write()

    def read(self):
        self.__disciplinaRepository.read()


