def solution(number):
  if number < 0:
    return 0
  else:
    list3 = 0
    list5 = 0
    for i in range(1, number):
      if i % 3 == 0:
        list3 += i
      elif i % 5 == 0:
        list5 += i
    return list3 + list5
