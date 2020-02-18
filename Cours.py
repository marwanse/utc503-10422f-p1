class cours:
    def __init__(self , Code_Cours , Intitule_Cours , Niveau_Cours):

        assert Niveau_Cours == 'A' or Niveau_Cours == 'B' or Niveau_Cours == 'C'

        self.Code_Cours = Code_Cours
        self.Intitule_Cours = Intitule_Cours
        self.Niveau_Cours = Niveau_Cours

    def __str__(self):
        return "Code %s , Intitule %s , Niveau %s" %(self.Code_Cours , self.Intitule_Cours , self.Niveau_Cours)
    
    def get_Cours(self):
        """Getter for Cours"""
        return (self.Code_Cours , self.Intitule_Cours , self.Niveau_Cours)

    def set_Cours(self, Code , Intitule , Niveau):
        """Setter for Cours"""
        
        self.Code_Cours = Code
        self.Intitule_Cours = Intitule
        self.Niveau_Cours = Niveau