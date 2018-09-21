import os

def ForcedOpen(filename,openkeys):
    """открываем файл и создаем директории если надо"""
    dirnm=os.path.dirname(filename)
    if not os.path.exists(dirnm):
        os.makedirs(dirnm)
    return open(filename,openkeys)