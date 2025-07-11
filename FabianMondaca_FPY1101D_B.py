#Fabian Mondaca Miranda
#productos = {Modelo:[marca, pantalla, RAM, disco , GB de DD, Procesador de video]}
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}


stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1], 
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}

#funciones----------------------------------------------------------------------

#"funcional a medias
def Stock_Marca(mod):
    for MarcaModelo in stock:
        if MarcaModelo == mod:
            print(f"El stock es de  {MarcaModelo} es {stock[MarcaModelo][1]} ")
    if mod not in MarcaModelo:
        print("Stock no encontrado")
        



#falta funcionalidad
def Busqueda_Precio(modelo):
    while True:
        try:
            precioMax =int(input("Ingrese Precio Maximo"))
            if precioMax < 0:
                print("el precio debe ser mayor que cero y ingresar valores enteros!!")
            else:
                break
        except ValueError:
            print("Debe ser un entero!!")
        while True:
            try:
                precioMin = int(input("Ingrese precio minimo"))
                if precioMin < 0:
                    print("Debe ser un numero mayor que 0 y un entero")
            except ValueError:
                print("Debe ser un entero!!")

#falta funcionalidad
def Eliminar_Producto(mod):
            for modelo in stock:
                mod == modelo
                del productos[modelo]
                print("Producto eliminado!!")
#menu-----------------------------------------------------------------------
def main():
    while True:
        print("***MENU Principal***")
        print("1.- Stock Marca")
        print("2.- Búsqueda por precio")
        print("3.- Eliminar producto")
        print("4.- Salir")
        
        #IMPORTANTE -> mod = al modelo que escoges para que funcione (cambiar desde acá)
        mod ='8475HD'
        op = input("Ingrese una opción: ")
        if op == "1":
            Stock_Marca(mod)
        elif op == "2":
            Busqueda_Precio()
        elif op == "3":
            Eliminar_Producto()
        elif op == "4":
         print("el programa se ha finalizado")
         break
        else:
            print("Debe seleccionar una opcion valida")



if __name__  == "__main__":
    main()
