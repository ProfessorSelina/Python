# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

dict_with_letter = {1: ("А","Е","В","И","Н","О","Р","С","Т", 
 'A','E','I','O','U','L','N','S','T','R'), 
 2: ("Д","К","Л","М","П","У", 
 'D', 'G'), 
 3: ("Б","Г","Ё","Ь","Я", 
 'B','C','M', 'P'), 
 4: ("Й","Ы", 
 'F', 'H', 'V', 'W', 'Y'), 
 5: ("Ж","З","Х","Ц","Ч", 
 'K'), 
 6: ("Ш", "Э","Ю", 
 'J','X'), 
 7: ("Ф","Щ","Ъ", 
 'Q','Z') 
 } 
 
def dicting(dict_with, words): 
 sum_points = 0 
 for key, value in dict_with.items(): 
  for letter in words.upper(): 
   if letter in value: 
    sum_points += key 
 print(sum_points) 
word = str(input()) 
dicting(dict_with_letter,word)