class etudiants:
    def __init__(self , Numero_Etudiants , Prenom_Etudiants , Nom_Etudiants , Niveaux_Etudiants):

        assert Niveaux_Etudiants == 'A' or Niveaux_Etudiants == 'B' or Niveaux_Etudiants == 'C'

        self.Numero_Etudiants = Numero_Etudiants
        self.Prenom_Etudiants = Prenom_Etudiants
        self.Nom_Etudiants = Nom_Etudiants
        self.Niveaux_Etudiants = Niveaux_Etudiants

    def __str__(self):
        return "%s %s, numero %d , niveau %s" %(self.Prenom_Etudiants, self.Nom_Etudiants,
                                                self.Numero_Etudiants, self.Niveaux_Etudiants)
    
    def get_Etudiants(self):
        """Getter for Etudiants"""
        return (self.Numero_Etudiants , self.Prenom_Etudiants ,
               self.Nom_Etudiants , self.Niveaux_Etudiants)

    def set_Etudiants(self, Num , Pren , Nom , Niveaux):
        """Setter for Etudiants"""
        self.Numero_Etudiants = Num
        self.Prenom_Etudiants = Pren
        self.Nom_Etudiants = Nom
        self.Niveaux_Etudiants = Niveaux