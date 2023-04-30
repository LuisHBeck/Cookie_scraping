from connect import cursor

def read_draw(table):
    sql = f'SELECT * from {table}'

    cursor.execute(sql)
    result = cursor.fetchall()

    return result

def search_draw(table, draw):
    sql = f'SELECT * from {table} WHERE idSorteio= {draw}' 

    cursor.execute(sql)
    result = cursor.fetchall()

    return result

def search_num(n1):
    sql = f'SELECT * from sorteios WHERE n1= {n1}'
    
    cursor.execute(sql)
    result = cursor.fetchall()

    return result

def select_num():
    sql = f'SELECT n1, n2, n3, n4, n5, n6 from sorteios'

    cursor.execute(sql)
    result = cursor.fetchall()

    return result


number_search = []
teste = set()

def num_plot():
        x = select_num()
        for i in x:
            for k in i:
                number_search.append(k)
                # print(k)

num_plot()
for i in number_search:
     teste.add(i)

print(teste)
number_search.sort()
# print(number_search)

repetition = []

for i in range(61):
    x = number_search.count(i)
    repetition.append(x)

del repetition[0]

# print(repetition)

print(len(number_search))
print(len(teste))
print(len(repetition))
print(repetition)


