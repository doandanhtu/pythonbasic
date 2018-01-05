weighted_choices = [('Red', 3), ('Blue', 2), ('Yellow', 1), ('Green', 4)]

#population = [val for val, cnt in weighted_choices for i in range(cnt)]

'''population = []
for val, cnt in weighted_choices:
    for i in range(cnt):
        population.append(val)'''

for val, cnt in weighted_choices:
  # the first for loop will be executed len(weighted_choices) times = 4
  for i in range(cnt):
  # the second for loop will be executed cnt times
  # for each execution of the outer loop
  # (cnt = second element of each tuple)
      print (val) # it will print each first element of the tuple 'Red', ...
                # len(weighted_choices) * cnt times


#Lets make the comprehension simple to start with

simple = [val for val, cnt in weighted_choices]
#This simple list comprehension is doing this:

#For every item in weighted_choices break the first part and assign it to val and the second part to cnt.
#Take the val and create a new array out of each val
#This would produce:

#['Red','Blue','Yellow''Green']
#Now lets look the second part lets make a simple list comprehension first

second_part = ['Red' for i in range(3)]
#This second part of the list comprehension is doing this:

#For every i in range(3) (the numbers [0,1,2])
#Discard i and add 'Red' to the list
#This would produce:

#['Red','Red','Red']
#Combining both comprehensions:

population = [val for val, cnt in weighted_choices for i in range(cnt)]
#This simple list comprehension is doing this:

#For every item in weighted_choices break the first part and assign it to val and the second part to cnt. (e.g 'Red' and 3 for the first item)
#Take the val and
#For every i in range(cnt) (the numbers [0,1,2] if cnt is 3) discard i and add val to the list


