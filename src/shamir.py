import secrets
import pyaes
class Shamir:
    _primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481
    
        """
        Genera numéros aletorioss de 256 bits, siempre encargándose de que dicho número sea menor al módulo primo
        """
    def genera_coeficientes():
        numero_aleatorio = secrets.randbits(256)
        
        while(numero_aleatorio > Shamir._primo):
            numero_aleatorio = secrets.randbits
            
        return numero_aleatorio
    
        """
        docstring
        """
    def encriptar(archivo):
        
        pass
    
    
        """
        la lista_argumentos : [archivo_por_cifrar, contrasenas_guardar, necesarios, evaluaciones]
        """
    def cifrar(lista_argumentos):
        archivo, contrasenas, necesarios, evaluaciones = lista_argumentos
        
        pass
    
    def descrifrar():
        a = 1
        pass