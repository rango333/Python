#!/usr/bin/env python
# coding: utf-8

# ## Hangman rules

# In[3]:


#First, we need to import libraries needed for work and set new functions.
 
# Import the random library
import random
# Import the string library
import string

# Set the load_words function
def load_words():
  # Set the word_list variable
  word_list = open('words.txt', 'r').readline().split()
  # Return the word_list
  return word_list


# ## Random Word Generator

# In[5]:


# Set the choose_word_random function 
def choose_word_random(word_list):
  # Return the random word from the word_list
  return  random.choice(word_list)

# Test the function
test_word_list = ['sun', 'sky', 'water', 'fire', 'nature'] 
print(choose_word_random(test_word_list))

# One of the possible results: sun


# ## Guessed Word

# In[7]:


# Set the is_word_guessed function 
def is_word_guessed(gameword, letters_already_guessed):
  # Set the condition
  if set(gameword) & set(letters_already_guessed) == set(gameword):
   # Return True
    return True
  else:
    # Return False
    return False

# Test the function
test_gameword = 'sunny'
test_letters_already_guessed = ['s', 'u', 'n', 'y']
print(is_word_guessed(test_gameword, test_letters_already_guessed))

# Result: True


# ## State of Affairs

# In[12]:


# We need to see the number of right letters guessed already
# and the remaining letters that need to be guessed. 

# Set the get_guessed_word function 
def get_guessed_word(gameword, letters_already_guessed):
  result_list = []
  # Set for loop to work with the gameword 
  for i in range(len(list(gameword))):
    # Set the condition
    if list(gameword)[i] in set(letters_already_guessed):
      # Append correct guessed letters to the result_list
      result_list.append(list(gameword)[i])
    else:
      # Append '_ ' to the result_list
      result_list.append('_ ')
  # Appending the space to the result_list
  return ''.join(result_list)

# Test the function  
test_gameword = 'sunny'
test_letters_already_guessed = ['n']
print(get_guessed_word(test_gameword, test_letters_already_guessed))

#Result: _ _ nn_


# ## Available Letters

# In[15]:


# To help users, we show available letters after every guess. The letter has
# to be deleted from the available_list if it has been used already. To do
# that, we create the get_available_letters function.

# Set the get_available_letters() function
def get_available_letters(letters_already_guessed):
  # Set the variable-alphabet available_list
  available_list = list(string.ascii_lowercase)
  # Set for loop to work with the available_list
  for i in range(-len(available_list), 0):
    # Set the condition
    if available_list[i] in letters_already_guessed:
      # Delete an element from the available_list
      del available_list[i]
  # Appending the space
  return ''.join(available_list)

# Test the function
test_letters_already_guessed = ['s', 'u', 'm', 'n', 'a']
print(get_available_letters(test_letters_already_guessed))

#Result: bcdefghijklopqrtvwxyz 


# ## Hints 1/2

# In[16]:


# We will implement the hint part of the program in 2 steps. The
# hints_match function defines if the current state of gameword(correct
# guessed letters and gaps) matches the exact word from the file. If it
# does, the function returns True or False otherwise.

# Set the hints_match function  
def hints_match(word_to_match, word_from_list):
  # Delete spaces in the word_to_match
  test_list = list(word_to_match.replace(' ', ''))
  other_list = list(word_from_list)
  # Compare lengths of the test_list and the other_list
  if len(test_list) != len(other_list):
    # Return False
    return False
  else:
    counter = 0
    # Set for loop to work with the test_list
    for i in range(len(test_list)):
      if test_list[i] == '_':
        if other_list[i] not in test_list:
          # Increase the counter
          counter += 1
      elif test_list[i] == other_list[i]:
        # Increase the counter
        counter += 1
  if counter == len(word_to_match.replace(' ', '')):
    return True
  else:
    return False

# Test the function 
test_word_to_match = 's_ _ _ _' 
test_word_from_list = 'sunny'
print(hints_match(test_word_to_match, test_word_from_list))

# Result: True


# ## Hints 2/2

# In[18]:


# The second hint function is named show_possible_matches and shows
# the word from the file (word_from_list) if this word matches the current
# state of the gameword.

# Note: The function we will implement doesn't work without the function
#       from the previous step. The hints_match function has already been
#       implemented in the code.

# The word_list to test
test_word_list = ['sun', 'sky', 'water', 'fire', 'nature']

# Set the show_possible_matches function
def show_possible_matches(word_to_match):
  possible_matches=[]
  # Set for loop to work with the test_word_list
  for word in test_word_list:
    if hints_match(word_to_match, word):
      # Append an element to the possible matches list_
      possible_matches.append(word)
  # Set condition if the possible_matches list is empty
  if len(possible_matches) == 0:
    return 'No matches found'
  else:
    return ' '.join(possible_matches)

# Test the function
test_word_to_match = 's_ _ '
print(show_possible_matches(test_word_to_match))

# Result: sun sky


# ## Main Body

# In[20]:


def hangman(gameword):
  used_letters = []
  guesses_remaining, warnings_remaining = 6, 3
  print('A gameword is', len(gameword), 'letters long')
  
  while True:
    if not is_word_guessed(gameword, used_letters):
      print('You have', int(guesses_remaining), 'guess(es) left and', int(warnings_remaining), 'warning(s) left!' + '\nAvailable letters: ', get_available_letters(used_letters) + '\nGame word: ', get_guessed_word(gameword, used_letters))
      guess = str.lower(input('Please, input a letter: '))
      
      if not guess.isalpha():
        if guess == '!':
          print('Possible word matches are: ', show_possible_matches(get_guessed_word(gameword, used_letters)))
        else:
          print('That is not a valid symbol.')
          warnings_remaining -= 1
          if warnings_remaining < 0:
            print('You have no warnings left so you lose 1 guess!')
            guesses_remaining -= 1
          else:
            print('You loose 1 warning!')
      
      elif guess in set(used_letters):
        warnings_remaining -= 1
        print('Oops! You`ve already guessed that letter.')
        if warnings_remaining < 0:
          print('You have no warnings left so you lose 1 guess!')
          guesses_remaining -= 1
        else:
          print('You loose 1 warning!')
      
      elif guess in set(gameword):
        print('Super! Good guess!')
        used_letters.append(guess)
      
      else:
        used_letters.append(guess)
        print('Oops! That letter is not in my word!')
        print('You loose 1 guess!')
        guesses_remaining -= 1        
      
      if guesses_remaining <= 0:
        print('Sorry, you ran out of guesses. The word was: ', gameword)
        break    
    else:
      print('Congratulations, you won!' + 'The gameword is: ', gameword)
      break


# ## Final Step

# In[ ]:


# Play the game!

if __name__ == '__main__':
  # Call the load_words() function
  word_list = load_words()
  # Set the gameword
  gameword = choose_word_random(word_list)
  # Call the hangman() function
  hangman(gameword)


# In[ ]:




