# 1.Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից թվերի գումարը։

# def ssum(*a):
#     b = 0
#     for i in a:
#         b += i
#     return b
#
# print(ssum(5, 9, 7, 4))


# 2.Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից տողերի քանակը։

# def tox(*a):
#     b = 0
#     for i in a:
#         b += 1
#     return b
#
# print(tox("good", "hello", "bed"))


# 3.Գրել ֆունկցիա որը կվերադարձնի ստասած արգումենտների միջին թվաբանականը։

# def mijinTva(*a):
#     b = 0
#     c = 0
#     for i in a:
#         b += i
#         c += 1
#     b /= c
#     return b

# print(mijinTva(1, 2, 3))


#4. Գրել ֆունկցիա որը կստանա 2 արգումենտ և կվերադարձնի այդ արգումենտերի հետ կատարած մաթեմատիկական գործողությունների
#արդյունքները։

# def matem(a, b):
#     plus = a + b
#     hanum = a - b
#     baj = a / b
#     baz = a * b
#     return plus, hanum, baz, baj
#
# print(matem(1, 2))

#5.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված ամբողջությամբ մեծատառ ֆունկցիան
#(upper օգտագործե չի կարելի)։

# def uupper(a):
#     b = ""
#     for i in a:
#         b += i.upper()
#     return b
#
# print(uupper("hello"))

########################################KAMKAMKAMKAM#############################################################

#print(list(map(lambda x: x.upper(), "hello")))



#6.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված ամբողջությամբ փոքրատառ ֆունկցիան
#(lower օգտագործե չի կարելի)։

# def uupper(a):
#     b = ""
#     for i in a:
#         b += i.lower()
#     return b
#
# print(uupper("HELLO"))


#7.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված բոլոր բառերի առաջին տառերը
# մեծատառ ֆունկցիան (title օգտագործել չի կարելի)։

# def mec1(*a):
#     b = []
#     for i in a:
#         b.append(i[0].upper() + i[1:])
#     return b
#
# print(mec1("mika", "hello", "good"))


#8. Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված հակառակ։

# def tars(a):
#     return a[::-1]
#
# print(tars("mika"))

#9. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և 2 թիվ։ Այն պետք է վերադարձնի տրված 2 թվերի արանքում եղած ենթատողը։

# def lurjChidem(tox, a, b):
#     c = ""
#     for i in range(a - 1, b):
#         c += tox[i]
#     return c
#
# print(lurjChidem("xodokoIan", 2, 5))


#10. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառը։

# def naxErkar(nax):
#     nax = nax.split()
#     erkar = nax[0]
#     for i in nax:
#         if len(erkar) < len(i):
#             erkar = i
#     return erkar
#
# print(naxErkar("Ian xodoko gna  tun"))


#11. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաշատ օգտագործված տառը։

# def shatTra(nax):
#     dict = {}
#     b = 0
#     c = ''
#     for i in nax:
#         if i.isalpha():
#             d = i.lower()
#             if d not in dict:
#                 dict[d] = 1
#             else:
#                 dict[d] += 1
#
#             if dict[d] > b:
#                 b = dict[d]
#                 c = d
#     return c
#
# print(shatTra("Ian xodoko gna  tu"))

#12. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառում ամենաշատ օգտագործված տառը։

# def naxErkar(nax):
#     nax = nax.split()
#     erkar = nax[0]
#     for i in nax:
#         if len(erkar) < len(i):
#             erkar = i
#     return shatTra(erkar)
#
# def shatTra(nax):
#     dict = {}
#     b = 0
#     c = ''
#     for i in nax:
#         if i.isalpha():
#             d = i.lower()
#             if d not in dict:
#                 dict[d] = 1
#             else:
#                 dict[d] += 1
#
#             if dict[d] > b:
#                 b = dict[d]
#                 c = d
#     return c
#
# print(naxErkar("Ian xodoko gna  tun"))

#13.Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և թիվ։
#Կվերադարձնի այդ թվին համապատասխն ինդեքսում եղած էլէմենտները՝ սկզբից և վերջից։

# def aga(tox, tiv):
#     a = ""
#     for i in range(tiv, len(tox)):
#         a += tox[i]
#     return a
# print(aga("xodoko", 2))


#15. Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կստուգի պոլինդրոմ է այն թե ոչ։

# def polidrom(tiv):
#     a = str(tiv)[::-1]
#     if int(a) == tiv:
#         return "palindrome"
#     return "No palindrome"
#
#
# print(polidrom(232))


# def is_polynomial(number):
#     n = number
#     rev = 0
#     while (number > 0):
#         dig = number % 10
#         rev = rev * 10 + dig
#         print(rev)
#         number = number // 10
#     if (n == rev):
#         return "palindrome"
#     return "no palindrome"
#
# print(is_polynomial(121))



#16. Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի իրեն ամենամոտ պոլինդրոմ թիվը։

# def palindrome(num):
#     return str(num) == str(num)[::-1]
#
#
# def motPalindrome(number):
#     a = number
#     b = number
#     while True:
#         if palindrome(a):
#             return a
#         elif palindrome(b):
#             return b
#         else:
#             a -= 1
#             b += 1
#
# print(motPalindrome(125))


#17. Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի իր առաջին և վերջին թվանշանների արտադրյալը։

# def arajinVerjinB(num):
#     arajin = num % 10
#     verjin = num
#     while len(str(verjin)) != 1:
#         verjin //= 10
#     return arajin * verjin
#
#
# print(arajinVerjinB(256))


#18. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում եղած տողերի քանակությունը։

# def listcount(list):
#     return len(list)
#
# print(listcount([1, 2, 3, 4]))



#19․Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա թվերից առավելագույնը։

# def mmax(list):
#     a = list[0]
#     for i in range(1, len(list)):
#         if list[i] > a:
#             a = list[i]
#     return a
#
# print(mmax([1, 6, 3, 4]))



#20.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի այդ լիստում առկա երկնիշ զույգ թվերը։

# def erkZuyg(list):
#     a = []
#     for i in range(len(list)):
#         if list[i] % 2 == 0 and len(str(list[i])) == 2:
#             a.append(list[i])
#     return a
#
# print(erkZuyg([1, 64, 3, 43, 56, 4, 47, 489]))


#21.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի այդ լիստում առկա թվերի միջին թվաբանականը։

# def mijinTva(list):
#     a = 0
#     for i in list:
#         a += i
#     return a / len(list)
#
# print(mijinTva([1, 2, 3]))


#22.Գրել ֆունկցիա որը որպես առգումենտ կստանա տողերի լիստ և կվերադարձնի այդ տողերի երկարությունները պարունակող լիստ։

# def toxLen(list):
#     a = []
#     for i in list:
#         a.append(len(i))
#     return a
#
# print(toxLen(["hello", "good", "mika"]))


#23.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա թվերը դասավորված նվազման կարգով։

#24.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա տողերը դասավորված երկարությունների նվազման կարգով։

#25.Գրել ֆունկցիա որը որպես արգումենտ կընդունի կընդունի տողերի լիստ և կվերադարձնի այն բառը որը կպարունակի ամենաշատ ձայնավորները։

#26.Գրել ֆունկցիա որը որպես արգումենտ կընդունի նախադասությունների լիստ և կվերադարձնի այն նախադասությունը որը կպարունակի ամենաշատ բառերը։

#27.Գրել ֆունկցիա որը որպես արգումենտ կստանա տող /իրականում նախադասություն և կվերադարձնի այդ նախադասությունում առկա ամենամեծ թիվը /ոչ թե թվանշանը/։

#28 Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝մարդկանց նկարագրող և կվերադարձնի այն բառարանը որում մարդու
#տարիքն ամենամեծն է։

#29Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ ուսանողների նկարագրող և կվերադարձնի այդ ուսանողների լիստը
#դասավորված աճման կարգով՝ ըստ միասվորների։

#30Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ համալսարանների նկարագրող և կվերադարձնի այն համալսարանը որի ,
#անվանումն ամենաերկարն է։
