Class Guichetieres(Banque):
     def __init__(self,nomGuichetiere,prenomGuichetiere,poste):
          
          self.nom= nomGuichetiere
          self.prenom= prenomGuichetiere
          self.poste= poste
          return "Guichetier:nom{0},prenom{1},poste{2}".format(self.nom,self.prenom,self.poste)
          guichetier=guichetier("Ousmanou","Amadou",12)
          Banque.__init__(self,nomGuichetuier,prenomGuichetier)
          self.poste= poste

Nom:Ousmanou alhadji Amadou 
Matricule :18A885FS
