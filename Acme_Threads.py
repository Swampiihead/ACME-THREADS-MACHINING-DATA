#acme thread machining data program
#written by Little Lee 25/01/2023

end_menu_choice=0
units=0
tol=0
boxorpin=0
thd_type=0
tol_loop=0
print('\033[1m')
 #user dimensional inputs

while units != 1 and units != 2:
    units = float(input("    Metric [1]   Or   Imperial [2] ? : "))
 #if sets "units" to a value of either 1 or 25.4    
    
nom_dia = float(input("    Nominal Dia. ? : "))
if units == 2:
    nom_dia*=25.4

tpi = float(input("    Threads Per Inch [tpi] ? : "))

#5g tolerance loop
while tol_loop==0:
    if tol==5 and thd_type!=1:
        print('\033[1m' + '\033[91m' +"    5'G' Tolerance Only Used For Acme Not Stub"+"    Choose Again :-\n"+'\033[0m')
        boxorpin=0
        thd_type=0
        tol = int(input("    Tolerence Grade 2,3,4 Or 5 ? : "))
        
    while tol != 2 and tol != 3 and tol != 4 and tol != 5:
        tol = int(input("    Tolerence Grade 2,3,4 Or 5 ? : "))

    while boxorpin != 1 and boxorpin != 2:
        boxorpin = int(input("    Box [1] Or  Pin [2] ? : "))

    while thd_type != 1 and thd_type != 2:
        thd_type = int(input("    Acme [1] Or  Stub-Acme [2] ? : "))
        tol_loop=1
    if tol==5 and thd_type!=1:
        tol_loop=0
        
#c28 f28 f29 f30
c28=1.27/tpi
f28=25.4/tpi
f29=(.0504*(f28**0.5)) + (0.01008*(nom_dia**0.5))
f30=nom_dia**0.5

#b28
if c28<=0.127:
    b28=.127
else:
    b28=c28
    
    #cant figure out squareroot so using **0.5 instead

#b29
if tol==2:
    b29=(.0403*(nom_dia**0.5))
if tol==3:
    b29=(.0302*(nom_dia**0.5))
if tol==4:
    b29=(.0203*(nom_dia**0.5))  
if tol==5:
    b29=(.0002*(nom_dia**0.5))

#b30
if tol==2:
    b30=(3*f29)
if tol==3:
    b30=(1.4*f29)
if tol==4:
    b30=(f29)  
if tol==5:
    b30=(.80134*f29)
    

#b31
if tpi>=12:
    b31=(.254)
if tpi<12:
    b31=(.508)

#b32
if tol==2:
    b32=(4.5*f29)
if tol==3:
    b32=(2.1*f29)
if tol==4:
    b32=(1.5*f29)  
if tol==5:
    b32=(1.2133*f29)
    
#b13
b13=nom_dia-(f28/2)

#b15
b15=nom_dia-f28

#b22
b22=b13

#b24
b24=b15

#g13
g13=nom_dia-(.3*f28)

#g15
g15=nom_dia-(.6*f28)

#g22
g22=g13

#g24
g24=g15

#             Acme box & pin / size calulations
    
#Acme box sizes
if thd_type==1 and boxorpin==1:
    maj_mid=(nom_dia + b31)+(b31/2)
    maj_tol= b31/2
    eff_mid=b22+b30/2
    eff_tol=b30/2
    min_mid=b24+(b28/2)
    min_tol=b28/2
#Acme pin sizes
if thd_type==1 and boxorpin==2:
    maj_mid=nom_dia-(b28/2)
    maj_tol=b28/2
    eff_mid=(b13-b29)-(b30/2)
    eff_tol=b30/2
    min_mid=(b15-b31)-(b32/2)
    min_tol=b32/2
    
    
#        Stub-Acme box & pin / size calculations
    
#Stub-Acme box sizes
if thd_type==2 and boxorpin==1:
    maj_mid=(nom_dia+b31)+(b30/2)
    maj_tol=b30/2
    eff_mid=g22+(b30/2)
    eff_tol=b30/2
    min_mid=g24+(b28/2)
    min_tol=b28/2
#Stub-Acme pin sizes
if thd_type==2 and boxorpin==2:
    maj_mid=nom_dia-(b28/2)
    maj_tol=b28/2
    eff_mid=(g13-b29)-(b30/2)
    eff_tol=b30/2
    min_mid=g15-((b31+b31+b30)/2)
    min_tol=b30/2
    
#thread depth calculation
thd_depth=(maj_mid-min_mid)/2

    
 #           show all results from here   
if units == 2:
        convert_units=25.4
        units_label=str('''"''')
else:
        convert_units=1   
        units_label="mm"

while end_menu_choice != 3:
    print()
    print()
    print()
    print("          =============================")
    end_menu_loop_switch=0  
  # Acme & Stub-Acme box & pin sizes
    if thd_type==1 and boxorpin==1:
        print('\033[1m' + '\033[91m' +"             Acme Box "+"'"+str(tol)+"G"+"'"+" Sizes  : -"+'\033[0m')
    if thd_type==1 and boxorpin==2:
        print('\033[1m' + '\033[91m' +"             Acme Pin "+"'"+str(tol)+"G"+"'"+" Sizes  : -"+'\033[0m')
    if thd_type==2 and boxorpin==1:
        print('\033[1m' + '\033[91m' +"          Stub-Acme Box "+"'"+str(tol)+"G"+"'"+" Sizes  : -"+'\033[0m')
    if thd_type==2 and boxorpin==2:
        print('\033[1m' + '\033[91m' +"          Stub-Acme Pin "+"'"+str(tol)+"G"+"'"+" Sizes  : -"+'\033[0m')
    print("          =============================")
    print()
    print("    Major Dia "+str(round(maj_mid/convert_units,5))+units_label+" +/-"+str(round(maj_tol/convert_units,5)))
    print()
    print("    Pitch Dia "+str(round(eff_mid/convert_units,5))+units_label+" +/-"+str(round(eff_tol/convert_units,5)))
    print()
    print("    Minor Dia "+str(round(min_mid/convert_units,5))+units_label+" +/-"+str(round(min_tol/convert_units,5)))
    print()   
    print("    Thd Depth "+str(round(thd_depth/convert_units,5))+units_label+" +/-"+str(round(eff_tol/convert_units,5)))
    while end_menu_choice == 2:
            print()
            clock_depth = float(input('\033[96m'+"    Enter Clock Depth In Inches  ? "))
            print()
            clock_depth*=25.4
            print("    Current Depth "+str(round(clock_depth/convert_units,5))+units_label)
            print()
            print("    Depth Should Be "+str(round(thd_depth/convert_units,5))+units_label+" +/-"+str(round(eff_tol/convert_units,5)))
            print()
            if boxorpin==1:
                alter_amount=thd_depth-clock_depth
            else:
                alter_amount=clock_depth-thd_depth
            print("    Alter Tool Offset :-  " +str(round(alter_amount/convert_units,5)))
            '\033[0m'
            print()
            print("          =============================")
            print()
            end_menu_choice = int(input(print('\033[1m'+'\033[93m'+"    Show Results Again   [1]    ?\n    Input Clock depth    [2]    ?\n    End                  [3]    ? \n")))
            '\033[0m'
            end_menu_loop_switch=1
            print()
    print()
    if end_menu_loop_switch != 1:
        end_menu_choice = int(input(print('\033[1m'+'\033[93m'+"    Show Results Again   [1]    ?\n    Input Clock depth    [2]    ?\n    End                  [3]    ? \n")))
        '\033[0m'
print()
print()    
print("Program End")
        