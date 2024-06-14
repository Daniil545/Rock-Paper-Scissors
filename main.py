import random
score=0
botscore=0
print("Добро пожаловать в игру камень, ножницы и бумага")
for i in range(3):
  answer=input("Что ты выберишь:").lower()
  if answer.find("камень")!=-1:
    answer="к"
  elif answer.find("ножницы")!=-1:
    answer="н"
  elif answer.find("бумага")!=-1 or answer.find("бумагу")!=-1:
    answer="б"
  elif answer.find("ящерица")!=-1:
    answer="я"
  elif answer.find("споук")!=-1:
    answer="с"
  botanswer=random.choice(["бумага","ножницы","камень","ящерица","споук"])
  print("Я выбрал",botanswer)
  botanswer=botanswer[0]
  if(answer==botanswer):
    print("ничья")
  elif (answer=="к" and botanswer=="н") or (answer=="б" and botanswer=="к") or (answer=="н" and botanswer=="б") or (answer=="с" and botanswer=="к") or (answer=="c" and botanswer=="н") or (answer=="к" and botanswer=="я") or (answer=="н" and botanswer=="я") or (answer=="я" and botanswer=="с") or (answer=="я" and botanswer=="б") or (answer=="б" and botanswer=="с"):
   print("Ты победил")
   score+=1
  else:
    print("Я победил")
    botscore+=1
if score>botscore:
  print("Ты победил")
elif score<botscore:
  print("Ты проиграл")
elif score==botscore:
 print("Ничья") 
