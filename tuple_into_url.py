tup = ('www', 'hackerrank', 'com','domains', 'python')
result = ""
domain_level = ['com','in','org']
separator = '.'
for slice in tup:
  if slice in domain_level:
      separator='/'
  result=result+slice+separator
print('/'+result[:-1])
