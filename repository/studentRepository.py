from domeniu.student import Student

class StudentRepository:
    def __init__(self):
        self._student={}

    def getAll(self):
        '''
        returneaza lista de studenti
        :return: o lista de obiecte de tipul student
        :return:
        '''
        return list(self._student.values())

    def getById(self, idStudent):
        '''
        returneaza studentul cu id ul cerut
        :param idStudent:
        :return: obiect
        '''
        if idStudent in self._student:
            return self._student[idStudent].nume
        return None

    def adauga(self,student):
        if self.getById(student.idStudent) is not None:
            raise KeyError("Exista deja un stiudent cu id ul acesta")
        self._student[student.idStudent] = student

    def modifica(self,studentNou):
        '''
        modifica un student dupa id
        :param : studentNou
        :return:obiect de tipul student
        '''
        if self.getById(studentNou.idStudent) is None:
            raise KeyError("Nu exista nici un student cu id ul introdus")
        self._student[studentNou.idStudent]=studentNou

    def sterge(self,idStudent):
        '''
        sterge un student data
        :param idDisciplina:
        :return:
        '''
        if self.getById(idStudent) is None:
            raise KeyError("Nu exista nici un student cu id ul dat")
        self._student.pop(idStudent)

    def cauta(self,iDCautat):
        '''
        cauta un student dupa id
        :param iDCautat:
        :return: obiect de tipul student
        '''
        if self.getById(iDCautat) is None:
            raise KeyError("nu exista un student cu id ul acesta")
        return self.getById(iDCautat)

    def write(self):
        save_file = open("student.txt", "w")

        lista = []
        for student in self.getAll():
            lista.append(student.__dict__)

        save_file.write(str(lista))


    def read(self):
        save_file = open("student.txt", "r")
        self._student = {}
        lista = list(eval(save_file.read()))

        for std in lista:
            self._student[std["_Student__idStudent"]] = Student(std["_Student__idStudent"], std["_Student__nume"])









