#!/usr/bin/env python3
import time


# First experiential
a_tuple = (1,2,3,4,5)  # syntax
a_list = [1,2,3,4,5]  # syntax

# mutability of the list
a_list.append(37)  # add an element at the last position
a_list.remove(2)  # remove the first occurence of 2
a_list.pop(4)  # remove using a specified index (4)

print(a_list)
# sorted list and tuple
print(sorted(a_list))
print(sorted(a_tuple))

# checking by index
print(a_list[2])
print(a_tuple[2])

# running speed
start_time = time.time()

for i in a_list:
    print(i)

running_time_list = time.time() - start_time

for i in a_tuple:
    print(i)


running_time_tuple = time.time() - start_time

print(f"List iteration time: {running_time_list:.6f} seconds\n")
print(f"Tuple iteration time: {running_time_tuple:.6f} seconds")

# Experiential learning 2
sentence = input("Enter a sentence: ").split(" ")
word = set(sentence) # create an empty set

for i in sentence:
    word.add(i)

def len_unique_word(word):
    word = set(word)
    print(f"The length of unique word is {len(word)}")

len_unique_word(word)
