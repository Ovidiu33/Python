from domeniu.student import Student
from repository.studentRepository import StudentRepository

class StudentService:
    def __init__(self, studentRepository: StudentRepository):
        self.__studentRepository = studentRepository

    def getById(self):
        '''
        lista de studenti dupa id
        :return:
        '''
        return self.__studentRepository.getById()

    def getAllStudenti(self):
        '''
        :return: studentii
        '''
        return self.__studentRepository.getAll()

    def adauga(self, idStudent, nume):
        '''
        adauga student
        :param idStudent:
        :param nume:
        :return:
        '''
        student = Student(idStudent, nume)
        self.__studentRepository.adauga(student)

    def modifica(self, idStudent, numeNou):
        '''
        modifica student
        :param idStudent:
        :param numeNou:
        :return:
        '''
        studentNou =Student(idStudent, numeNou)
        self.__studentRepository.modifica(studentNou)

    def sterge(self, idStudent):
        '''
        sterge student
        :param idStudent:
        :return:
        '''
        self.__studentRepository.sterge(idStudent)

    def cauta(self, idStudent):
        '''
        cauta student
        :param idStudent:
        :return:
        '''
        return self.__studentRepository.cauta(idStudent)

    def write(self):
        self.__studentRepository.write()

    def read(self):
        self.__studentRepository.read()

