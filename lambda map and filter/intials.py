names = ['Anuja Abhisheki', 'Bhushan Abhisheki', 'Moksh Abhisheki']

for name in names:
  print(f'{name.split()[0][0]},{name.split()[1][0]}')


intials = list(map(lambda name:"".join([n[0] for n in name.split()] ), names))
print(intials)