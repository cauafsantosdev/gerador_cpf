import cpf_generator as gen


while True:
    select = gen.menu()
    
    if select == 1:
        cpf = gen.generator()
        gen.db_write(cpf)
        print(f'CPF GERADO: {cpf}\n')

    elif select == 2:
        gen.db_show()

    else:
        break
    
