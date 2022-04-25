def customerSuccessBalancing(customerSuccess, customers, customerSuccessAway):
  # Processo de filtragem dos CSS não disponíveis
  cssDisp = customerSuccess.copy()
  for iCA, csA in enumerate(customerSuccessAway):
    for iCs, cs in enumerate(customerSuccess):
      if cs[0] == csA:
        #print(cs)
        cssDisp.remove(cs)

  # Processo de organização crescente dos scores CSS
  cssOrd, scoresOrd = [], []
  for s in cssDisp:
    scoresOrd.append(s[1])
  scoresOrd.sort()
  #print(scoresOrd)
  for iS, s in enumerate(scoresOrd):
    for iCs, cs in enumerate(cssDisp):
      if s == cs[1]:
        cssOrd.append(cs)
  #print(cssOrd)
  
  '''me = cssDisp[0][1]
  ma = 0
  for iCs, cs in enumerate(cssDisp):
    if cs[1] < me:
      me = cs[1]
    if cs[1] > ma:
      ma = cs[1]
  print(f'Maior: {ma}, Menor: {me}')'''

  # Processo de comparação e aquisição CSS - Cust
  CssCuId, idUsados, idAdd = [], [], []
  for iCs, cs in enumerate(cssOrd):
    CssCuId.append(cs[0])
    idAdd.clear()
    for iCu, c in enumerate(customers):
      #print(f'{iCs} - {cs} = {iCu} - {c}')
      # [[5, [2, 4, 6]], [1, []]]
      # Verifica ID em uso
      if c[0] not in idUsados:
        if cs[1] >= c[1]:
          idUsados.append(c[0])
          idAdd.append(c[0])
          print(f'{cs[1]} - {c[1]} (id: {c[0]}')
          print('Id em Uso:',idUsados)
    CssCuId.append(idAdd.copy())
    print(CssCuId)
      
  # Processo de verificar maior Customers
  cont, id = 0, 0
  for i,c in enumerate(CssCuId):
    if type(c) == list:
      if len(c) > cont:
        cont = len(c)
        id = i
      if len(c) == cont:
        id = 0
        break
  
  return id


'''
10, 20 para o cs de nível 20
40, 60 para o cs de nível 60
70 para o cs de nível 75
90 para o cs de nível 95

10, 20, 40, 60 para o cs de nível 60
70, 90 para o cs de nível 95
'''

cssD = {'id': [1, 2, 3, 4], 'score': [60, 20, 95, 75]}
css = [[1, 60], [2, 20], [3, 95], [4, 75], [5, 40]]

customersD = {'id': [1, 2, 3, 4, 5, 6], 'score': [90, 20, 70, 40, 60, 10]}
customers = [[1, 90], [2, 20], [3, 70], [4, 40], [5, 60], [6, 10]]

csAway = [2, 4]

print(customerSuccessBalancing(css, customers, csAway))