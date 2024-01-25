#!/usr/bin/env python3

class MyString:
    def __init__(self,value=""):
      self._value = value
  
    def get_value (self):
      return self._value
    
    def set_value (self,new_value):
      if type(new_value)== str:
        self._value = new_value
      else:
        print ("The value must be a string.")
        
    value =property(get_value,set_value)
    
    def is_sentence(self):
      if self._value[-1] == ".":
        return True
      else:
        return False
      
    def is_question(self):
      if self._value[-1] == "?":
        return True
      else:
        return False
      
    def is_exclamation(self):
      if self._value[-1] == "!":
        return True
      else:
        return False
      
    def count_sentences(self):
      value = self.value


      for punctuation in ['!','?']:
        value = value.replace(punctuation, '.')
    
      sentences = [sentence for sentence in value.split('.') if sentence]
    
      return len(sentences)