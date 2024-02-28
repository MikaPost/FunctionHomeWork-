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
#
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

# def naxErkar(nax):
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
# print(naxErkar("Ian xodoko gna  tu"))

#12. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառում ամենաշատ օգտագործված տառը։

