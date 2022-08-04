def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    # for i in poblacion_paises.keys():
    #     print(i)
    
    # for i in poblacion_paises.values():
    #     print(i)

    for i, j in poblacion_paises.items():
        print(str(i) + ' Tiene ' + str(j) + ' De poblacion')



if __name__ == '__main__':
    run()