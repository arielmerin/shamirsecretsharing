from sys import argv
from shamir import Shamir

"""
Se encarga de administrar el formato que podemos ponerle a una cadena dentro de la terminal
"""
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

"""
    Se encarga de recibir los argumentos en la terminal y manejar cualquier error por parte del usuario, al proveer indicaciones.
    Regresa los valores necesarios para la ejecución en cada caso.
"""
def extract_arg():
    try:
        proceso = argv[1]
        
        if(proceso == "-c"):
            archivo_por_cifrar = argv[2]
            contrasenas_guardar = argv[3]
            necesarios = int(argv[4])
            evaluaciones = int(argv[5])
            if((contrasenas_guardar.lower().endswith(".txt")) and (evaluaciones > 2) and (necesarios > 1) and (necesarios <= evaluaciones) ):
                return [archivo_por_cifrar, contrasenas_guardar, necesarios, evaluaciones]

        elif(proceso == "-d"):
            archivo_por_descifrar = argv[2]
            contrasenas = argv[3]
            if (".txt" in contrasenas.lower()):
                return [archivo_por_descifrar, contrasenas]
                      
        elif(proceso == "-h"):
            print("\nSecreto compartido de shamir")
            
            print( color.BOLD + color.BLUE + "\n\n-c\n\tCifrar\n\t------------------" + color.END)
            print("\tDeben ingresarse los siguientes datos separados por espacios\n\t-archivo a cifrar\n\t-archivo para guardar contraseñas (txt), si no existe dicho archivo se creará\n\t-Evaluaciones necesarias para desencriptar el archivo\n\t-Evaluaciones deseadas\n")
            print(color.UNDERLINE + "\tEjemplo:  python3 src/main.py -c InformeDeEstado.pdf contraseñas.txt 12 25" + color.END)
            
            print(color.RED +color.BOLD +"\n\n-d\n\tDescifrar\n\t------------------" + color.END)
            print("\tDeben ingresarse los siguientes datos separados por espacios\n\t-archivo a descifrar\n\t-archivo donde se encuentren las contraseñas (en formato txt) separadas por saltos de linea")
            print(color.UNDERLINE + "\tEjemplo:  python3 src/main.py -d InformeDeEstado.pdf contraseñas.txt" + color.END)
            
            print("\n\n-h\n\tObtener ayuda")
        else:
            raise ValueError
    except ValueError:
        print("Ingresa los argumentos correctos, encontrarás ayuda corriendo el programa con -h ")
        exit()
    except IndexError:
        print("Ingresa los argumentos completos, encontrarás ayuda corriendo el programa con -h ")
        exit()
    else:
        print("Error.")
        exit()     
    
"""
Este método maneja el primer contacto con el programa, bifurca su comportamiento en función del número de argumentos pasados en la terminal para su ejecución
"""
def main():
    list_argumentos = extract_arg()
    if(len(list_argumentos) == 4):
        Shamir.cifrar(list_argumentos)
    elif(len(list_argumentos) == 2):
        Shamir.descrifrar(list_argumentos)
    else:
        exit()

if __name__ == "__main__":
    main()