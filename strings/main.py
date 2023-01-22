# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Part 1
#Exercise 1
#print('1')
first_scorer = 'Ruud Gullit'
second_scorer = 'Marco van Basten'

#Exercise 2
#print('2')
goal_0 = 32
goal_1 = 54

#Exercise 3
#print('3')
scorers = first_scorer + ' ' + str(goal_0) + ', ' + second_scorer + ' ' + str(goal_1)
print(scorers)  

''' Aqui me quede, ver como se hace para que no aparezcan los parentesis al darle print al Ejercicio 3.'''

#Exercise 4
#print('4') 
report = first_scorer + ' scored in the ' + str(goal_0) + 'nd minute' '\n' + second_scorer + ' scored in the ' + str(goal_1) + 'th minute'
print(report)

#report_with_f = (f'{first_scorer} scored in the {str(goal_0)}nd minute \n{second_scorer} scored in the {str(goal_1)}th minute')
#print(report_with_f)


#Part 2
#Exercise 1
#print('1')
player = 'Hans van Breukelen'


#Exercise 2
#print('2')
#Using indexing
""" first_name = player[:4]
print(first_name)

last_name = player[5:18]
print(last_name)

last_name_len = len(last_name)
print(last_name_len) """

#Exercise 2
# Using Find() and Slice()
player = 'Hans van Breukelen'
x = player.find('Hans')
z = slice(x,4)
first_name = (player[z])
print(first_name)

#Exercise 3
#print('3')
y = player.find('van Breukelen')
w = slice(y,18)
last_name = (player[w])
#print(last_name)
last_name_len = (len(last_name))
print(last_name_len)


#Exercise 4
#print('4')
name_short = player[0:1] + '. ' + last_name
print(name_short)



#chant = first_name + '!'
#print(chant * len(first_name))

#chant = first_name + '!'
#Multiplier = len(first_name) -1
#print(Multiplier)
#print(chant * Multiplier + chant)

''' canto = first_name + '!'
Multiplier = len(first_name) -1
#print(Multiplier)
chant = (canto * Multiplier + canto)
print(chant) '''


#Exercise 5
#print('5')
canto = first_name + '!'
Multiplier = len(first_name) -1
#print(Multiplier)
chant = (((canto + ' ') * Multiplier) + canto)
print(chant)


#Exercise 6
#print(6)

good_chant = (chant[-1] != ' ')
print(good_chant)




