
# coding: utf-8

# ## 1.1  Write a Python Program(with class concepts) to find the area of the triangle using the below formula. 
#  
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
#  
# Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass. 
# 

# In[15]:


class Triangle:
    def __init__(self, a,b,c):
        self.a = a
        self.b=b
        self.c= c
        self.area=0
    def Area(self):
        # calculate the Perimeter
        self.s = (self.a + self.b + self.c)/2
        self.area =(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c)) ** 0.5
        return self.area

def main():
    a = float(input('Please Enter the First side of a Triangle: '))
    b = float(input('Please Enter the Second side of a Triangle: '))
    c = float(input('Please Enter the Third side of a Triangle: '))
    s=Triangle(a,b,c)
    s.Area()
    print("The Area of a Triangle is" ,Area)

if __name__ == '__main__':
    
    main()


# ## 1.2  Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n. 

# In[10]:


def long_words(words, n):
    return filter(lambda x: len(x) > n, words)

longword=list(long_words(['Hi', 'Welcome', 'Jeevanandam'], 5))
print (longword)


# ## 2.1  Write a Python program using function concept that maps  list of words into a list of integers representing the lengths of the corresponding words​. 
#  Hint: ​If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] 
#  Here 2,3 and 4 are the lengths of the words in the list. 

# In[4]:


def leng_lists(words):
    return [len(word) for word in words]
    
words = ['abv', 'try me', 'test']

print (list(leng_lists(words)))


# ## 2.2  Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise. 

# In[2]:


def Chk_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
    if char not in vowels:
        return False
    return True


if __name__ == "__main__":
    print (Chk_vowel(1))
    print (Chk_vowel('a'))
    print (Chk_vowel('b'))
    print (Chk_vowel('I'))

