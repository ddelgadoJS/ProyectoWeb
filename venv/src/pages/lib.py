from .models import Log, Empresa, Ruta, Parada


def crear_log(usuario, accion, empresa=None, ruta=None, parada=None):
    """
    Crea un entry en la bitacora
    empresa, ruta, y parada son opcionales, 

    si parada tiene un objeto se determina que es parada, 
    si no entonces si ruta tiene un objeto es una ruta
    si no entonces si empresa tiene un objeto es una empresa
    """
    objeto = ''
    objetoReal = None
    if empresa is not None:
        objeto='empresa'
        objetoReal = empresa
    if ruta is not None:
        objeto='ruta'
        objetoReal = ruta
    if parada is not None:
        objeto='parada'
        objetoReal = parada

    nombreUsuario =usuario.username

    operacion = f'{nombreUsuario} {accion} {objeto} {objetoReal.nombre}'
    log = Log(
        usuario=usuario,
        operacion=operacion,
        empresa=empresa,
        ruta=ruta,
        parada=parada
    )
    log.save()