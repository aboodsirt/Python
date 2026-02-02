#Sorting Hat
Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0
print ("Q1) Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk")
ans1= int(input("enter your choice (1,2) : "))
if ans1 ==1:
  Ravenclaw=Ravenclaw+1
  Gryffindor =Gryffindor +1
elif ans1==2:
  Slytherin =Slytherin +1
  Hufflepuff =Hufflepuff +1
else :
  print ("Wrong input")

print ("Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold")
ans2=int(input("enter your choice (1,2,3,4) : "))
if ans2==1:
  Hufflepuff =Hufflepuff +2
elif ans2==2:
  Slytherin =Slytherin +2
elif ans2==3:
  Ravenclaw =Ravenclaw +2
elif ans2==4:
  Gryffindor =Gryffindor +2
else :
  print ("Wrong input")
print("Q3) Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum")
ans3=int(input("enter your choice (1,2,3,4) : "))
if ans3==1:
  Slytherin =Slytherin +4
elif ans3==2:
  Hufflepuff =Hufflepuff +4
elif ans3==3:
  Ravenclaw =Ravenclaw +4
elif ans3==4:
  Gryffindor=Gryffindor +4
else :
  print ("Wrong input")

max_points=max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
if max_points==Gryffindor:
  print ("you belong to Gryffindor!")
elif max_points==Ravenclaw:
  print ("you belong to Ravenclaw!")
elif max_points==Hufflepuff:
  print ("you belong to Hufflepuff!")
elif max_points==Slytherin:
  print ("you belong to Slytherin!")

print ("the score : ")
print (str(Gryffindor)+ "point for Gryffindor.")
print (str(Ravenclaw)+ "point for Ravenclaw.")
print (str(Hufflepuff)+ "point for Hufflepuff.")
print (str(Slytherin)+ "point for Slytherin.")
