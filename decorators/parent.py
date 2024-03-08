# Functions can be returned from other functions. 
# In the example below, parent returns the functions first_child or second_child.
def parent(num):
  def first_child():
    return "Hi, I am Emma"
  
  def second_child():
    return "Call me Liam"
  
  if num == 1:
    return first_child
  else: 
    return second_child
  
