def decora(f):
    def envuelve():
        print('Estoy a punto de ejecutar la fucnión')
        f()
        print('Terminé de ejecutar la función')
    return envuelve

@decora
def hola():
    print('Hola mundo!')

hola()