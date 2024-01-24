notas = [5.0, 6.2, 4.1, 7.6]
soma = 0 

for nota in notas:
  print(f'Nota: {nota}')
  soma =+ soma + nota

media = soma/ 4
print(f'A média é: {media}')