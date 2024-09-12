import re, hashlib

class Usuario:
    __intentos = 5

    def __init__(self, nombre, email, passw):
        self.nombre = nombre
        self.email = email
        Usuario.__valida_password_segura(passw)
        hash_passw = hashlib.sha256(passw.encode()).hexdigest()
        self.__passw = str(hash_passw)

    def __str__(self):
        cadena = "Usuario:\n"
        cadena += "-Nombre: %s\n" % self.nombre
        cadena += "-Email: %s" % self.email
        return cadena

    def cambia_password(self, new_passw):
        self.__passw = new_passw

    def verifica_password(self, given_passw):
        hash_passw = str(hashlib.sha256(given_passw.encode()).hexdigest())
        return hash_passw == self.__passw

    def __valida_password_segura(passw):
        patron = r'.*(\d.*[A-Za-z]|[A-Za-z].*\d).*'
        result = re.search(patron, passw)
        if not result or len(passw) < 5:
            raise PasswordInvalido

    def serializa(self):
        try:
            escritor = open('usuarios.txt', 'a')
            escritor.write('%s;%s;%s\n' % (self.nombre, self.email, self.__passw))
        except Exception:
            print("Error")
        finally:
            escritor.close()


class PasswordInvalido(Exception):
    pass
