def first_non_unic_letter(str1:str):
  if not str1:
    raise ValueError

  letter_order = []
  ctr = {}
  for i in str1.lower():
    if i in ctr:
      ctr[i] += 1
    else:
      ctr[i] = 1
      letter_order.append(i)
  for i in letter_order:
    if ctr[i] == 1:
      return i
  return None

print(first_non_unic_letter('Google'))
print(first_non_unic_letter('Amazon'))