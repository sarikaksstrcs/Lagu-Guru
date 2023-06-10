import streamlit as st
def find_len(akshara):
  l = 0
  chillu = ['ൺ', 'ൻ', 'ർ', 'ൽ', 'ൾ']
  for x in akshara:
    if x not in chillu and x[-1] != '്':
      l +=1
  return l


def divide_list_for_kakali(akshara,mathra):
    i =0
    temp = []
    temp_mathra = []
    chillu = ['ൺ', 'ൻ', 'ർ', 'ൽ', 'ൾ']
    for x in range(4):
      x= 3
      for t in akshara[i:i+x]:
        if len(t)==2:
          if t[1] == '്':
            x+=1
        elif t in chillu:
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
      if len(t)==2:
        if t[1] == '്':
          x+=1
      elif t in chillu:
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
    if x not in chillu and x[-1] != '്':
      sum+=1
  print(sum)
  if sum!=14:
    return False
  for x in grouped_mathra:
    if 'G' not in x:
      return False
  return True

def check_manjari(akshara,mathra):
  grouped_akshara,grouped_mathra = divide_list_for_kakali(akshara, mathra)
  print(grouped_akshara)
  print(grouped_mathra)
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
  l = 0
  chillu = ['ൺ', 'ൻ', 'ർ', 'ൽ', 'ൾ']
  for x in (grouped_akshara[-1]):
    if x not in chillu and x[-1] != '്':
       l += 1
  if l == 1:
    return True
  else:
     return False

def correct_vritham_for_kakali(grouped_akshara,grouped_mathra):
  i,j =0,0
  mathra_sum =[]
  for i in range(len(grouped_akshara)):
      sum =0
      for j in range(len(grouped_mathra[i])):
          if grouped_mathra[i][j] == 'G':
              sum += 2
          elif grouped_mathra[i][j] == 'L':
              sum += 1
      mathra_sum.append(sum)
  text = []
  for i in range(len(mathra_sum)):
      if mathra_sum[i]-5 == -1:
          text.append("<span style='color:red'>"+''.join(grouped_akshara[i])+"</span>")
          for j in range(len(grouped_akshara[i])):
              if grouped_akshara[i][j][-1] == 'ൊ':
                  # st.write(mathra_sum[i])
                  st.write("Replace with",grouped_akshara[i][j][:-1]+'ോ')
              elif grouped_akshara[i][j][-1] == '്':
                  st.write("Replace with",grouped_akshara[i][j][:-1]+'ി')
              elif grouped_akshara[i][j][-1] == 'ി':
                  st.write("Replace with",grouped_akshara[i][j][:-1]+'ീ')
              elif grouped_akshara[i][j][-1] == 'െ':
                  st.write("Replace with",grouped_akshara[i][j][:-1]+'േ')
              elif grouped_akshara[i][j][-1] == 'ു':
                  st.write("Replace with",grouped_akshara[i][j][:-1]+'ൂ')
              if j+1 <len(grouped_akshara[i]):
                if grouped_mathra[i][j] == 'L' and grouped_akshara[i][j+1][-1] in ['ോ','ാ','ീ','േ','ൂ'] and '്' not in grouped_akshara[i][j+1] :
                  st.write("Replace with",grouped_akshara[i][j+1][0]+'്'+grouped_akshara[i][j+1][0]+grouped_akshara[i][j+1][-1])
     
      elif mathra_sum[i]-5 == 1:
          text.append("<span style='color:blue'>"+''.join(grouped_akshara[i])+"</span>")
          for j in range(len(grouped_akshara[i])):
              if grouped_mathra[i][j] == 'L' and grouped_akshara[i][j+1][-1] in ['ോ','ാ','ീ'] and '്' not in grouped_akshara[i][j+1]:
                  st.write("Replace with",grouped_akshara[i][j+1][0]+'്'+grouped_akshara[i][j+1][0]+grouped_akshara[i][j+1][-1])
              elif grouped_akshara[i][j][-1] == 'ി':
                  st.write("Replace with",grouped_akshara[i][j][:-1]+'്')
              elif grouped_akshara[i][j][-1] == 'ീ':
                  st.write("Replace with",grouped_akshara[i][j][:-1]+'ി')
      else:
          text.append(''.join(grouped_akshara[i]))
  print(text)
  final_txt = ' '.join(text)
  return final_txt

def correct_vritham_for_keka(grouped_akshara,grouped_mathra):
  i,j =0,0
  mathra_sum =[]
  text = []
  for i in range(len(grouped_akshara)):
      if 'G' not in grouped_mathra[i]:
        text.append("<span style='color:red'>"+''.join(grouped_akshara[i])+"</span>")
        for j in range(len(grouped_akshara[i])):
          if grouped_akshara[i][j][-1] == 'ൊ':
              # st.write(mathra_sum[i])
              st.write("Replace with",grouped_akshara[i][j][:-1]+'ോ')
          elif grouped_akshara[i][j][-1] == '്':
              st.write("Replace with",grouped_akshara[i][j][:-1]+'ി')
          elif grouped_akshara[i][j][-1] == 'ി':
              st.write("Replace with",grouped_akshara[i][j][:-1]+'ീ')
          elif grouped_akshara[i][j][-1] == 'െ':
              st.write("Replace with",grouped_akshara[i][j][:-1]+'േ')
          elif grouped_akshara[i][j][-1] == 'ു':
              st.write("Replace with",grouped_akshara[i][j][:-1]+'ൂ')
          if j+1 <len(grouped_akshara[i]):
              if grouped_mathra[i][j] == 'L' and grouped_akshara[i][j+1][-1] in ['ോ','ാ','ീ','േ','ൂ'] and '്' not in grouped_akshara[i][j+1] :
                  st.write("Replace with",grouped_akshara[i][j+1][0]+'്'+grouped_akshara[i][j+1][0]+grouped_akshara[i][j+1][-1])
      else:
        text.append(''.join(grouped_akshara[i]))
  final_txt = ' '.join(text)
  return final_txt
    