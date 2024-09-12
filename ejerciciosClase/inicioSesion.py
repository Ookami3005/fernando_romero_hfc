from claseAlumno import Usuario, PasswordInvalido
import re, hashlib

def main():
    user_dicc = dict([(u.nombre,u) for u in recuperaUsuarios()])
    print("BIENVENIDO")
    print("1. Iniciar sesión")
    print("2. Terminar el programa\n")
    elec = ""
    while elec != "1" and elec != "2":
        elec = input("Introduce tu elección: ")

    if elec == "1":
        usuario = input('\nusername: ')
        contra = input('passwd: ')
        print(hashlib.sha256(contra.encode()).hexdigest())

        if usuario in user_dicc:
            if user_dicc[usuario].verifica_password(contra.strip()):
                print("Inicio de sesión correcto!!")
            else:
                print("Contraseña incorrecta!!")
        else:
            print("El usuario no existe!")


def escribeUsuarios():
    usuarios = []
    usuarios.append(Usuario('juanchoeh', 'juan@ciencias', 'abc123'))
    usuarios.append(Usuario('ookami', 'ookami@ciencias', 'roy123'))
    usuarios.append(Usuario('dalix', 'dalix@ciencias', 'dalix123'))

    for u in usuarios:
        u.serializa()

def recuperaUsuarios():
    try:
        lector = open('usuarios.txt', 'r')
        lineas = lector.readlines()
        usuarios = []
        for l in lineas:
            datos = re.split(r';',l)
            hash_passwd = datos[2]
            print(hash_passwd)
            usuarios.append(Usuario(datos[0], datos[1], hash_passwd.strip()))
        return usuarios
    except Exception as e:
        print(e)
    finally:
        lector.close()

if __name__ == '__main__':
    main()
