# Lista de usuarios y contraseñas válidas
usuContra = [["Manuel", "canMorto"], ["pepe", "usuaya"]]

# -------------------------------------------------------
# Función para comprobar si el usuario y contraseña existen
# -------------------------------------------------------
def comprobarUsuario(listaUsuarioContrasinal):
    existeUsuario = False  # Variable para indicar si el usuario existe o no
    nomeUsuario = input("¿Cuál es el nombre de usuario? ")  # Pide el nombre
    contrasinal = input("¿Cuál es la contraseña? ")          # Pide la contraseña

    # Recorre toda la lista de usuarios
    for usuarioContrasinal in listaUsuarioContrasinal:
        # Comprueba si el nombre coincide
        if usuarioContrasinal[0] == nomeUsuario:
            # Si además coincide la contraseña, el usuario existe
            if usuarioContrasinal[1] == contrasinal:
                existeUsuario = True
    return existeUsuario  # Devuelve True o False

# -------------------------------------------------------
# Llamada a la función para comprobar usuario y contraseña
# -------------------------------------------------------
existe = comprobarUsuario(usuContra)

# Muestra un mensaje según el resultado
if existe:
    print("Usuario válido")
else:
    print("Contraseña o usuario erróneo")

# -------------------------------------------------------
# Función para comprobar la longitud del contraseña
# -------------------------------------------------------
def comprobarLonxitude(contrasinal):
    # Devuelve True si la longitud es mayor que 8 caracteres
    if len(contrasinal) > 8:
        return True
    else:
        return False

# -------------------------------------------------------
# Función para comprobar si el contraseña contiene mayúsculas
# -------------------------------------------------------
def comprobarMaisculasContrasinal(contrasinal):
    # Recorre cada letra del contraseña
    for letra in contrasinal:
        # Si la letra está en mayúscula, devuelve True
        if letra == letra.upper() and letra.isalpha():
            return True
    return False  # Si no hay mayúsculas, devuelve False

# -------------------------------------------------------
# Función para comprobar si el contraseña contiene números
# -------------------------------------------------------
def comprobarNumerosEnContrasinal(contrasinal):
    # Recorre cada carácter del contraseña
    for caracter in contrasinal:
        # Si el carácter es un número, devuelve True
        if caracter.isnumeric():
            return True
    return False  # Si no hay números, devuelve False

# -------------------------------------------------------
# Función para comprobar si hay caracteres especiales
# -------------------------------------------------------
def comprobarCaracteresEspeciais(contrasinal):
    especiais = '!@$%&*_'  # Lista de símbolos permitidos
    # Recorre cada carácter del contraseña
    for caracter in contrasinal:
        # Si el carácter está en la lista de símbolos, devuelve True
        if caracter in especiais:
            return True
    return False  # Si no hay símbolos especiales, devuelve False