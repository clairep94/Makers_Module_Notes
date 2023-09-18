'''
In this project you will build a personal diary 
system. You'll start by writing a couple of 
functions that will be useful later on.

Design

A function called make_snippet that takes a 
string as an argument and returns the first 
five words and then a '...' if there are more
than that.
'''

class PersonalDiary():
    def __init__(self) -> None:
        self.split_entry = []

    def make_snippet(self, entry: str) -> str:
        '''Creates a snippet of a string if it is over 5 words long.
        
            Parameters:
            - entry: a string containing words 
                - (eg. "How many words is this in the end?")

            Returns:
            - for strings 5 words or under, returns the entry
            - for strings over 5 words long, returns the first five words followed by "..."
                - (eg. "How many words is this...")        
        '''
        if self.count_words(entry) <= 5:
            return entry
        else:
            first_five = self.split_entry[:5]
            return " ".join(first_five) + "..."
    

    def count_words(self, entry: str) -> int:
        ''' Counts the number of words in a string

            Parameters:
            - entry: a string containing words
                - (eg. "How many words is this in the end?")

            Returns:
            - number of words as an integer
        '''
        self.split_entry = entry.split(" ")
        if entry == "":
            return 0
        else:
            return len(self.split_entry)


