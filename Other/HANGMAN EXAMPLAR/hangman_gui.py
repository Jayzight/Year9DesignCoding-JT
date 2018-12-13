'''
Created on 4 Apr 2016

@author: aml
'''


from Tkconstants import W
from Tkinter import Tk, Button, Entry, Label, StringVar, Canvas
import tkMessageBox

from hangman import Hangman
from turtle_hangman import TurtleHangman


class HangmanGUI(Tk):
    
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        
        self.initialise()
        self.prep_buttons()
        
    def prep_buttons(self):
        new_game = Button(self, command=self.hangman.begin_new_game, text='Restart')
        new_game.grid(column=2, row=5, sticky=W)
        
        guess_letter = Button(self, command=lambda: self.guess(True), text='Guess letter')
        guess_letter.grid(column=3, row=5, sticky=W)
        
        guess_button = Button(self, command=lambda: self.guess(False), text='Guess word')
        guess_button.grid(column=4, row=5, sticky=W)
        
    def initialise(self):
        self.hangman = Hangman(self)
        self.my_word = StringVar()
        self.my_word.set("Word: " + 
                         self.hangman.word_of_underlines(len(self.hangman.word_to_guess)))
        
        self.tried_so_far = StringVar()
        self.tried_so_far.set('Letters tried so far: ')
        
        self.guesses_left = StringVar()
        self.update_no_of_guesses()
        
        self.geometry('{}x{}'.format(545, 400))
        
        self.grid()
        
        
        word = Label(self, textvariable=self.my_word)
        word.grid(column=1, row=7, sticky=W)
        
        tried = Label(self, textvariable=self.tried_so_far)
        tried.grid(column=1, row=8, sticky=W)
        
        no_guesses = Label(self, textvariable=self.guesses_left)
        no_guesses.grid(column=1, row=9, sticky=W)
        
        turtle_canvas = Canvas(self, width=300, height=450)
        self.th = TurtleHangman(turtle_canvas)
        turtle_canvas.grid(column=1, row=10, rowspan = 8, columnspan = 3)
        
        infotext = 'Hangman v1.0 by AML'
        info = Label(self, text = infotext)
        info.grid(column = 4, row = 12, columnspan = 2)
       
        
        
    def update_my_word(self):
        self.my_word.set('Word: ' + self.hangman.my_word)
        
    def update_tried_so_far(self):
        self.tried_so_far.set('Letters tried so far: ' + self.hangman.l_tried())
        
    def update_no_of_guesses(self):
        self.guesses_left.set('Guesses left: ' + 
                              str(Hangman.max_number_of_guesses - self.hangman.number_of_guesses))
    
        
    def guess(self, guessing_letter):
        title = 'Guess a '
        if guessing_letter:
            title += 'letter'
        else:
            title += 'word'
        
        
        g_window = Tk()
        g_window.title(title)
        g_window.grid()
        
        entry = Entry(g_window)
        entry.grid(column=1, row=1)
       
        
        confirm = Button(g_window, command=lambda: 
                         self.send_input(guessing_letter, entry.get(), g_window), text='Confirm')
        confirm.grid(column=1, row=3)
        
       
     
    def send_input(self, guessing_letter, user_guess, g_window):
        
        
        if user_guess.isalpha():
            if (guessing_letter and len(user_guess) > 1):
                tkMessageBox.showerror('Error', 'Please only guess a letter')
            else:
                if guessing_letter:
                    self.hangman.guess_letter(user_guess)
                else:
                    self.hangman.guess_word(user_guess)
                    
                g_window.destroy()
        else:
            tkMessageBox.showerror('Error', 'Please make a valid guess')
            
    def award_win(self):
        tkMessageBox.showinfo('Winner!', 'You won. Click on Restart to play again')
        
    def notify_loser(self):
        tkMessageBox.showinfo('Loser!', 'You lost. Word was *' + self.hangman.word_to_guess + '*. Click on Restart to play again') 
            
               
    
if __name__ == "__main__":
    hg = HangmanGUI(None)
    hg.title('Hangman')
    hg.mainloop()
        





