tab = [] #Tableau vide
def tri_selection(tab): # Fonction qui a pour nom tri_selection et pour argument tab
   for i in range(len(tab)):#boucle longueur du tableau
      # Trouver le min
       min = i # le minimum est égal a i
       for j in range(i+1, len(tab)):#pour i entre x+1 et la longueur du tableau
           if tab[min] > tab[j]:# Si longueur du tableau est supérieur a l'élement j
               min = j #le minimum est = j

       tmp = tab[i] # tmp = au plus petit élement du tableau
       tab[i] = tab[min] # l'element i du tableau est égal au plus petit élement du tableau
       tab[min] = tmp # le plus petit élement du tableau est égal tmp
   return tab #sa renvoi au tableau

def activate_selection(tab): #Active la fonction tri selection
    tab = [] #tableau vide
    for i in range(0,5): # Pour i entre 0 et 5
        a = input("Entre un nombre : ") # Sa renvoi entre un nombre
        a = int(a) # A est égal a un nombre entier
        tab.append(a) #sa ajoute a la liste les notes qui ont été rentrer par l'utlisateur dans le input
    tri_selection(tab) #sa appelle la fonction du tab
    print("Le tableau trié est:") # Sa affiche que le tableau est trié
    for i in range(len(tab)): # # i est égal al la longueur du tableau / pour i de 0 à 5 (la longueur du tableau)
        print ("%d" %tab[i])

def tri_insertion(tab): #  Fonction qui a pour nom tri_insertion et qui a pour argument tab
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): # pour i de 1 à la longueur du tableau.
        k = tab[i] # k est égal au plus petit élement du tableau
        j = i-1 # J est égal a i-1
        while j >= 0 and k < tab[j] : # Tant que j est supérieur ou égal a 0 et K inférieur au tableau j
                tab[j + 1] = tab[j] # Alors le tableau j + 1 est égal au tabbleau J
                j -= 1 # j = 1
        tab[j + 1] = k # l'element j du tableau + 1 est égal a k

def activate_insertion(tab): #Active la fonction tri insertion
    tab = [] # Tableau vide
    for i in range(0,5): # Pour i entre 0 et 5
        a = input("Entre un nombre : ") # Sa affiche Entre un nombre
        a = int(a) # A est égal a un nombre sans virgule
        tab.append(a) # Au tableau est ajouter a
    tri_insertion(tab) # Sa rappelle la fonction tri par insertion
    print ("Le tableau trié est:") # Sa affiche que le tableau est trié
    for i in range(len(tab)): # i est égal al la longueur du tableau / pour i de 0 à 5 (la longueur du tableau)
        print ("% d" % tab[i])