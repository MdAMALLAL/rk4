# <summary>
# A = B + C
# <summary>
#
import matplotlib.pylab as plt

def fA(k1, a):
    return - k1 * a


def fB(k1, a, k2, b):
    return k1 * a - k2 * b


def rk4(Ai, Bi, Ci, k1, k2, Dt, t0):

    ti = t0
    i = 0
    #stocker des valeurs initial
    a0, b0, c0 = Ai, Bi, C0
    bmax = 0
    tbmax = 0

    # le variable tmax contient le temps maximum 
    tmax = 100

    while ti <= tmax::
        print('t%3.f =  %3.3f s -- [A]%3.f = %3.9f mol/L -- [B]%3.f = 
%3.9f mol/L -- [C]%3.f  = %3.9f mol/L' % (i, ti, i, Ai, i, Bi, i, Ci))

        # Sauvegarder les valeurs de t, [A], [B] et [C]
        lt.append(ti)
        lA.append(Ai)
        lB.append(Bi)
        lC.append(Ci)


        # calculation des quantités intermidiaires pour A
        AS1 = Dt * fA(-k1, Ai)s
        AS2 = Dt * fA(-k1, Ai + 1 / 2 * AS1)
        AS3 = Dt * fA(-k1, Ai + 1 / 2 * AS2)
        AS4 = Dt * fA(-k1, Ai + AS3)

        # calculation des quantités intermidiaires pour B
        BS1 = Dt * fA(k1, Bi)s
        BS2 = Dt * fA(k1, Bi + 1 / 2 * BS1)
        BS3 = Dt * fA(k1, Bi + 1 / 2 * BS2)
        BS4 = Dt * fA(k1, Bi + BS3)

        # calculation des quantités intermidiaires pour C
        CS1 = Dt * fA(k1, Ci)s
        CS2 = Dt * fA(k1, Ci + 1 / 2 * CS1)
        CS3 = Dt * fA(k1, Ci + 1 / 2 * CS2)
        CS4 = Dt * fA(k1, Ci + BS3)





        # Claculation de [A]i+1, [B]i+1 et [C]i+1 en utilisant les meme variable Ai, Bi et Ci
        A = Ai
        Ai = Ai + 1 / 6 * (AS1 + 2 * AS2 + 2 * AS3 + AS4)
        Bi = Bi + 1 / 6 * (BS1 + 2 * BS2 + 2 * BS3 + BS4)
        Ci = Ci + 1 / 6 * (CS1 + 2 * CS2 + 2 * CS3 + CS4)


         #Arrette  de RK4 de i
        if Ai - A == 10**-8:
            print('le temps tbmax =', tbmax)
            break

        # incrementation de i
        i = i + 1
        ti = t0 + i * Dt


# ici listet sera represanter par la liste de ti
# et listeC par liste des con
def ecriture_fichier(fichier, listet, listeC, c):

    # ouvrir le fichier
    f = open(fichier, 'w')

    for index in range(len(listeC)):
        # ecrire dans le fichier
        f.write('t%3.f =  %3.3f s -- [%s]%3.f = %3.9f mol.L-1 \n' % 
(index, lt[index], c, index, listeC[index]))

    # fermer le fichier
    f.close()
    return f


def visuel(listt, listC, label):
    plt.plot(listt, listC, 'r-', label=label)
    plt.show()
    plt.save()


#
#
#
# le programme principal
#
#
#
#
# fixation des valeurs :


t0, Dt = 0, 0.05

# Declaration de list

lt = []
lA = []
lB = []
lC = []

#le choix de l'utilisateur
A0 = float(input('Choisir la valeur de [A]0:  '))
B0 = float(input('Choisir la valeur de [B]0:  '))
C0 = float(input('Choisir la valeur de [C]0:  '))

K1 = float(input('Choisir la valeur de [K]1:  '))
K2 = float(input('Choisir la valeur de [K]2:  '))

# boucle RK4
rk4(A0, B0, C0, K1, K2, Dt, t0)

# ouvrir le fichier
ecriture_fichier('DATA_A.txt', lt, lA, 'A')
ecriture_fichier('DATA_B.txt', lt, lB, 'B')
ecriture_fichier('DATA_C.txt', lt, lC, 'C')

visuel(lt, lA,'[A](t)')
visuel(lt, lB,'[B](t)')
visuel(lt, lC,'[C](t)')
