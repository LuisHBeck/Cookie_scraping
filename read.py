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

def search_num(table, n1):
    sql = f'SELECT * from {table} WHERE n1= {n1}'
    
    cursor.execute(sql)
    result = cursor.fetchall()

    return result

def select_num(table):
    sql = f'SELECT n1, n2, n3, n4, n5, n6 from {table}'

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

# num_plot()
# for i in number_search:
#      teste.add(i)

# print(teste)
# number_search.sort()
# # print(number_search)

# repetition = []

# for i in range(61):
#     x = number_search.count(i)
#     repetition.append(x)

# del repetition[0]

# # print(repetition)

# print(len(number_search))
# print(len(teste))
# print(len(repetition))
# print(repetition)


# x = select_num()
# # print(x)
# n1 = 1
# n2 = 5
# n3 = 12
# n4 = 13
# n5 = 17
# n6 = 31

# lista = [n1, n2, n3, n4, n5, n6]

# for i in x:
#     if i[0] == n1:
#         if i[1] == n2:
#             if i[2] == n3:
#                 if i[3] == n4:
#                     if i[4] == n5:
#                         if i[5] == n6:
#                             print('Find')
    

