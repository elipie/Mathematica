import re #used to see if 'i' is a string. 
red = '\033[0;31m' # For error
regular = '\033[0m' # For regular

ops = [
  '+',
  '-',
  '*',
  '/',
  '<', 
  '>',
  '!=',
  '=', # for !=
  '!' # for !=
]
#numvars = {}


while True:
  print("Type a math equation, then press enter \n")

  _src = input("> ")
  inum = 0

  for i in _src:
    _src.strip()
    if i in ops:
      if i == ops[0]:
        num1 = int(_src[:inum])
        inum +=1
        num2 = int(_src[inum:])
        
        print(num1+num2)
      # + 
      elif i == ops[1]:
        num1 = int(_src[:inum])
        inum +=1
        num2 = int(_src[inum:])

        # -
      elif i == ops[2]:
        num1 = int(_src[:inum])
        inum +=1
        num2 = int(_src[inum:])
        print(num1*num2)
        # * 
      elif i  == ops[3]:
        num1 = int(_src[:inum])
        inum +=1
        num2 = int(_src[inum:])  
        if num2 == '0':
          print("You little trickster! Can't do that!")
        else: 
          print(num1/num2)

        #/
      elif i == ops[4] :
        num1 = int(_src[:inum])
        inum +=1
        num2 = int(_src[inum:])
        # < 
        if num1 < num2: 
          print("True")
        elif num1 > num2:
          print("False")
        else:
          print(str(num1)+" is equal to "+str(num2) )
      elif i == ops[5]:
        num1 = int(_src[:inum])
        inum +=1
        num2 = int(_src[inum:])
        #>
        if num1 > num2: 
          print("True")
        elif num1 < num2:
          print("False")
        else:
          print(str(num1)+" is equal to "+str(num2))
      elif i == ops[8]:
        
        num1 = int(_src[:inum])
        inum +=1
        if _src[inum] == ops[7]:
          inum += 1
          num2 = int(_src[inum:])
          if num1 != num2:
            print("True.")
          elif num1 == num2: 

            print("False. They are equal")  
                
        elif _src[inum] == ops[8]:
          inum += 1 
          num2 = int(_src[inum:])
          if num1 == num2:
            print("True")
          else: 
            print("False")
        else: 
          print(red+"Error! Unexpected: "+i+"\nMaybe you meant '!='?")
        # != 

      
    elif re.match("[a-z]", i) or re.match("[A-Z]", i):
      print("Heya, either you mistyped something, or you were trying to make a variable! Elipie is still working on variables! Will come out in the next version! ")
    

    inum += 1
