'''
>>Projeto Açaiteria:
'''



# Ufa, quebrei a maldição
# print('Olá, Mundo!')




print('_'* 48 + '\n')
print('Bem vindo ao sistema de vendas - Açaiteria!\n')
print('1 - Cadastrar produto')
print('2 - Listar produtos')
print('3 - Realizar vendas')
print('4 - Açaí')
print('5 - Toppings')
print('6 - Localização')
print('7 - Contato')
print('8 - Redes sociais')
print('9-  Feedback')
print('0 - Sair do sistema')
print('\n--------------------------------------\n')

opcao__definida = int(input('Digite a opcao deseja: '))
if opcao__definida == 1:
    print('Cadatrando produtos...')

elif opcao__definida == 2:
    print('Listando produtos...')

elif opcao__definida == 3:
    print('Realizando Vendas...')

elif opcao__definida == 4:
    print('Preparando Pedido...') 

elif opcao__definida == 5:
    print('Acrescentando os complementos...')

elif opcao__definida == 6:
    print('Localizando entrega...')

elif opcao__definida == 7:
    print('Entrando em contato...')
        
elif opcao__definida == 8:
    print('Avalição do produto...')

elif opcao__definida == 9:
    print('Pronto! Conheca nos mais na nossa comunidade...')


else:
    print('Ops, houve algum erro, tente novamente!')