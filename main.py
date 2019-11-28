# Um for simples, passando por todos os dados até achar um certo valor e retornar algum print
from datetime import datetime

nemo = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']

teste = ['nemo' for i in range(0,10000)]

def findNemo(nemo):
  inicial = datetime.now()
  for i in range(0,len(nemo)):
    if nemo[i] == 'nemo':
      print('Found Nemo')
  print(inicial)
  print(datetime.now())
  

findNemo(teste)

