Dic={"Aventura":{
    "Robinson Crusoe":[1719,731582,"Daniel Defoe","Disponible",0],
    "Los tres mosqueteros":[1844,930017,"Alejandro Dumas","Disponible",0],
    "Moby Dick":[1851,213567,"Herman Melville","Disponible",0],
    "Viaje al centro de la tierra":[1864,838628,"Julio Verne","Disponible",0],
    "El libro de la selva":[1894,635612,"Rudyard Kipling","Disponible",0]},
"Ciencia ficcion":{
    "La teoria de Rogers":[2006,149065,"Faust Rogers","Disponible",0],
    "La máquina del tiempo":[1895,754866,"Herbert George Wells","Disponible",0],
    "En las montañas de la locura":[1936,382955,"H.P. Lovecraft","Disponible",0],    
    "1984":[1949,209821,"George Orwell","Disponible",0],
    "Soy leyenda":[1954,685505,"Richard Matheson","Disponible",0]},
"Fantasia":{
    "Alicia en el país de las maravillas":[1865,368937,"Lewis Carrol","Disponible",0],
    "Mary Poppins":[1964,586505,"Pamela Lyndon Travers","Disponible",0],
    "La cámara sangrienta":[1979,322553,"Angela Carter","Disponible",0],
    "Outlander":[1990,252756,"Diana Gabaldon","Disponible",0],
    "Ozma of Oz":[1907,827203," L. Frank Baum","Disponible",0]},
"Historia":{
    "Dioses, tumbas y sabios":[1949,672408,"C. W. Ceram","Disponible",0],
    "Armas, gérmenes y acero":[1997,260192,"Jared Diamond","Disponible",0],
    "Sapiens":[2011,624910,"Yuval Noah Harari","Disponible",0],
    "La gran aventura de los griegos":[2014,169567,"Javier Negrete","Disponible",0]},
"Romance":{
    "Orgullo y prejuicio":[1813,187298,"Jane Austen","Disponible",0],
    "El jinete de bronce":[2000,225691,"Paullina Simons","Disponible",0],
    "Lo que el viento se llevo":[1936,588418,"Margaret Mitchell","Disponible",0],
    "Bajo la misma estrella":[2012,259004,"John Green","Disponible",0]}}

def ver_inventario():
    print("\nLos libros en el inventario actual son:")
    print("Libro / Estado")
    for i in Dic:
        for l in Dic[i]:
            if Dic[i][l][4]<8:
                print(f'\t {l}  // {Dic[i][l][0]}, escrito por {Dic[i][l][2]} //  {Dic[i][l][3]}')
            else:
                print(f'\t{l}  // {Dic[i][l][0]}, escrito por {Dic[i][l][2]} //  {Dic[i][l][3]} con atraso de {Dic[i][l][4]-7} dias')
    print("\n")

def arrendar_libro(libro):
    for i in Dic:
        for l in Dic[i]:
            if l == libro:
                Dic[i][libro][3]="Arrendado"
def ver_inv_categorias():
    print("\nSeleccione una de las siguientes categorias:")
    for i in Dic:
        print(f'{i}')
    cat=input("Categoria: ")
    if cat in Dic:
        print("\nEl inventario de esa categoria es:")
        for i in Dic[cat]:
            print(f'\t{i}  // {Dic[cat][i][0]}, escrito por {Dic[cat][i][2]}  // {Dic[cat][i][3]}')
        print("\n")
    else:
        print(f'La categoria "{cat}" no esta dentro del sistema. \n')

def mod_inventario():
    print("\n1. Agregar un nuevo libro ")
    print("2. Modificar uno existente")
    print("3. Eliminar un libro")
    accion=int(input("Elige una accion: "))
    if accion==1:
        categoria=input("\tIngresa la categoria del libro: ")
        nombre=input("\tNombre del libro: ")
        autor=input("\tNombre del autor: ")
        year=int(input("\tAño de publicacion: "))
        while True:
            serie=int(input("\tNumero de serie (6 digitos): "))
            if 100000<serie and serie<999999:
                break
        if not categoria in Dic:
            Dic[categoria]={}
            Dic[categoria][nombre]=[]
            Dic[categoria][nombre].append(year)
            Dic[categoria][nombre].append(serie)
            Dic[categoria][nombre].append(autor)
            Dic[categoria][nombre].append("Disponible")
            Dic[categoria][nombre].append(0)
        else:
            if not nombre in Dic[categoria]:
                Dic[categoria][nombre]=[]
                Dic[categoria][nombre].append(year)
                Dic[categoria][nombre].append(serie)
                Dic[categoria][nombre].append(autor)
                Dic[categoria][nombre].append("Disponible")
                Dic[categoria][nombre].append(0)
            else:
                if Dic[categoria][nombre][0]!=year or Dic[categoria][nombre][1]!=serie or Dic[categoria][nombre][2]!=autor:
                    Dic[categoria][nombre+"v2"]=[]
                    Dic[categoria][nombre].append(year)
                    Dic[categoria][nombre].append(serie)
                    Dic[categoria][nombre].append(autor)
                    Dic[categoria][nombre].append("Disponible")
                    Dic[categoria][nombre].append(0)
        
    if accion==2:
            libro=input("Elige el libro que quieres modificar: ")
            for i in Dic:
                for l in Dic[i]:
                    if libro==l:
                        print("\nQue deseas modificar?")
                        print("1. Año de publicacion.")
                        print("2. Numero de serie, tiene que ser 6 digitos si no es invalido.")
                        print("3. Autor del libro.")
                        rpt=int(input(""))
                        if rpt==1:
                            n_y=int(input("Nuevo año que desea ingresar: "))
                            Dic[i][libro][0]=n_y
                        if rpt==2:
                            n_s=int(input("Nuevo numero de serie: "))
                            if 100000<n_s and n_s<999999:
                                Dic[i][libro][1]=n_s
                            else:
                                print("El numero de serie ingresado no es valido. \n")
                        if rpt==3:
                            n_n=input("Nuevo autor del Libro: ")
                            Dic[i][libro][2]=n_n

    if accion==3:
            libro=input("\nNombre del libro que hay que eliminar: ")
            ex=False
            for i in Dic:
                for l in Dic[i]:
                    if libro==l:
                        g=i
                        ex=True
            if ex==False:
                print("El libro ingresado no esta dentro de nuestro inventario.\n")
            if ex==True:
                Dic[g].pop(libro)
                print("El libro fue eliminado\n")
        

def devolver_libro(libro):
    for i in Dic:
        for l in Dic[i]:
            if l == libro:
                Dic[i][libro][3]="Disponible"
                Dic[i][libro][4]=0
def verificar_libros():
    for i in Dic:
        for l in Dic[i]:
            if Dic[i][l][3]=="Arrendado":
                Dic[i][l][4]+=1


while True:
    print("1. Para visualizar el inventario completo.")
    print("2. Arrendar libro.")
    print("3. Ver el inventario por categorias.")
    print("4. Modificar el inventario.")
    print("5. Devolver libro.")
    print("0. Para salir de la aplicacion.")
    R=int(input("Ingrese el numero de su accion: "))

    if R==1:
        x=ver_inventario()
    
    if R==2:
        disponibilidad=False
        while disponibilidad==False:
            existe=False
            libro=input("\nQue libro deseas arrendar: ")
            if libro=="0":
                break
            for i in Dic:
                for l in Dic[i]:
                    if l==libro:
                        existe=True
                        if Dic[i][l][3]=="Disponible":
                            disponibilidad=True
                            x=arrendar_libro(libro)
                            print("Si esta disponible, porfavor devolver dentro de los proximos 7 dias\n")
                            break
                        else:
                            print("El libro esta arrendado actualmente, porfavor elegir otro o 0 para salir")
            if existe==False:
                print("El libro no se encuentra dentro de nuestro inventario, porfavor elegir otro o 0 para salir")

    verificar_libros()

    if R==3:
        ver_inv_categorias()

    if R==4:
        mod_inventario()
    
    if R==5:
        disp=False
        while disp==False:
            dev_libro=input("Que libro deseas devolver: ")
            if dev_libro=="0":
                break
            existencia=False
            for i in Dic:
                for l in Dic[i]:
                    if l==dev_libro:
                        existencia=True
                        if Dic[i][l][3]=="Arrendado":
                            disp=True
                            x=devolver_libro(dev_libro)
                            print("Gracias por devolver el libro.\n")
                            break
                        else:
                            print("El libro elegido ya se encuentra devuelto, porfavor devolver otro o 0 para salir.")
            if existe==False:
                print("El libro no se encuentra dentro de nuestro inventario, porfavor elegir otro o 0 para salir")

    if R==0:
        break
print("Adios! :)")