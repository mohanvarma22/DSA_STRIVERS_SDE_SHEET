'''brute force

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
    
        # Initialize an empty stack
        stack = []
        
        # Push each word onto the stack
        for word in words:
            stack.append(word)
        
        # Pop each word from the stack to get them in reverse order
        reversed_sentence = ""
        while stack:
            reversed_sentence += stack.pop() + " "
        
        # Remove the trailing space and return
        return reversed_sentence.strip()
    
'''

# optimal
def reverse_words(sentence):
    # Initialize an empty result to build the reversed sentence
    result = ""
    i = len(sentence) - 1  # Start from the end of the sentence
    
    while i >= 0:
        # Skip spaces
        while i >= 0 and sentence[i] == ' ':
            i -= 1
        
        # Find the start of the word
        j = i
        while i >= 0 and sentence[i] != ' ':
            i -= 1
        
        # Add the word to the result with a space if result is not empty
        if j >= 0:
            word = sentence[i + 1 : j + 1]  # Extract the word
            if result:
                result += " " + word
            else:
                result = word
    
    return result
