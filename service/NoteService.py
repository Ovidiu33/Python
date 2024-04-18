from domeniu.note import note
from repository.noteRepository import NoteRepository
from domeniu.student import Student
from repository.studentRepository import StudentRepository
from domeniu.disciplina import Disciplina
from repository.disciplinaRepository import DisciplinaRepository

class NoteService:
    def __init__(self,noteRepository:NoteRepository,studentRepository:StudentRepository,disciplinaRepository:DisciplinaRepository):
        self.__noteRepository=noteRepository
        self.disciplinaRepository=disciplinaRepository
        self.__studentRepository=studentRepository

    def getAllNote(self):
        '''
        :return: o lista cu note
        '''
        return self.__noteRepository.getAll()

    def adauga(self,idNota,idStudent,idDisciplina,Valoarea):
        '''
        adauga note
        :param idNota:
        :param idStudent:
        :param idDisciplina:
        :param Valoarea:
        :return:
        '''
        nota=note(idNota,idStudent,idDisciplina,Valoarea)
        self.__noteRepository.adauga(nota)

    def cauta(self,idNota):
        '''
        cauta note
        :param idNota:
        :return:
        '''
        return self.__noteRepository.cauta(idNota)

    def ordonare(self):
        lista = []
        note = self.__noteRepository.getAll()
        for nota in note:
            elev_nota = nota.Valoarea
            student = self.__studentRepository.cauta(nota.idStudent)
            dictionar = {'student': student, 'nota':elev_nota}
            lista.append(dictionar)
        return lista

    def primii_20_la_suta(self):
        listafinala=[]
        lista = []
        medie=0
        nr=0
        note=self.__noteRepository.getAll()
        for nota in note:
            medie+=int(nota.Valoarea)
            nr=nr+1
            student=self.__studentRepository.cauta(nota.idStudent)
            dictionar={'student':student}
            lista.append(dictionar)
        media=medie/nr
        lista.append(media)
        return lista

    def write(self):
        self.__noteRepository.write()

    def read(self):
        self.__noteRepository.read()






