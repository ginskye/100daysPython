alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift_amount, direction):
  if direction=="encode":
      cipher_text = ""
      for letter in text:
          position = alphabet.index(letter)
          new_position = position + shift_amount
          cipher_text += alphabet[new_position]
      print(f"The encoded text is {cipher_text}")
  elif direction=="decode":
      decoded = ""
      for letter in text:
          position = alphabet.index(letter)
          new_position = position - shift_amount
          decoded += alphabet[new_position]
      print(f"The decoded text is {decoded}")
    
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
#decaesar(text, shift, direction)

def tinycaesar(text, shift_amount, direction):
    result = ""
    if direction=="decode":
        shift_amount = shift_amount*(-1)
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        result += alphabet[new_position]
    print(f"The result is {result}")

tinycaesar(text, shift, direction)
 