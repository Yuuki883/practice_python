#FizzBuzz
#1から100までの数字を出力するプログラムを書く。ただし、3の倍数のときには数字の代わりにFizzと出力し、5の倍数の時には数字の代わりにBuzzと出力する
#3,5の倍数の時にはFizzBuzzと出力する

for i in range(1,100):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)

#線形探索/データ構造の中の要素を一つずつ確認して探しているものを見つける手法
def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)

#回文
def palindrome(word):
  word = word.lower()
  return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("Mom"))

#アナグラム/文字を並べ替えて別の単語を作る
def anagram(w1,w2):
  w1 = w1.lower()
  w2 = w2.lower()
  return sorted(w1) == sorted(w2)

print(anagram("icecream","cinema"))
print(anagram("leaf","tree"))

#出現する文字数を数える
def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)

count_characters("Dynasty")

#出現する文字数を数える2
from collections import defaultdict

def count_characters(string):
  count_dict = defaultdict(int)
  for c in string:
    count_dict[c] += 1
    print(count_dict)

count_characters("Dynasty")

#再帰/大きな問題を小さい問題に分割して解決する分割倒置手法
def bottles_of_beer(bob):
    """ Prints 99 Bottle
        of Beer on the
        Wall lyrics.
        :param bob: Must
        be a positive
        integer.
    """
    if bob < 1:
        print("""No more 
                 bottles 
                 of beer 
                 on the wall. 
                 No more 
                 bottles of 
                 beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of 
             beer on the 
             wall. {} bottles
             of beer. Take one 
             down, pass it 
             around, {} bottles 
             of beer on the 
             wall.
          """.format(tmp, 
                     tmp, 
                     bob))
    bottles_of_beer(bob)

bottles_of_beer(90)

