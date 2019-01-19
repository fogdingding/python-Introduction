#我們先來創造一個dict
ID_and_name = {10311201 : '黃小美', 10311202 : '張三狗', 10311203 : '李小四'}
print(ID_and_name)

#在來我們透過索引來找尋各別的姓名
print( ID_and_name[10311201] )
print( ID_and_name[10311202] )

#當然我們也能刪除元素
del ID_and_name[10311201]
print(ID_and_name)

#我們也能用另一種確認方法
10311201 in ID_and_name
10311202 in ID_and_name