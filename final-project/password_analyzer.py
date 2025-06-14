import argparse
import json
import os
import sys
from datetime import datetime
from typing import List, Dict
import zxcvbn
import nltk
from nltk.corpus import words
from nltk.tokenize import word_tokenize
import itertools
from tkinter import Tk, Label, Button, Entry, Text, END, messagebox
from tkinter.ttk import Combobox

# Download required NLTK data
nltk.download('words')

class PasswordAnalyzer:
    def __init__(self):
        self.common_words = set(words.words())
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.digits = "0123456789"
        
    def analyze_password(self, password: str) -> Dict:
        """Analyze password strength using zxcvbn"""
        result = zxcvbn.zxcvbn(password)
        return {
            'score': result['score'],
            'feedback': result['feedback'],
            'crack_time': result['crack_times_display'],
            'entropy': result['entropy']
        }
    
    def generate_wordlist(self, name: str = '', birthdate: str = '', pet: str = '', 
                         output_file: str = 'wordlist.txt') -> List[str]:
        """Generate custom wordlist based on user inputs"""
        wordlist = set()
        
        # Add user inputs
        if name:
            wordlist.update(self._generate_variations(name))
        if birthdate:
            wordlist.update(self._generate_date_variations(birthdate))
        if pet:
            wordlist.update(self._generate_variations(pet))
            
        # Add common patterns
        wordlist.update(self._generate_common_patterns())
        
        # Add leetspeak variations
        wordlist.update(self._generate_leetspeak(list(wordlist)))
        
        # Write to file
        with open(output_file, 'w') as f:
            for word in sorted(wordlist):
                f.write(word + '\n')
                
        return list(wordlist)
    
    def _generate_variations(self, word: str) -> List[str]:
        variations = set()
        variations.add(word.lower())
        variations.add(word.upper())
        variations.add(word.capitalize())
        
        # Add with special characters
        for char in self.special_chars[:5]:  # Limit to first 5 special chars
            variations.add(word + char)
            variations.add(char + word)
        
        return variations
    
    def _generate_date_variations(self, date_str: str) -> List[str]:
        variations = set()
        # Try different date formats
        formats = ['%Y%m%d', '%d%m%Y', '%m%d%Y', '%Y%d%m']
        
        for fmt in formats:
            try:
                dt = datetime.strptime(date_str, '%Y-%m-%d')
                variations.add(dt.strftime(fmt))
            except ValueError:
                continue
        
        return variations
    
    def _generate_common_patterns(self) -> List[str]:
        patterns = [
            'password', '123456', 'qwerty', 'letmein',
            'admin', 'root', 'user', 'pass'
        ]
        return patterns
    
    def _generate_leetspeak(self, words: List[str]) -> List[str]:
        leet_dict = {
            'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$',
            't': '7', 'g': '6', 'l': '1', 'z': '2'
        }
        
        variations = set()
        for word in words:
            leet_word = ''
            for char in word.lower():
                leet_word += leet_dict.get(char, char)
            variations.add(leet_word)
        
        return variations

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Password Strength Analyzer & Wordlist Generator")
        self.root.geometry("800x600")
        
        # Password Analysis Section
        Label(self.root, text="Password Analysis", font=("Arial", 14, "bold")).pack(pady=10)
        
        self.password_entry = Entry(self.root, show="*", width=50)
        self.password_entry.pack(pady=5)
        
        self.analyze_btn = Button(self.root, text="Analyze Password", 
                                command=self.analyze_password)
        self.analyze_btn.pack(pady=5)
        
        self.results_text = Text(self.root, height=10, width=70)
        self.results_text.pack(pady=10)
        
        # Wordlist Generation Section
        Label(self.root, text="\nWordlist Generator", font=("Arial", 14, "bold")).pack(pady=10)
        
        Label(self.root, text="Name:").pack()
        self.name_entry = Entry(self.root, width=50)
        self.name_entry.pack(pady=5)
        
        Label(self.root, text="Birthdate (YYYY-MM-DD):").pack()
        self.birthdate_entry = Entry(self.root, width=50)
        self.birthdate_entry.pack(pady=5)
        
        Label(self.root, text="Pet Name:").pack()
        self.pet_entry = Entry(self.root, width=50)
        self.pet_entry.pack(pady=5)
        
        self.generate_btn = Button(self.root, text="Generate Wordlist", 
                                 command=self.generate_wordlist)
        self.generate_btn.pack(pady=10)
        
        self.status_label = Label(self.root, text="")
        self.status_label.pack(pady=5)
        
        self.analyzer = PasswordAnalyzer()
        
    def analyze_password(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("Warning", "Please enter a password")
            return
            
        result = self.analyzer.analyze_password(password)
        self.results_text.delete(1.0, END)
        self.results_text.insert(END, json.dumps(result, indent=2))
        
    def generate_wordlist(self):
        name = self.name_entry.get()
        birthdate = self.birthdate_entry.get()
        pet = self.pet_entry.get()
        
        try:
            self.analyzer.generate_wordlist(name, birthdate, pet)
            self.status_label.config(text="Wordlist generated successfully!", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg="red")
            
    def run(self):
        self.root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer and Wordlist Generator")
    parser.add_argument('--cli', action='store_true', help="Run in command line mode")
    
    args = parser.parse_args()
    
    if args.cli:
        # CLI mode
        analyzer = PasswordAnalyzer()
        
        # Password Analysis
        print("\nPassword Analysis:")
        password = input("Enter password to analyze: ")
        result = analyzer.analyze_password(password)
        print("\nAnalysis Results:")
        print(json.dumps(result, indent=2))
        
        # Wordlist Generation
        print("\nWordlist Generation:")
        name = input("Enter name (optional): ")
        birthdate = input("Enter birthdate (YYYY-MM-DD, optional): ")
        pet = input("Enter pet name (optional): ")
        
        print("\nGenerating wordlist...")
        analyzer.generate_wordlist(name, birthdate, pet)
        print("Wordlist generated successfully!")
    else:
        # GUI mode
        gui = GUI()
        gui.run()

if __name__ == "__main__":
    main()
