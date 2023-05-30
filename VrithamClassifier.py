
def divide_list_for_kakali(akshara,mathra):
    i =0
    temp = []
    temp_mathra = []
    chillu = ['ൺ', 'ൻ', 'ർ', 'ൽ', 'ൾ']
    for x in range(4):
      x= 3
      for t in akshara[i:i+x]:
        if t in chillu:
          x +=1
      temp.append(akshara[i:i+x])
      temp_mathra.append(mathra[i:i+x])
      i+=x
    return temp,temp_mathra

def divide_list_for_keka(akshara,mathra):
  inc_list = [3,2,2,3,2,2]
  i =0
  temp = []
  temp_mathra = []
  chillu = ['ൺ', 'ൻ', 'ർ', 'ൽ', 'ൾ']
  for x in inc_list:
    for t in akshara[i:i+x]:
      if t in chillu:
        x +=1
    temp.append(akshara[i:i+x])
    temp_mathra.append(mathra[i:i+x])
    i+=x
  return temp,temp_mathra

def check_kakali(akshara,mathra):
  grouped_akshara,grouped_mathra = divide_list_for_kakali(akshara, mathra)
  print(grouped_akshara)
  print(grouped_mathra)
  i,j =0,0
  for i in range(len(grouped_akshara)):
    sum =0
    for j in range(len(grouped_mathra[i])):
      if grouped_mathra[i][j] == 'G':
        sum += 2
      elif grouped_mathra[i][j] == 'L':
        sum += 1
    if sum != 5:
      return False
  return True

def check_keka(akshara,mathra):
  grouped_akshara,grouped_mathra = divide_list_for_keka(akshara,mathra)
  print(grouped_akshara)
  print(grouped_mathra)
  chillu = ['ൺ', 'ൻ', 'ർ', 'ൽ', 'ൾ']
  sum = 0
  for x in akshara:
    if x not in chillu:
      sum+=1
  if sum!=14:
    return False
  for x in grouped_mathra:
    if 'G' not in x:
      return False
  return True

def check_manjari(akshara,mathra):
  grouped_akshara,grouped_mathra = divide_list_for_kakali(akshara, mathra)
  
  i,j =0,0
  for i in range(len(grouped_akshara)-1):
    sum =0
    for j in range(len(grouped_mathra[i])):
      if grouped_mathra[i][j] == 'G':
        sum += 2
      elif grouped_mathra[i][j] == 'L':
        sum += 1
    if sum != 5:
      return False
  if len(grouped_akshara[-1])==1:
    return True
