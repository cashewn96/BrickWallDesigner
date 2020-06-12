import tkinter as tk
from tkinter import messagebox
frame=tk.Tk()
L=tk.Label(frame)
 
frame.title("Wall-Design")
pic=tk.PhotoImage(file="site.gif")
w = pic.width()
h = pic.height()
frame.geometry('%dx%d+0+0' % (w,h))
tk.Label(frame,image=pic,bg="gray").grid(row=1,column=1)

tk.Label(frame,text="Designing a Masonry Wall Under Vertical Loads According To Eurocode 6",fg="red",font="none 12 bold").place(x=150, y=0)

tk.Label(frame,text=" Load on top of the wall:                     kN/m",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=60)
e=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e.place(x=270,y=60)


tk.Label(frame,text=" Load on top of the wall:                    kN/m",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=60)
e1=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e1.place(x=300,y=60)

tk.Label(frame,text="Load at mid height of the wall:         kN/m",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=100)
e2=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e2.place(x=300,y=100)

tk.Label(frame,text="Load at bottom of the wall:               kN/m",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=140)
e3=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e3.place(x=300,y=140)



tk.Label(frame,text="Design permanent load on slab:   kN/m^2",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=180)
e4=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e4.place(x=300,y=180)

tk.Label(frame,text="Design total load on slab:            kN/m^2",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=220)
e5=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e5.place(x=300,y=220)

tk.Label(frame,text="Effective thickness of the wall:             m",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=260)
e6=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e6.place(x=300,y=260)

tk.Label(frame,text="Exact thickness of the wall:                    m",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=300)
e7=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e7.place(x=300,y=300)

tk.Label(frame,text="Slab thickness:                                       m",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=340)
e8=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e8.place(x=300,y=340)

tk.Label(frame,text="Effective height of the wall :                     m",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=380)
e9=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e9.place(x=300,y=380)


tk.Label(frame,text="Clear span to upper floor:                         m",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=420)
e10=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e10.place(x=300,y=420)


tk.Label(frame,text="Clear span to lower floor :                        m",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=460)
e11=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e11.place(x=300,y=460)


tk.Label(frame,text="Elastic modulus of masonry:      kN/mm^2",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=500)
e12=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e12.place(x=300,y=500)


tk.Label(frame,text="Elastic modulus of concrete:      kN/mm^2",fg="sienna4",font="TkTooltipFont 12").place(x=10, y=540)
e13=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e13.place(x=300,y=540)


tk.Label(frame,text="Enter length of slab part 1 :                      m",fg="sienna4",font="TkTooltipFont 12").place(x=510, y=60)
e14=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e14.place(x=800,y=60)


tk.Label(frame,text="Length of slab part 2:                               m",fg="sienna4",font="TkTooltipFont 12").place(x=510, y=100)
e15=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e15.place(x=800,y=100)


tk.Label(frame,text="Plaster thickness:                                     m",fg="sienna4",font="TkTooltipFont 12").place(x=510, y=140)
e16=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e16.place(x=800,y=140)



tk.Label(frame,text="Partial factor of safety",fg="sienna4",font="TkTooltipFont 12").place(x=510, y=180)
e17=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e17.place(x=800,y=180)


tk.Label(frame,text="K value: ",fg="sienna4",font="TkTooltipFont 12").place(x=510, y=220)
e18=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e18.place(x=800,y=220)


tk.Label(frame,text="Alpha: ",fg="sienna4",font="TkTooltipFont 12").place(x=510, y=260)
e19=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e19.place(x=800,y=260)

tk.Label(frame,text="Beeta:",fg="sienna4",font="TkTooltipFont 12").place(x=510, y=300)
e20=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e20.place(x=800,y=300)

tk.Label(frame,text="Design strength of mortar:             N/mm^2",fg="sienna4",font="TkTooltipFont 12").place(x=510, y=340)
e21=tk.Entry(frame,bg='white',fg='blue',borderwidth=3,width=10)
e21.place(x=800,y=340)

def close():
   frame.destroy()
   exit()
   
def clear():
   L.destroy()
   e1.delete(0,'end')
   e2.delete(0,'end')
   e3.delete(0,'end')
   e4.delete(0,'end')
   e5.delete(0,'end')
   e6.delete(0,'end')
   e7.delete(0,'end')
   e8.delete(0,'end')
   e9.delete(0,'end')
   e10.delete(0,'end')
   e11.delete(0,'end')
   e12.delete(0,'end')
   e13.delete(0,'end')
   e14.delete(0,'end')
   e15.delete(0,'end')
   e16.delete(0,'end')
   e17.delete(0,'end')
   e18.delete(0,'end')
   e19.delete(0,'end')
   e20.delete(0,'end')
   e21.delete(0,'end')

def Click():
   global L
   L.destroy()
    
   try:
      top_load=float(e1.get())
      mid_load=float(e2.get())
      bottom_load=float(e3.get())
      perma_load_slab=float(e4.get())
      tot_load_slab=float(e5.get())
      
      eff_t=float(e6.get())
      t=float(e7.get())
      Slab_t=float(e8.get())
      eff_h=float(e9.get())
      h_1=float(e10.get())
      h_2=float(e11.get())
      E_1=float(e12.get())
      E_2=float(e13.get())
      L_1=float(e14.get())
      L_2=float(e15.get())
      plaster=float(e16.get())
      Gamma=float(e17.get())
      K=float(e18.get())
      alpha=float(e19.get())
      beeta=float(e20.get())
      f_m=float(e21.get())
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
      ans=round(c,5)
      
      L=tk.Label(frame,text="Characteristic strength of brick = "+str(c)+"N/mm^2",bg="gold",fg="blue4",font="TkTooltipFont 16")
      L.place(x=20, y=600)
 
          
   except:
      L=tk.Label(frame,text="ERROR",bg="red",fg="blue4",font="TkTooltipFont 16")
      L.place(x=400, y=600)
      
      tk.messagebox.showerror('Input Error','Plese Enter the Correct values')

      
   
   
tk.Button(frame,text="CALCULATE",width=15,height=2,bg='Deeppink',fg='blue',font="TkTooltipFont 14",command=Click).place(x=600,y=450)
tk.Button(frame,text="EXIT",width=15,bg="orange",font=('comicsans', 8),command=close).place(x=820, y=600)
tk.Button(frame,text="CLEAR",width=15,bg="cyan",font=('comicsans', 8),command=clear).place(x=820, y=540)





