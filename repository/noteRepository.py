from domeniu.note import note
class NoteRepository:
    def __init__(self):
        self.__note={}

    def getAll(self):
        '''
        returneaza lista de note
        :return: o lista de obiecte de tipul nota
        '''
        return list(self.__note.values())

    def getById(self, idNota):
        '''
        returneaza disciplina cu id ul cerut
        :param idNota:
        :return: obiect
        '''
        if idNota in self.__note:
            return self.__note[idNota]
        return None
    def adauga(self,nota):
        '''
        adauga o nota in dictionar
        :param nota:
        :return: obiect de tip nota
        '''
        if self.getById(nota.idNota) is not None:
            raise KeyError("Exista deja un stiudent cu nota aceasta")
        self.__note[nota.idNota] = nota

    def cauta(self,iDCautat):
        '''
        cauta o nota dupa id
        :param iDCautat:
        :return:obiect
        '''
        if self.getById(iDCautat) is None:
            raise KeyError("nu exista o nota cu id ul acesta")
        return self.getById(iDCautat)

    def write(self):
        save_file = open("note.txt", "w")

        lista = []

        for note in self.getAll():
            lista.append(note.__dict__)

        save_file.write(str(lista))


    def read(self):
        save_file = open("note.txt", "r")
        self._note = {}
        lista = list(eval(save_file.read()))

        for std in lista:
            self._note[std["_note__idNota"]] = note(std["_note__idNota"], std["_note__idStudent"], std["_note__idDisciplina"], std["_note__Valoarea"])