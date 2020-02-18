from Etudiants import *
from Cours import *

class note(etudiants , cours):

    def __init__(self , Note_Etudiants , Numero_Etudiants , Code_Cours):
        self.Note_Etudiants = Note_Etudiants
        super().__init__(Numero_Etudiants)
        super().__init__(Code_Cours)

    def __str__(self):
        return "Numero %d , Note %d , Code %s" %(self.Numero_Etudiants , self.Note_Etudiants , self.Code_Cours)

    def get_Note(self):
        """Getter for Note"""
        return (self.Numero_Etudiants , self.Note_Etudiants , self.Code_Cours)

    def set_Note(self, Note , Numero , Code):
        """Setter for Note"""
        
        self.Note_Etudiants = Note
        self.Numero_Etudiants = Numero
        self.Code_Cours = Code