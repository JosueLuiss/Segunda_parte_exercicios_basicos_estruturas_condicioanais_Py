# n1 = float(input("Insira sua primeira nota: "))
# n2 = float(input("Insira a segunda nota: "))

# media = (n1 + n2) / 2
# print("Média: {}" .format(media))

# if media >= 7:
#     print("Aprovado")
# else:
#     if media >= 5 and media < 7:
#         print("Recuperação")
#     else:
#         print("Reprovado")

#------------------------------------------------------

# altura = float(input("Insira sua altura (m): "))
# massa = float(input("Insira seu peso atual (Kg): "))

# imc = massa / (altura * altura)
# print("IMC: {}" .format(imc))

# if imc < 17:
#     print("Muito abaixo do peso")
# else:
#     if imc >= 17 and imc < 18.5:
#         print("Abaixo do peso")
#     else:
#         if imc >= 18.5 and imc < 25:
#             print("Peso ideal")
#         else:
#             if imc >= 25 and imc < 30:
#                 print("Sobrepeso")
#             else:
#                 if imc >= 30 and imc < 35:
#                     print("Abesidade")
#                 else:
#                     if imc >= 35 and imc < 40:
#                         print("Obesidade Severa")
#                     else:
#                         print("Obesidade Mórbida")

#-------------------------------------------------------

# print("[1] Para doar R$10")
# print("[2] Para doar R$25")
# print("[3] Para doar R$50")
# print("[4] Para doar outros valores")
# print("[5] Para cancelar")
# print("-----------------------------")

# opcao = int(input("Escolha uma opção de a 5: "))

# valor = 0

# if opcao == 1:
#     valor = 10
#     print("Você doou R${}. Muito obrigado" .format(valor))
# elif opcao == 2:
#     valor = 25
#     print("Você doou R${}. Muito obrigado" .format(valor))
# elif opcao == 3:
#     valor = 50
#     print("Você doou R${}. Muito obrigado " .format(valor))
# elif opcao == 4:
#     valor = float(input("Insira o valor que deseja doar: "))
#     print("Você doou R${}. Muito obrigado " .format(valor))
# else:
#     print("Sua doação foi de R$0. Mesmo assim, muito obrigado")

#----------------------------------------------------------------

# nome = str(input("Qual seu nome? "))
# salario = float(input("Qual o valor do seu salário? "))
# dependente =int(input("Qual a quantidade de dependentes? "))

# print("Seja bem, {}" .format(nome))
# print("O seu salário é R${}" .format(salario))

# reajuste = 0

# if dependente == 0:
#     reajuste = salario + (salario * (5 / 100))
#     print("O seu salário com reajuste vai para R${} " .format(reajuste))
# elif dependente == 1 or dependente == 2 or dependente == 3:
#     reajuste = salario + (salario * (10 / 100))
#     print("Seu salário com reajuste vai para R${} " .format(reajuste))
# elif dependente == 4 or dependente == 5 or dependente == 6:
#     reajuste = salario + (salario * (15 / 100))
#     print("Seu salário com reajuste vai para R${} " .format(reajuste))
# else:
#     reajuste = salario + (salario * (18 / 100))
#     print("Seu salário com reajuste vai para R${} " .format(reajuste))

#---------------------------------------------------------------------------
# nota1 = float(input("Insira sua primeira nota: "))
# nota2 = float(input("Insira sua segunda nota: "))
# nota3 = float(input("Insira sua terceira nota: "))
# nota4 = float(input("Insira sua quarta nota: "))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# if media >= 9 and media <= 10:
#     print("Média: {}" .format(media))
#     print("Aproveitamento: A")
# else:
#     if media < 9 and media >= 8:
#         print("Média: {}" .format(media))
#         print("Aproveitamento: B")
#     else:
#         if media < 8 and media >= 7:
#             print("Mèdia: {}" .format(media))
#             print("Aproveitamento: C")
#         else:
#             if media < 7 and media >= 6:
#                 print("Média: {}" .format(media))
#                 print("Aproveitamento: D")
#             else:
#                 if media < 6 and media >= 5:
#                     print("Média: {}" .format(media))
#                     print("Aproveitamento: E")
#                 else:
#                     if media < 5 and media >=0:
#                         print("Média: {}" .format(media))
#                         print("Aproveitamento: F")
#                     else:
#                         print("Insira as notas corretamente")

#---------------------------------------------------------------

# print("Insira abaixo quantos gols cada time fez: ")

# fla = int(input("Flamengo: "))
# flu = int(input("Fluminense: "))

# print("Resultado final: Flamengo {} x {} Fluminense" .format(fla, flu))

# diferenca = fla - flu
# diferenca2 = flu - fla

# if diferenca == 0:
#     print("Empate")
# elif diferenca < 4 and fla > flu:
#     print("Resultado Normal")
#     print("Diferença de {} gols " .format(diferenca))
# elif diferenca2 < 4 and flu > fla:
#     print("Resultado Normal")
#     print("Diferença de {} gols " .format(diferenca2))
# elif diferenca >= 4 and diferenca < 5 and fla > flu:
#     print("Goleada")
#     print("Diferença de {} gols " .format(diferenca))
# elif diferenca2 >= 4 and diferenca2 < 5 and flu > fla:
#     print("Goleda")
#     print("diferença de {} gols " .format(diferenca2))
# elif diferenca >= 5 and fla > flu:
#     print("Humilhação")
#     print("Diferença de {} gols " .format(diferenca))
# elif diferenca2 >= 5 and flu > fla:
#     print("Humilhação")
#     print("Diferença de {} gols " .format(diferenca2)) 

