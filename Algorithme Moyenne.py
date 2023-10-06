      Algorithme Moyenne
      variable
          N1,N2,N3,M:Réel
      Début 
         ecrire("veuillez entrer les notes:")
         lire(N1,N2,N3)
      Tant que (N1 > 20 or N1<0) or (N2 > 20 or N2 < 0) or (N3 > 20 or N3 < 0)faire
      ecrire("veuillez entrer les notes est:")
      lire(N1,N2,N3)
          M=(N1 +N2 + N3) / 3
      ecrire("la moyenne des notes est:")
      fin tant que
      si M < 10 alors:
        ecrire("insufissant")
      sinon 
         si M >= 10 ou M < 12 alors:
            ecrire("passable")
      sinon
         si M >= 12 ou M < 14 alors:
            ecrire("assez bien")
      sinon 
         si M >= 14 ou M < 16 alors:
            ecrire("bien")
      sinon 
          ecrire("trés bien")
      fin si
    fin si 
   fin si 
  fin si 
fin