#!/usr/bin/env python
# coding: utf-8

# """
# Problem Statement​ ​1:
# Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()
# Problem Statement​ ​2:
# Write a Python program to implement your own myfilter() function which works exactly
# like Python's built-in function filter()
# """

# In[40]:


def myreduce(anyfunc, sequence):

 # Get first item in sequence and assign to result
    first = sequence[0]
 # iterate over remaining items in sequence and apply reduction function 
    for i in sequence[1:]:
        first = anyfunc(first, i)
    return first


# In[ ]:


# test myreduce function
def sum(x,y): return x + y


# In[48]:


def  multi(x,y): return x * y


# In[55]:


print ("Sum on list [1,2,3] using custom reduce function " + str(myreduce(sum, [1,2,3])) )
print ("product on list [1,2,3] using custom reduce function " + str(myreduce(multi, [1,2,3])))


# In[63]:


# filter funcion creation

def myfilter(anyfunc,sequance):
    
    result = []
    
    for i in sequance:
        if anyfunc(i):
            result.append(i)
            
    return result            


# In[64]:


# test myfilter function
def ispositive(x):
 if (x <= 0): 
  return False 
 else: 
  return True


# In[65]:


print ("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,5])))


# In[66]:





# """
# Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
# """

# In[69]:


word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
alphabet_list 


# In[93]:


input_list  = ['x','y','z']
result = [i*num  for i in input_list  for num in range(1,5)]
result


# In[123]:


input_list  = ['x','y','z']
result = [i*num   for num in range(1,5) for i in input_list ]
result


# In[78]:


input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
result


# In[84]:


input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)]
result


# In[90]:


input_list = [1,2,3]
result = [(y,x) for x in input_list for y in input_list]
result


# In[114]:


#Implement a function longestWord() that takes a list of words and returns the longest one.

def longest_word(word_list):
    word_len = []
    for i in word_list:
        word_len.append((i,len(i)))
    word_len.sort( )
    return word_len[-1][0]


# In[115]:


longest_word(['hadjkajdskjas','aaddad','asdadasda'])


# In[131]:


def Area_triangle(a,b,c):
    
    s = (a+b+c)/2
    
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    
    return area
    
    


###########
1.2
Write a function filter_long_words() that takes a list of words and an integer n and returns the list
of words that are longer than n.
###########
def filterlongword(string,number):
    listwords = []
    for i in range(len(string)):
        if len(string[i]) > number:
            listwords.append(string[i])
    return listwords



##############

###########
2.1
Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words .
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list#################



 def wordlength(wordlist):
    return  list(map(lambda x: len(x), wordlist))


wordlength(wordlist =['sadsdsdf','sdfdsfsdf','sdfdsfdsfdsfsd'])
Output:  [8, 9, 14]

################################################

2.2
Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
a vowel, False otherwise.
###########


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels


