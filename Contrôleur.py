
class Controleurs(Banque):
     def __init__(self,nom,matricule):
         self.nom=nom
         self.matricule=matricule
         return "controleur{0},matricule{1}".format(self.nom,self.matricule)
         controleur=controleur("Aboubakar Ishaga",123-456)
         Banque.__init__(self,nom)#qui fait l'appel au constructeur de la classe mére
         self.matricule=matricule
         #Gestionnaire est aussi recruté de la banque

         #Aboubakar Ishaga 
         #17B593FS
