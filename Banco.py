saldo = 0
limite = 500
numero_saques = 0
historico = ""
extrato = 0
historico = ""


while True:
  opcao =  input ("Digite uma opção, d para depositar, s para sacar, e para extrato e q para sair")
  if opcao == "d":

    print("Depósito")
    parcela = float(input ("Digite o quanto irá depositar"))
    if parcela >=0:
      extrato = extrato + parcela
      historico += f"Depósito:  R$ {parcela: .2f}\n"
    else:
      print("Digite um valor válido")
        

  elif opcao == "s":
    print("Saque")
    saque = float(input("Digite o quanto deseja sacar"))
    if saque >500:
      print("Digite um valor válido")
    elif extrato-saque<0:
      print("Você não possuí esse dinheiro em conta")
    elif numero_saques > 2:
      print("Você não pode mais sacar dinheiro hoje")
    else:
      extrato = extrato-saque
      numero_saques = numero_saques +1
      historico += f"Saque:  R$ {saque: .2f}\n"

  elif opcao == "e":
    print("Não foram realizadas movimentações." if not historico else historico)
    print(f"\n Saldo R${extrato:.2f}")
      
  elif opcao == "q":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")