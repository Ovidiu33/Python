from service.StudentService import StudentService
from repository.studentRepository import StudentRepository
from domeniu.student import Student
from service.DisciplinaService import DisciplinaService
from repository.disciplinaRepository import DisciplinaRepository
from domeniu.disciplina import Disciplina

def test_student():
    student1 = Student(1, "Taciuc Ovidiu")
    assert student1.getIdStudent() == 1
    assert student1.getnume() == "Taciuc Ovidiu"
    student1.setIdStudent(2)
    student1.setnume("Spac Alex")
    assert student1.getIdStudent() == 2
    assert student1.getnume() == "Spac Alex"

def test_disciplina():
    disciplina1=Disciplina(1, "Matematica", "Andrei")
    assert disciplina1.getIdDisciplina() == 1
    assert disciplina1.getNumeDisciplina()=="Matematica"
    assert disciplina1.getprofesor()=="Andrei"
    disciplina1.setIdDisciplina(2)
    disciplina1.setnumeDisciplina("Romana")
    disciplina1.setprofesor("Ovidiu")
    assert disciplina1.getIdDisciplina()==2
    assert disciplina1.getNumeDisciplina()=="Romana"
    assert disciplina1.getprofesor()=="Ovidiu"

def test_student_repository():
    repository = StudentRepository()
    #assert len(StudentRepository.getAll()) == 0
    student1 = Student(1, "Taciuc Ovidiu")
    repository.adauga(student1)
    #assert len(StudentRepository.getAll()) == 1

def test_disciplina_repository():
    repositoryy=DisciplinaRepository()
    disciplina1=Disciplina(1,"mate","miron")
    repositoryy.adauga(disciplina1 )

def test_student_service():
    repository = StudentRepository()
    service = StudentService(repository)
    #assert len(StudentService.getAll()) == 0
    service.adauga(1, "Spac Alex")
    #assert len(StudentService.getAll()) == 1

def teste():
    test_student()
    test_disciplina()
    test_student_repository()
    test_disciplina_repository()
    test_student_service()
    print("Testele sunt Ok")