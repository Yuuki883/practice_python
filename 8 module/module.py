#モジュール/分割したコードが書かれているファイル。python本体に含まれている組み込みモジュールもある
#モジュールを使う場合
import [モジュール名]
モジュール名.[コード]

#math
import math
math.pow(2, 3)

#random
import random
#範囲内の数字を無作為に出力
random.randint(0,15)

#statistics
import statistics
#mean(平均値)
nums = [3,5,9,10,11,12,13,14,15,16,17]
statistics.mean(nums)
#median(中央値)
nums = [10,20,30]
statistics.median(nums)
#mode(最頻度)
nums = [10,20,30,30,30]
statistics.mode(nums)

#keyword
import keyword
#pythonのキーワードか確認
keyword.iskeyword("for")
keyword.iskeyword("def")
keyword.iskeyword("footboll")