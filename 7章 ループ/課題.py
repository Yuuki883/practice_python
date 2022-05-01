#1
movie = ["永遠の0","ミッドナイトイーグル","のだめカンタービレ","復活のルルーシュ","孤狼の血","ライアーゲーム"]
for i in movie:
  print(i)

#2
for i in range(25,51):
  print(i)

#3
movies = ["永遠の0","ミッドナイトイーグル","のだめカンタービレ","復活のルルーシュ","孤狼の血","ライアーゲーム"]
for i, movie in enumerate(movies):
  print(i)
  print(movie)

print(movie)

#4
numbers = [10,9,8,7,6,5,4,3,2,1]

while True:
  answer = input("Guess a number or type q to quit.")
  if answer == "q":
      break
  try:
    answer = int(answer)
  except ValueError:
      print("please type a number or q to quit.")
  if answer in numbers:
      print("You guessed correctly!")
  else:
    print("You guessed incorrectly!")

#5
list1 = [8,19,148,4]
list2 = [9,1,33,83]
result = []
for i in list1:
  for j in list2:
    result.append(i * j)

print(result)
