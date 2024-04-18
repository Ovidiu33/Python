from service.StudentService import  StudentService
from service.DisciplinaService import DisciplinaService
from service.NoteService import NoteService

class Consola:
    def __init__(self,studentService:StudentService,disciplinaService:DisciplinaService,noteService:NoteService):
        self.__studentService=studentService
        self.__disciplinaService=disciplinaService
        self.__noteService=noteService


    def adaugaStudent(self):
        try:
            idStudent =input("Dati id ul studentului:")
            try:
                int(idStudent)
            except:
                print("Introduceti un id de tip int")
                return
            try:
                nume = str(input("Dati numele studentului:"))
            except:
                print("Ati introdus un nume incorect")
                return
            self.__studentService.adauga(idStudent,nume)
        except KeyError as e:
            print(e)

    def adauga_din_fisier(self):
        fisier=open("student.txt","r")
        print(self.adaugaStudent(fisier))
        fisier.close()
    def adaugaDisciplina(self):
        try:
            idDisciplina=input("Dati id ul discipline:")
            numeDisciplina=input("Dati numele disciplinei")
            profesor=input("Dati numele profesorului")
            self.__disciplinaService.adauga(idDisciplina,numeDisciplina,profesor)
        except KeyError as e:
            print(e)
    def adaugaNota(self):
        try:
            idNota=input("Dati id ul notei:")
            idStudent=input("Dati id ul studentului:")
            idDisciplina=input("Dati id ul disciplinei:")
            Valoarea=input("Dati valoarea notei")
            self.__noteService.adauga(idNota,idStudent,idDisciplina,Valoarea)
        except KeyError as e:
            print(e)

    def modfificaDisciplina(self):
        try:
            idDisciplina= input("Dati id ul disciplinei de modificat:")
            numeNou=input("Dati numele nou al materiei:")
            numeNouP=input("Dati numele profesorului")
            self.__disciplinaService.modifica(idDisciplina,numeNou,numeNouP)
        except KeyError as e:
            print(e)

    def modificaStudent(self):
        try:
            idStudent= input("Dati id ul studentului de modificat:")
            numeNou=input("Dati numele nou al studentului:")
            self.__studentService.modifica(idStudent,numeNou)
        except KeyError as e:
            print(e)

    def stergeD(self):
        try:
            idDisciplina = input("Dati id ul disciplinei de sters:")
            self.__disciplinaService.sterge(idDisciplina)
        except KeyError as e:
            print(e)

    def sterge(self):
        try:
            idStudent = input("Dati id ul studentului de sters:")
            self.__studentService.sterge(idStudent)
        except KeyError as e:
            print(e)

    def afiseaza(self,entitati):
        for entitate in entitati:
            print(entitate)

    def cauta(self):
        try:
            idStudentdeCautat= input("Dati id ul studentului pe care il cautati")
            print(self.__studentService.cauta(idStudentdeCautat))
        except KeyError as e:
            print(e)
    def cautaD(self):
        try:
            idDisciplinadeCautat= input("Dati id ul disciplinei pe care o cautati")
            print(self.__disciplinaService.cauta(idDisciplinadeCautat))
        except KeyError as e:
            print(e)

    def ordoneaza(self):
        print(self.__noteService.ordonare())
    def primii20(self):
        print(self.__noteService.primii_20_la_suta())

    def adauga_din_fisier_student(self):
        self.__studentService.read()

    def scrie_in_fisier_student(self):
        self.__studentService.write()

    def adauga_din_fisier_disciplina(self):
        self.__disciplinaService.read()

    def scrie_in_fisier_disciplina(self):
        self.__disciplinaService.write()

    def adauga_din_fisier_note(self):
        self.__noteService.read()

    def scrie_in_fisier_note(self):
        self.__noteService.write()

    def printMeniu(self):
        print("Lab 7-9")
        print(' ')
        print("1.Adauga Student")
        print("2.Adauga Disciplina")
        print("3.Modifica student")
        print("4.Modifica disciplina")
        print("5.Sterge student")
        print("6.Sterge disciplina")
        print("7.Afiseaza toti studentii")
        print("8.Afiseaza discipline")
        print("9.Cauta student")
        print("10.Cauta disciplina")
        print("11.Adaugare nota")
        print("12.Afisare note")
        print("13.Ordonare")
        print("14.Primii 20 la suta")
        print("15.Adaugare din fisier student")
        print("16.Scrie in fisier student ")
        print("17.Adaugare din fisier disciplina")
        print("18.Scrie in fisier disciplina ")
        print("19.Adaugare din fisier note")
        print("20.Scrie in fisier note ")
        print("x.Exit")

    def meniu(self):
        while True:
            self.printMeniu()
            optiune= input("Dati optiune:")
            if optiune == "1":
                self.adaugaStudent()
            elif optiune== "2":
                self.adaugaDisciplina()
            elif optiune == "3":
                self.modificaStudent()
            elif optiune == "4":
                self.modfificaDisciplina()
            elif optiune =="5":
                self.sterge()
            elif optiune=="6":
                self.stergeD()
            elif optiune =="7":
                self.afiseaza(self.__studentService.getAllStudenti())
            elif optiune =="8":
                self.afiseaza(self.__disciplinaService.getAllDiscipline())
            elif optiune =="9":
                self.cauta()
            elif optiune=="10":
                self.cautaD()
            elif optiune=="11":
                self.adaugaNota()
            elif optiune=="12":
                self.afiseaza(self.__noteService.getAllNote())
            elif optiune=="13":
                self.ordoneaza()
            elif optiune == "14":
                self.primii20()
            elif optiune == "15":
                self.adauga_din_fisier_student()
            elif optiune == "16":
                self.scrie_in_fisier_student()
            elif optiune == "17":
                self.adauga_din_fisier_disciplina()
            elif optiune == "18":
                self.scrie_in_fisier_disciplina()
            elif optiune == "19":
                self.adauga_din_fisier_note()
            elif optiune == "20":
                self.scrie_in_fisier_note()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita,reincercati")


