'''
Created on 31 Mar 2016

@author: aml
'''

import random


class Hangman:
    possible_words = ['random', 'lackadaisical', 'extreme', 'archaeologist', 'innocuous']
    max_number_of_guesses = 10
    
    def __init__(self, gui):
        self.gui = gui
        self.prep_for_new_game()
        
    def prep_for_new_game(self):
        self.number_of_guesses = 0
        self.word_to_guess = self.random_word_to_guess()
        self.word_guessed = False
        self.my_word = self.word_of_underlines(len(self.word_to_guess))
        self.letters_tried = []
        
    def word_of_underlines(self, l):
        wd = ''
        for i in range (0, l):
            wd += '*'
        return wd
    
    def recompute_my_word(self, letter):
        word_as_list = list(self.my_word)
        
        
        for pos in self.find_letter_positions_in_word(letter, self.word_to_guess):
            word_as_list[pos] = letter
           
            
        self.my_word = ''.join(word_as_list)
        
        
    def find_letter_positions_in_word(self, letter, word):
        pos_list = []

        for i in range (0, len(word)):
            if word[i] == letter:
                pos_list.append(i)
        
        return pos_list
        
        
    def random_word_to_guess(self):
        return Hangman.possible_words[random.randint(0, 4)]
    
    def begin_new_game(self):
        self.prep_for_new_game()
        self.gui.initialise()
          
    
    def check_for_end(self):
        if self.word_guessed:
            self.gui.award_win()
            return
            
        if self.number_of_guesses == Hangman.max_number_of_guesses:
            self.gui.notify_loser()
            return
            
                     
    def guess_letter(self, letter):
        
        self.letters_tried.append(letter)
        self.gui.update_tried_so_far()
        
        self.recompute_my_word(letter)       
        
        if self.my_word == self.word_to_guess:
            self.word_guessed = True
        self.gui.update_my_word()   
        
        if len(self.find_letter_positions_in_word(letter, self.word_to_guess)) == 0:
            self.number_of_guesses += 1
            self.gui.update_no_of_guesses()
            self.gui.th.update_hangman_viz(self.number_of_guesses)
        
        self.check_for_end()
        
        
    def l_tried(self):
        tried = ''
        
        for letter in self.letters_tried:
            tried += str(letter)
            tried += ' '
            
        return tried
        
        
    def guess_word(self, word):
        #print('You have guessed the whole word: ' + word)
        
        if word == self.word_to_guess:
            self.word_guessed = True
        else:   
            self.number_of_guesses += 1
            self.gui.update_no_of_guesses()
            self.gui.th.update_hangman_viz(self.number_of_guesses)
        
        self.check_for_end()
        
                    
        
        
          
         
                   
        
            
