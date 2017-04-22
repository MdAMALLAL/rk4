# <summary>
# promière séance
# <summary>
#
# fixation des valeurs :
k1 , t0 , A0 , Dt = 0.1, 0, 0.01, 0.05

# Calculation de t1 :
t1 = t0 + Dt

# Calculation de t2 :
t2 = t0 + Dt

# Calculation de [A]2:
A1 = A0 + Dt * ( - k1 * A0 )

# Calculation de [A]2:
A2 = A1 + Dt * ( - k1 * A1 )

#Affichage des valeurs
print('t0 = ', t0, 's -- [A]0 = ', A0, 'mol/L')
print('t1 = ', t1, 's -- [A]1 = ', A1, 'mol/L')
print('t2 = ', t2, 's -- [A]2 = ', A2, 'mol/L')
