""""""""""""""""""""""""""""""""""""""""""""""
1) jeu de cartes
2) classer les mots par ordres alphabetics
3) classer des notes du bac
4) comptes bancaires
""""""""""""""""""""""""""""""""""""""""""""""







def tri(A):
    n=len(A)
    for i in range(n):
        for j in range(n):
            if A[i] >= A[j] and i <= j:
                A[i] ,A[j] = A[j] , A[i]
    return A





test(a)
Ce code il marche :


def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j

       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab

tab = [98, 22, 15, 32, 2, 74, 63, 70]

tri_selection(tab)

print("Le tableau trié est:")
for i in range(len(tab)):
    print ("%d" %tab[i])





def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j

       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab

tab = []
for i in range(0,5):
    a = input("Entre vos notes du bac : ")
    a = int(a)
    tab.append(a)

tri_selection(tab)

print("Vos notes du bac sont maintenant triés:")
for i in range(len(tab)):
    print ("%d" %tab[i])




    "TRI PAR INSERTION QUI MARCHE"

# Programme Python pour l'implémentation du tri par insertion
def tri_insertion(tab):
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k
# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]
tri_insertion(tab)
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("% d" % tab[i])











"TRI PAR SELECTION QUI MARCHE"

def tri_insertion(tab):
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k

tab = []
for i in range(0,5):
    a = input("Entrez vos notes du bac : ")
    a = int(a)
    tab.append(a)

tri_insertion(tab)

print ("Vos notes du bac sont maintenant triés:")
for i in range(len(tab)):
    print ("% d" % tab[i])