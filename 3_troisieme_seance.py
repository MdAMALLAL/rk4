# <summary>
# deuxiéme séance
# <summary>


# fixation des valeurs :
k1 , k2 = 0.1, 0.05
t0 , Dt =0, 0.05
i = 0
B0, Bi, C0, Ci = 0, 0, 0, 0

tBMax = 0
BMax = 0
tMax = 10
# Declaration de list

lt = []
lA = []
lB = []
lC = []



#le choix de [A]
A0 = float(input('Choisir la valeur de [A]0:  '))

#initialisation
Ai = A0
ti = t0

# ouvrir le fichier
fichier = open('data.txt', 'w')


# boucle RK4
while 1:
    print('t0 =  %3.3f s -- [A]%3.f = %3.3f mol/L -- [B]%3.f = %3.3f mol/L -- [C]%3.f  = %3.3f mol/L' %(ti, i, Ai, i, Bi, i, Ci ))

    #Sauvegarder les valeurs de t, [A], [B] et [C]
    lt.append(ti)
    lA.append(Ai)
    lB.append(Bi)
    lC.append(Ci)



    #ecrire dans le fichier
    fichier.write('t0 =  %3.3f s -- [A]%3.f = %3.3f mol.L-1 \n' %(ti, i, Ai ) )



    #calculation des quantités intermidiaires pour A
    AS1 = Dt * ( -k1 * Ai)
    AS2 = Dt * ( -k1 * (Ai + 1/2*AS1))
    AS3 = Dt * ( -k1 * (Ai + 1/2*AS2))
    AS4 = Dt * ( -k1 * (Ai + AS3))

    #calculation des quantités intermidiaires pour B
    BS1 = Dt * ( k1 * Ai - k2 * Bi)
    BS2 = Dt * ( k1 * (Ai + 1/2*AS2) - k2 * (Bi + 1/2 * BS1 ))
    BS3 = Dt * ( k1 * (Ai + 1/2*AS2) - k2 * (Bi + 1/2 * BS2 ))
    BS4 = Dt * ( k1 * (Ai + 1/2*AS3) - k2 * (Bi + 1/2 * BS3 ))

    #Claculation de [A]i+1, [B]i+1 et [C]i+1 en utilisant les meme variable Ai, Bi et Ci
    A = Ai
    Ai = Ai + 1/6 * (AS1 + 2 * AS2 + 2 + AS3 + AS4 )
    Bi = Bi + 1/6 * (BS1 + 2 * BS2 + 2 + BS3 + BS4 )
    Ci = A0 + B0 + C0 - Ai - Bi

    # Detrmination de Bmax
    if BMax < Bi :
        BMax = Bi

    #Arrette  de RK4 de i
    if Ai - A == 10**(-8):
       tBMax = ti
       break


    # incrementation de i
    i = i + 1
    ti = t0 + i * Dt

#fermer le fichier
fichier.close()
