from telnetlib import theNULL


def palindromo(frase, frase_fix):
    if frase == frase[::-1]:
        print(f'La frase {frase} es un palindromo!, al reves es {frase_fix[::-1]}')
    else:
        print(f'Lo sentimos, la frase {frase} no es un palindromo, al reves es {frase_fix[::-1]} ingresa otra frase y comprueba de nuevo.')
        
def limpieza(frase):
    frase=frase.lower()
    frase=frase.strip()
    frase=frase.replace(' ','')
    print(frase)
    return frase
        
def run():
    print("Hola y bienvenido al comprobador de palindromos.")
    frase = str(input("Escribe la palabra o frase a la que quieras comprobar si es un palindromo: "))
    frase_fix = limpieza(frase)
    palindromo(frase, frase_fix)
    
if __name__ == '__main__':
    run()