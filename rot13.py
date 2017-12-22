def rot_13(text):
 def rot(englishlang):
  i='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.find(englishlang)
  if i!=-1:
   return 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'[i]
  else:
   return englishlang
 return "".join(map(rot, text))
print(rot_13('noenpnqnoen'))  #результат: abracadabra


#со считыванием из файла
 def rot13(text):
  def rot(englishlang):
   i='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.find(englishlang)
   if i !=-1:
    return 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'[i]
   else:
    return englishlang
  return "".join(map(rot, text))
file=open("text.txt", "r") #только для чтения
textik=file.read()
file.close()
file_1=open("text_1.txt", "a+") #если такого файла нет, то он будет создан
readik=(rot13(textik))
file_1.write(readik)
file_1.close()