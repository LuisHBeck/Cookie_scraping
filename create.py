from connect import cursor, data_base

def creat_sorteio(sorteio, n1, n2, n3, n4, n5, n6):
    insert_sorteio = f'''INSERT INTO resultados(idSorteio, n1, n2, n3, n4, n5, n6)
    values
    ({sorteio}, {n1}, {n2}, {n3}, {n4}, {n5}, {n6},)
    '''

    cursor.execute(insert_sorteio)
    data_base.commit()