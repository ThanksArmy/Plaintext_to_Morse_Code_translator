def build_dictionary():
  morse = ".-,-...,-.-.,-..,.,..-.,--.,....,..,.---,-.-,.-..,--,-.,---,.--.,--.-,.-.,...,-,..-,...-,.--,-..-,-.--,--..,-----,.----,..---,...--,....-,.....,-....,--...,---..,----."

  morsecode = morse.split(',')

  alphanum = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,0,1,2,3,4,5,6,7,8,9"

  an = alphanum.split(',')


  morse_dict = {}

  counter = 0

  for code in morsecode:
    letter = an[counter]
    morse_dict[letter] = code
    counter += 1

  return morse_dict

def get_input():
  text = input("What text would you like to translate? ")
  text = text.upper()
  return text

def main():
  morse_string = ""

  morse_dict = build_dictionary()
  text = get_input()

  for character in text:
    if character == " ":
      morse_string = morse_string + "   "
    else:
      morse_string = morse_string + morse_dict[character] + " "

  print(morse_string)
  
if __name__== "__main__":
  main()
