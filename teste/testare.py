import unittest

from domeniu.student import Student
from domeniu.disciplina import Disciplina
from repository.disciplinaRepository import DisciplinaRepository
from repository.studentRepository import StudentRepository
from service.DisciplinaService import DisciplinaService
from service.StudentService import StudentService


class Teste(unittest.TestCase):

    def test_get_id_student(self):
        student1 = Student("1", "Taciuc Ovidiu")
        self.assertTrue(student1.getIdStudent()=="1")

    def test_get_id_disciplina(self):
        dis1=Disciplina("1","Matematica","Miron")
        self.assertTrue(dis1.getIdDisciplina()=="1")

    def test_get_nume_student(self):
        student1=Student("1","Adi")
        self.assertTrue(student1.getnume()=="Adi")

    def test_get_nume_dis(self):
        dis1=Disciplina("1","Matematica","Miron")
        self.assertTrue(dis1.getNumeDisciplina()=="Matematica")

    def test_get_prof(self):
        dis1 = Disciplina("1", "Matematica", "Miron")
        self.assertTrue(dis1.getprofesor()=="Miron")

    def test_set_nume_student(self):
        student1=Student("1","Adi")
        student1.setnume("Ovidiu")
        self.assertTrue(student1.getnume()=="Ovidiu")

    def test_set_nume_dis(self):
        dis1 = Disciplina("1", "Matematica", "Miron")
        dis1.setnumeDisciplina("Romana")
        dis1.setnumeDisciplina(dis1.getNumeDisciplina()=="Romana")

    def test_set_id(self):
        student1=Student("1","Adi")
        student1.setIdStudent("2")
        self.assertTrue(student1.getIdStudent()=="2")

    def test_set_id_dis(self):
        dis1 = Disciplina("1", "Matematica", "Miron")
        dis1.setIdDisciplina("2")
        dis1.setIdDisciplina(dis1.getIdDisciplina()=="2")

    def test_set_prof_dis(self):
        dis1 = Disciplina("1", "Matematica", "Miron")
        dis1.setprofesor("Pelea")
        dis1.setprofesor(dis1.getprofesor()=="Pelea")

    def test_adauga_student(self):
        id_student = "1"
        nume = "Spac"
        student = Student(id_student, nume)
        repo_student = StudentRepository()
        service_student = StudentService(repo_student)
        service_student.adauga(id_student, nume)
        nume_acelasi = "Teo"
        with self.assertRaises(KeyError) as context:
            service_student.adauga(id_student, nume_acelasi)
        self.assertTrue("Exista deja un stiudent cu id ul acesta" in str(context.exception))


    def test_modifica_student(self):
        id_student = "1"
        nume = "Spac"
        numenou="Ovidiu"
        stud = Student(id_student, nume)
        studn = Student(id_student, numenou)
        repo = StudentRepository()
        repo.adauga(stud)
        repo.modifica(studn)
        lst = repo.getAll()
        student = lst[0]
        self.assertEqual(student.getnume(), "Ovidiu")

    def test_cauta_student(self):
        id_student= "1"
        nume="Adi"
        id_cautat="1"
        student=Student(id_student,nume)
        repo = StudentRepository()
        repo.adauga(student)
        repo.cauta(id_cautat)
        self.assertTrue(student.getIdStudent(),"1")


    def test_sterge_student(self):
        id_student="1"
        nume="Adi"
        student=Student(id_student,nume)
        repo=StudentRepository()
        repo.adauga(student)
        repo.sterge(id_student)
        self.assertTrue(student.getIdStudent(),' ')

    def test_adauga_disciplina(self):
        id_disciplina="1"
        numeDisciplina = "Matematica"
        profesor="Miron"
        disciplina=Disciplina(id_disciplina,numeDisciplina,profesor)
        repo_disciplina=DisciplinaRepository()
        service_disciplina = DisciplinaService(repo_disciplina)
        service_disciplina.adauga(id_disciplina,numeDisciplina,profesor)
        nume_acelasi = "Teo"
        prfn="Mihai"
        with self.assertRaises(KeyError) as context:
            service_disciplina.adauga(id_disciplina,nume_acelasi,prfn)
        self.assertTrue("Exista deja un stiudent cu id ul acesta" in str(context.exception))

    def test_sterge_disciplina(self):
        id_disciplina ="2"
        numeDisciplina="Matematica"
        profesor = "Miron"
        disciplina = Disciplina(id_disciplina,numeDisciplina,profesor)
        repo = DisciplinaRepository()
        repo.adauga(disciplina)
        repo.sterge(id_disciplina)
        self.assertTrue(disciplina.getIdDisciplina(), ' ')

    def test_cauta_disciplina(self):
        id_disciplina = "2"
        id_cautat = "2"
        numeDisciplina = "Matematica"
        profesor = "Miron"
        disciplina = Disciplina(id_disciplina, numeDisciplina, profesor)
        repo = DisciplinaRepository()
        repo.adauga(disciplina)
        repo.cauta(id_cautat)
        self.assertTrue(disciplina.getIdDisciplina(), "2")

    def test_modificad(self):
        id_disciplina = "2"
        numeDisciplina = "Matematica"
        profesor = "Miron"
        numeDisciplinan = "Romana"
        profesorn = "Samo"
        disciplina = Disciplina(id_disciplina, numeDisciplina, profesor)
        disciplinan = Disciplina(id_disciplina, numeDisciplinan, profesorn)
        repo = DisciplinaRepository()
        repo.adauga(disciplina)
        repo.modifica(disciplinan)
        self.assertTrue(disciplinan.getIdDisciplina(),"2")












