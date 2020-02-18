import Note
from functools import reduce

class BaseDeDonnees(Note.etudiants , Note.cours , Note.note):

    def __init__(self):
        
        self.List_Etudiants = []
        self.List_Cours = []
        self.List_Note = []    

    def add_Etudiant(self , Numero_Etudiants , Nom_Etudiants , Prenom_Etudiants , Niveaux_Etudiants):
        
        self.List_Etudiants.append(self.Numero_Etudiants , self.Nom_Etudiants , 
                                    self.Prenom_Etudiants , self.Niveaux_Etudiants)
    
    def remove_Etudiants(self , Numero_Etudiants):

        print(self.List_Etudiants)

        self.List_Etudiants.remove(self.Numero_Etudiants , self.Nom_Etudiants , 
                                    self.Prenom_Etudiants , self.Niveaux_Etudiants)

    def modifier_Etudiants(self):

        print(self.List_Etudiants)

        Numero_Etudiants_Modifier = input("Quel est le numero d'etudiant que vous envie d'editer ? ")

        for i in self.List_Etudiants :
            if (i == Numero_Etudiants_Modifier):
                Note.etudiants.set_Etudiants(self, Numero_Etudiants_Modifier , Pren="" , Nom="" , Niveaux="")
    

    def add_Cours(self , Code_Cours , Intitule_Cours , Niveau_Cours):
        
        self.List_Cours.append(self , self.Code_Cours , self.Intitule_Cours , self.Niveau_Cours)
    
    def remove_Cours(self , Code_Cours):

        print(self.List_Cours)

        self.List_Cours.remove(self.Code_Cours , self.Intitule_Cours , self.Niveau_Cours)

    def modifier_Cours(self):

        print(self.List_Cours)

        Code_Cours_Modifier = input("Quel est le code de cours que vous envie d'editer ? ")

        for i in self.List_Cours :
            if (i == Code_Cours_Modifier):
                Note.cours.set_Cours(self, Code_Cours_Modifier , Intitule="" , Niveau="")

    def add_Note(self , Note_Etudiants , Numero_Etudiants , Code_Cours):
        
        self.List_Cours.append(self , self.Note_Etudiants , self.Numero_Etudiants , self.Code_Cours)
    
    def remove_Note(self , Note_Etudiants):

        print(self.List_Note)

        self.List_Note.remove(self.Note_Etudiants , self.Numero_Etudiants , self.Code_Cours)

    def modifier_Note(self):

        print(self.List_Note)

        Note_Modifier = input("Quel est la note que vous envie d'editer ? ")

        for i in self.List_Note :
            if (i == Note_Modifier):
                Note.note.set_Note(self, Note_Modifier , Numero_Etudiants="" , Code_Cours="")


    def moyenne_Classe(self):
        if len(self.List_Note == 0): return -1

        else: return reduce((lambda :(sum(self.List_Note)/len(self.List_Note))), self.List_Note)

    def moyenne_Etudiant(self):
        return reduce((lambda :(sum(self.List_Etudiants)/len(self.List_Etudiants))), self.List_Etudiants)