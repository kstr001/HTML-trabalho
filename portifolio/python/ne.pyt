from ast import Continue
id_global = 0
lista = []
def cadastro_u(id):
  print('CADASTRO')
  print(f'ID do cliente: {id}')
  y = input('Nome: ')
  u = input('CPF: ')
  r = input('Cidade: ')
  e = input('Rua: ')
  w = input('Número: ')
  q = input('E-mail: ')
  print('-'*20)
  s = input('Senha: ')
  print('-'*20)
  dicionario = {'Nome' : y,
                'CPF' : u,
                'Cidade' : r,
                'Rua' : e,
                'Número' : w,
                'E-mail' : q,
                'Senha' : s}
  lista.append(dicionario.copy())

def menu():
  acu = float(f'{0:.2f}')

  while True:
    print('-'*37)
    print('|           CARDAPIO                |')
    print('-'*37)
    print('|(PF) Prato Feito:        R$12,99   |\n'
          '|(PP) Prato Por kg:       R$22,25 kg|\n'
          '|(BR) Buffet 2 repetições:R$35,50   |\n'
          '|(S) Voltar ao menu principal       |')
    print('-'*37)
    print(f'Total: {acu:.2f}')
    print('-'*37)
    op = input('Escolha (PF)/(PP)/(BR)/(S): ')
    if op == 'PF' or op == 'pf':

  #                                              PRATO FEITO
      print('Prato feito selecionado')
      print('-'*20)
      c = input('Com ou sem salada (S) (N): ')
      if c == 'S' or c =='N' or c == 's' or c == 'n':
        print('-'*20)
        p = input('Peixe, Frango, Suino ou Gado\n'
                  '(P) or (F) or (S) or (G): ')
        print('-'*20)
        if p == 'P' or p == 'F' or p == 'S' or p == 'G' or p == 'p' or p == 'f' or p== 's' or p== 'g':
          mais = input('Mais alguma coisa (S) (N)\n'
                       '->>>')
          acu += 12.99
          if mais == 'S' or mais == 's':
            print('')
            continue
          elif mais == 'N' or mais == 'n':
            print('-'*20)
            print('Formas de pagamento')
            print('1 - Dinheiro')
            print('2 - Cartão de Crédito')
            print('3 - Cartão de Débito')
            print('4 - Pix')
            print('-'*20)
            print(f'Total: R${acu:.2f}')
            print('-'*20)
            pago = input('Forma de Pagamento: ')
            if pago == '1':
              di = float(input('Dinheiro: '))
              tro = di - float(f'{acu:.2f}')
              if di >= float(f'{acu:2f}'):
                print(f'Troco: {tro:.2f}')
                print('Feito')
                print('-'*20)
                print('Espere ser chamado')
                acu -= acu
                break
              else:
                print('Dinheiro Insuficiente')
                acu -= acu
                continue


            elif pago == '2':
              cc = float(input('Cartão de Crédito: '))
              if cc == float(f'{acu:.2f}'):
                print('Feito')
                print('-'*20)
                print('Espere ser chamado')
                acu -= acu
                break
              else:
                print('Value_error')
                acu -= acu
                continue

            elif pago == '3':
              cd = float(input('Cartão de Débito: '))
              if cd == float(f'{acu:.2f}'):
                print('Feito')
                print('-'*20)
                print('Espere ser chamado')
                acu -= acu
                break
              else:
                print('Value_error')
                acu -= acu
                continue

            elif pago == '4':
              pi = float(input('Pix: '))
              if pi == float(f'{acu:.2f}'):
                print('Feito')
                print('-'*20)
                print('Espere ser chamado')
                acu -= acu
                break
              else:
                print('Value_error')
                acu -= acu
                continue

            elif pago == '3':
              cd = float(input('Cartão de Débito: '))
              if cd == float(f'{acu:.2f}'):
                print('Feito')
                print('-'*20)
                print('Espere ser chamado')
                acu -= acu
                break
              else:
                print('Value_error')
                acu -= acu
                continue

            elif pago == '4':
              pi = float(input('Pix: '))
              if pi == float(f'{acu:.2f}'):
                print('Feito')
                print('-'*20)
                print('Espere ser chamado')
                acu -= acu

                break
              else:
                print('Value_error')
                acu -= acu
                continue

  #                                               PRATO POR KG
    elif op == 'PP' or op == 'pp':
      print('Prato por kg selecionado')
      print('-'*20)
      peso = float(input('Peso do prato : '))
      g = 22.25 * peso
      mais = input('Mais alguma coisa (S) (N)\n'
                   '->>>')
      acu += g
      if mais == 'S' or mais == 's':
        print('')
        continue
      elif mais == 'N' or mais == 'n':
        print('-'*20)
        print('Formas de pagamento')
        print('1 - Dinheiro')
        print('2 - Cartão de Crédito')
        print('3 - Cartão de Débito')
        print('4 - Pix')
        print('-'*20)
        print(f'Total: R${acu:.2f}')
        print('-'*20)
        pago = input('Forma de Pagamento: ')
        if pago == '1':
          di = float(input('Dinheiro: '))
          tro = di - acu
          if di >= float(f'{acu:.2f}'):
            print(f'Troco: {tro:.2f}')
            print('Feito')
            acu -= acu
            break
          else:
            print('Dinheiro Insuficiente')
            acu -= acu
            continue

        elif pago == '2':
          cc = float(input('Cartão de Crédito: '))
          if cc == float(f'{g:.2f}'):
            print('Feito')
            acu -= acu
            break
          else:
            print('Value_error')
            acu -= acu
            continue

        elif pago == '3':
          cd = float(input('Cartão de Débito: '))
          if cd == float(f'{g:.2f}'):
            print('Feito')
            acu -= acu
            break
          else:
            print('Value_error')
            acu -= acu
            continue

        elif pago == '4':
          pi = float(input('Pix: '))
          if pi == float(f'{g:.2f}'):
            print('Feito')
            acu -= acu
            break
          else:
            print('Value_error')
            acu -= acu
            continue

  #                                             BUFFET
    elif op == 'BR' or op == 'br':
      print('Buffet selecionado')
      acu += 35.50
      mais = input('Mais alguma coisa (S) (N)\n'
                   '->>>')
      if mais == 'S' or mais == 's':
        print('')
        continue
      elif mais == 'N' or mais == 'n':
        print('-'*20)
        print('Formas de pagamento')
        print('1 - Dinheiro')
        print('2 - Cartão de Crédito')
        print('3 - Cartão de Débito')
        print('4 - Pix')
        print('-'*20)
        print(f'Total: R${acu:.2f}')
        print('-'*20)
        pago = input('Forma de Pagamento: ')
        if pago == '1':
          di = float(input('Dinheiro: '))
          tro = di - acu
          if di >= float(f'{acu:.2f}'):
            print(f'Troco: {tro}')
            print('Feito')
            acu -= acu
            break
          else:
            print('Dinheiro Insuficiente')
            acu -= acu
            continue

        elif pago == '2':
          cc = input('Cartão de Crédito: ')
          if cc == float(f'{acu:.2f}'):
            print('Feito')
            acu -= acu
            break
          else:
            print('Value_error')
            acu -= acu
            continue

        elif pago == '3':
          cd = float(input('Cartão de Débito: '))
          if cd == float(f'{acu:.2f}'):
            print('Feito')
            acu -= acu
            break
          else:
            print('Value_error')
            acu -= acu
            continue

        elif pago == '4':
          pi = float(input('Pix: '))
          if pi == float(f'{acu:.2f}'):
            print('Feito')
            acu -= acu
            break
          else:
            print('Value_error')
            acu -= acu
            continue

#                                              SAIR
    elif op == 'S' or op == 's':
      break
    else:
      print('Opção Inválida')
      continue


#                                                ini
while True:
  print('-'*38)
  ca = input('cadastrado S or N or Sair = 1: ')
  print('-'*38)
  if ca == 'S' or ca == 's':
    us = input('e-mail: ')
    ps = input('senha: ')
    if us == lista[0]['E-mail'] and ps == lista[0]['Senha']:
      print('-'*20)
      print(f'Bem vindo(a)')
      lista[0]['Nome']
      print('-'*20)
      print('Cardapio >> 1')
      print('sair >> 2')
      print('-'*20)
      test = input('digite: ' )
      if test == '1':
        menu()
      elif test == '2':
        break
      else:
        print('Opção Inválida')
        continue
  elif ca == 'N' or ca == 'n':
    id_global += 1
    cadastro_u(id_global)
  elif ca == '1':
    break