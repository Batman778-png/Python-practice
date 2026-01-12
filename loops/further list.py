
#continuing the further topic
## Modifying The List elements
fruits
o/p:
['apple', 'banana', 'cherry', 'kiwi', 'gauva']

fruits[1]="watermelon"
print(fruits)
o/p: ['apple', 'watermelon', 'cherry', 'kiwi', 'gauva']

## List Methods
fruits.append("orange") ## Add an item to the end
print(fruits)
o/p: ['apple', 'banana', 'cherry', 'kiwi', 'gauva', 'orange']

fruits.insert(1,"watermelon")
print(fruits)
o/p: ['apple', 'watermelon', 'banana', 'banana', 'cherry', 'kiwi', 'gauva', 'orange']

fruits.remove("banana") ## Removing the first occurance of an item
print(fruits)
o/p: ['apple', 'watermelon', 'banana', 'cherry', 'kiwi', 'gauva', 'orange']


## Remove and return the last element
popped_fruits=fruits.pop()
print(popped_fruits)
print(fruits)
o/p:orange
['apple', 'watermelon', 'banana', 'cherry', 'kiwi', 'gauva']


fruits.sort() ## SSorts the list in ascending order
fruits
['apple', 'banana', 'banana', 'cherry', 'gauva', 'kiwi', 'watermelon']



## Slicing List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])

o/p:
[3, 4, 5]
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10]
[1, 3, 5, 7, 9]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


### Iterating Over List

for number in numbers:
    print(number)
  
o/p:
1
2
3
4
5
6
7
8
9
10


## Iterating with index
for index,number in enumerate(numbers):
    print(index,number)
  
o/p:

0 1
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10

## Nested List Comphrension
lst1=[1,2,3,4]
lst2=['a','b','c','d']

pair=[[i,j] for i in lst1 for j in lst2]

print(pair)

o/p:
[[1, 'a'], [1, 'b'], [1, 'c'], [1, 'd'], [2, 'a'], [2, 'b'], [2, 'c'], [2, 'd'], [3, 'a'], [3, 'b'], [3, 'c'], [3, 'd'], [4, 'a'], [4, 'b'], [4, 'c'], [4, 'd']

 ## List Comprehension with function calls
words = ["hello", "world", "python", "list", "comprehension"]
lengths = [len(word) for word in words]
print(lengths)  # Output: [5, 5, 6, 4, 13]
