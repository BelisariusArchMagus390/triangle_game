# verifica se é ou não um triângulo
def if_triangle(a, b, c):
    condition = False
    if ((a + b) > c) or ((a + c) > b) or ((b + c) > a):
        condition = True
    return condition

# verifica se o triângulo é equilátero
def if_equilateral(a, b, c):
    condition = False
    if (a == b) and (a == c) and (b == c):
        condition = True
    return condition

# verifica se o triângulo é isósceles
def if_isosceles(a, b, c):
    condition = False
    if (a == b) or (a == c) or (b == c):
        condition = True
    return condition

# verifica se o triângulo é escaleno
def if_scalene(a, b, c):
    condition = False
    if (a != b) and (a != c) and (b != c):
        condition = True
    return condition

# centraliza funções relacionadas a categorização de triângulos
def triangle_game():
    a = input("\nDigite o primeiro lado: ")
    b = input("Digite o segundo lado: ")
    c = input("Digite o terceiro lado: ")
    if if_triangle(a, b, c) == True:
        if if_equilateral(a, b, c) == True:
            print('\nO que foi digitado é um triângulo equilátero.')
        elif if_isosceles(a, b, c) == True:
            print('\nO que foi digitado é um triângulo isósceles.')
        elif if_scalene(a, b, c) == True:
            print('\nO que foi digitado é um triângulo escaleno.')
    else:
        print('\nOs valores dados não é um triângulo.')

def main():
    flag_program = True
    # menu de opções
    while flag_program == True:
        print('\n1 - Verificar triângulo.')
        print('2 - Sair.')

        option = input('\nEscolha uma das opções acima: ')

        match option:

            case '1':
                triangle_game()
            case '2':
                flag_program = False
            case _:
                print('Opção errada, por favor escolha uma existente no menu.')

main()