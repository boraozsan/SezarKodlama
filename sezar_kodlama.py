alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer=[]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift,direction):
    answer_text = ""
    if direction=="encode":
        for letter in text:
            if letter is not " ":
             x=alphabet.index(letter)
             new_letter=x+shift
             if new_letter<26:
                answer.append(alphabet[new_letter])
             else:
                new_letter=new_letter%26
                answer.append(alphabet[new_letter])
            else:
                answer.append(" ")
        for x in range(len(answer)):
         answer_text+=answer[x]
        print(answer_text)
    elif direction=="decode":
        for letter in text:
            while 26-shift>0:
                shift+=26
            if letter is not " ":
                x=alphabet.index(letter)
                new_letter=x-shift
                answer.append(alphabet[new_letter])
            else:
                answer.append(" ")
        for x in range(len(answer)):
         answer_text+=answer[x]
        print(answer_text)

encrypt(text,shift,direction)