#首先我們來創立一個list吧。
letters = ['a','b','c']
#這邊我們需要這樣看，首先用 = 來分別看待左半部分，以及右半部分。
#左半部分，我們稱為變數。主要就是把右邊的東西，丟到左邊去，製作出左邊的東西等於右邊的東西。
#右半部分，則為一個list(清單)，裡面包含三個字元，'a'、'b'、'c'。
#在集合內，我們會把元素用,隔開。


#我來印出看看吧。
print(letters)

#但是如果今天，我只需要其中的一個元素我該如何做呢?

#他將會印出'a'
print(letters[0])

#請注意一下，在程式語言，多半都會從0開始數數唷。
#也就是說 'a'、'b'、'c'
#分別代表  0    1    2

#聰明的您，一定想到如果，我想要拿C的話呢。
print(letters[2])

#在來我們會學習如何新增元素進去、刪除元素、更新元素。

#更新元素
letters[0] = 'b'
print(letters)

#新增元素
letters.append('d')
print(letters)

#刪除元素
letters.remove('b')
print(letters)

#刪除元素-指定位址
del letters[0]
print(letters)