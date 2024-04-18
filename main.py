from repository.studentRepository import StudentRepository
from service.StudentService import StudentService
from repository.disciplinaRepository import DisciplinaRepository
from service.DisciplinaService import DisciplinaService
from repository.noteRepository import NoteRepository
from service.NoteService import NoteService
from ui.consola import Consola

def main():
    studentRepository=StudentRepository()
    studentService=StudentService(studentRepository)
    disciplinaRepository=DisciplinaRepository()
    disciplinaService=DisciplinaService(disciplinaRepository)
    notaRepository=NoteRepository()
    notaService=NoteService(notaRepository,studentRepository,disciplinaRepository)
    consola=Consola(studentService,disciplinaService,notaService)
    consola.meniu()



main()