def string_length(word):
     return len(word)
word = str(input("Type something: "))
word = string_length(word)
print("The length is ", word)

def test_string_length():
   assert string_length('hello!') == 6
   assert string_length('banana') == 6
   assert string_length('8') == 1
   assert string_length('funnyguys') == 9
   assert string_length('101') == 3
   print("YOUR CODE IS CORRECT!")

   
test_string_length()