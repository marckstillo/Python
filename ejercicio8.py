### strings  o cadenas de texto

nombre = "MARCOS"
apellido = "CASTILLO"

print(nombre + "" + apellido)

texto = "Este texto \n tiene salto de linea y \t tabulación"
print(texto)

#formateo

user, password, email = "maria", 51125, "maria@gmail.com"
print("su usuario y contraseña son {} {} y su emal es {}".format (user, password, email))
print("su usuario y contraseña son %s %d y su email es %s" % (user, password, email))
print("su usuario y contraseña son " + user + "" + str(password)+ "y su email " + email)
print(f"su usuario y contraseña son {user} {password} y email {email}")