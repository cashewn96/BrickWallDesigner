print "Designing a masonry wall under vertical loads according to Eurocode 6"
print " "
print " "
top_load = input('Enter the load on top of the wall in kN/m: ')
mid_load = input('Enter the load at mid height of the wall in kN/m: ')
bottom_load = input('Enter the load at bottom of the wall in kN/m: ')
perma_load_slab = input('Enter the design permanent load on slab in kN/m**2: ')
tot_load_slab = input('Enter the design total load on slab in kN/m**2: ')
eff_t = input('Enter the effective thickness of the wall in m: ')
t = input('Enter the exact thickness of the wall in m: ')
Slab_t = input('Enter the slab thickness in m: ')
eff_h = input('Enter the effective height of the wall in m: ')
h_1 = input('Clear span to upper floor in m: ')
h_2 = input('Clear span to lower floor in m: ')
E_1 = input('Elastic modulus of masonry in kN/mm**2: ')
E_2 = input('Elastic modulus of concrete in kN/mm**2: ')
L_1 = input('Enter length of slab part 1 in m: ')
L_2 = input('Enter length of slab part 2 in m: ')
plaster = input('Enter plaster thickness in m: ')
Gamma = input('Enter the partial factor of safety: ')
K = input('Enter the K value: ')
alpha = input('Enter the alpha: ')
beeta = input('Enter the beeta: ')
f_m = input('Enter the design strength of mortar in N/mm**2: ')





#slend_rat = eff_h/eff_t
e_init = 1
e_init = eff_h/450          #in m
M_excess = 1
M_excess = (tot_load_slab * max(L_1,L_2)**2 - perma_load_slab * min(L_1,L_2)**2)/12         #calculating excess moment using fixed end moments in kNm


M_1d = 1
I_1 = 1
I_1 = (t**3)/12
I_2 = 1
I_2 = (Slab_t**3)/12
M_1d = M_excess*(4*E_1*I_1/h_1)/((4*E_1*I_1/h_1)+(4*E_1*I_1/h_2)+(4*E_2*I_2/L_1)+(4*E_2*I_2/L_2))    #calculating the moment on top of the wall M_1d in kNm

factor = 1
factor = 1-(((E_2*I_2/L_1)+(E_2*I_2/L_2))/(4*(E_1*I_1/h_1)+4*(E_1*I_1/h_2)))

Modi_Mom_top = 1
Modi_Mom_top = factor*M_1d        #in kNm



a = []                 #list to collect the slenderness reduction factors top,mid,bottom

Ecc_top = 1
Ecc_top = Modi_Mom_top/top_load    #in m

Ecc_top_tot = 1
Ecc_top_tot = Ecc_top + e_init
if Ecc_top_tot<0.05*(t+plaster):
    Ecc_top_tot = 0.05*(t+plaster)
else:
    Ecc_top_tot = Ecc_top + e_init
Shy_top = 1
Shy_top = 1-2*(Ecc_top_tot/t)
a.append(Shy_top)



Ecc_bot = 1
Ecc_bot = Modi_Mom_top/(2*bottom_load)   #in m

Ecc_bot_tot = 1
Ecc_bot_tot = Ecc_bot + e_init
if Ecc_bot_tot<0.05*(t+plaster):
    Ecc_bot_tot = 0.05*(t+plaster)
else:
    Ecc_bot_tot = Ecc_bot + e_init
Shy_bot = 1
Shy_bot = 1-2*(Ecc_bot_tot/t)
a.append(Shy_bot)




x = 1           #calculation to find the moment at the mid height of the slab
x = h_1/3
Mom_mid = 1
Mom_mid = Modi_Mom_top*((h_1/2)-x)/((h_1)-x)

Ecc_mid = 1
Ecc_mid = Mom_mid/mid_load     #in m

Ecc_mid_tot = 1
Ecc_mid_tot = Ecc_mid + e_init
if Ecc_mid_tot<0.05*(t+plaster):
    Ecc_mid_tot = 0.05*(t+plaster)
else:
    Ecc_mid_tot = Ecc_mid + e_init


Lambda = 1
Lambda = (eff_h/eff_t)/(1000**0.5)
u = 1
u = (Lambda - 0.063) / (0.73-1.17*Ecc_mid_tot)
A_1 = 1
A_1 = 1-2*(Ecc_mid_tot/2)
Shy_mid = 1
Shy_mid = A_1 ** (Ecc_mid_tot - u**2/2)
a.append(Shy_mid)


Slenderness_Factor = 1
Slenderness_Factor = min(a)     #take the minimum slenderness reduction factor from top,mid,bottom shy values


b = []           #assigning f_k values to the list b

b.append((top_load * Gamma)/(1000* t * Slenderness_Factor))       #f_k value at top
b.append((mid_load * Gamma)/(1000* t * Slenderness_Factor))
b.append((bottom_load * Gamma)/(1000* t * Slenderness_Factor))
#print b

         
c = 1.0
c = (max(b)/(K*f_m**beeta))**(1/alpha)
print 'Characteristic strength of brick in N/mm**2= ',c         

