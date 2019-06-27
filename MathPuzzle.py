#sandrex cabrales simple math puzzle

import random #to randomize number

#variable name
#f1 = first row first column
#f3 = first row third column
#s1 = second row first column
#s2 = second row second column
#t2 = third row second column
#t3 = third row third column

f1numrow = random.randrange(0, 9)  # first number in first row random number with range from negative 9 to  positive 10
f3numrow = random.randrange(5,10) - f1numrow  # 3rd number random number from 5 to 10

s1numrow = random.randrange(0, 9)  # Same explanation
s2numrow = random.randrange(5,10) - s1numrow  # Same explanation

t2numrow = random.randrange(0, 9)  # Same explanation
t3numrow = random.randrange(5,10) - t2numrow  # Same explanation

class Puzzle:

    print('')
    print('------------------------------------------- WELCOME TO SANDREX MATH PUZZLE ---------------------------------------------------------')


    print('                                       #######################################')
    print('                                                      ' +str(f1numrow) + ' | ' + str(f3numrow) + ' | ?')
    print('                                                      ' +str(s1numrow) + ' | ' + '? | ' + str(s2numrow))
    print('                                                      ' + '? | ' +str(t2numrow) + ' | ' + str(t3numrow))
    print('                                       #######################################')
    print('')
    def __init__(self, f2numrow, s3numrow, t1numrow ):
        self.f2numrow = f2numrow,
        self.s3numrow = s3numrow,
        self.t1numrow = t1numrow,



    def myfunc(self):
      if(x.isalpha() and x.isalnum() or y.isalpha() and y.isalnum() or z.isalpha() and z.isalnum()): #i tried, this is the problem when i input alpha and number it got error! sorry it is beyond my capabilities
          print('')
          print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Please Input a Valid Number!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      else:
        if(int(x) + f1numrow + f3numrow != 10): #logic operator to check if answer is greater than 10 for row 1
            ansf = f1numrow + f3numrow - 10 #logic operator to check if answer is right for row 1
            ansf2 = s1numrow + s2numrow - 10 #logic operator to check if answer is right for row 2
            ansf3 = t2numrow + t3numrow - 10 #logic operator to check if answer is right for row 3

            if(abs(ansf)) != int(x): #logic operator to check if answer is not correct to display the answer for row 1

                print('                                                      ' + str(f1numrow) + ' | ' + str(
                f3numrow) + ' | ' + str(x) + ' | = ' + str(abs(ansf)) + " - 1st row wrong " )
            else:
                print('                                                      ' + str(f1numrow) + ' | ' + str(
                    f3numrow) + ' | ' + str(x) + ' | = ' + str(abs(ansf)) + " - 1st row correct  ")
            if(abs(ansf2)) != int(y):

                print(
                '                                                      ' + str(s1numrow) + ' | ' + str(y) + ' | ' + str(
                    s2numrow) + ' | = ' + str(abs(ansf2)) + ' - 2nd row wrong  ')
            else:
                print(
                    '                                                      ' + str(s1numrow) + ' | ' + str(
                        y) + ' | ' + str(
                        s2numrow) + ' | = ' + str(abs(ansf2)) + ' - 2nd row correct  ')
            if(abs(ansf3)) != int(z):
                 print('                                                      ' + str(z) + ' | ' + str(t2numrow) + ' | ' + str(
                     t3numrow) + ' | = ' + str(abs(ansf3)) + ' - 3rd row wrong ')
            else:
                print('                                                      ' + str(z) + ' | ' + str(
                    t2numrow) + ' | ' + str(
                    t3numrow) + ' | = ' + str(abs(ansf3)) + ' - 3rd row correct ')




        elif(int(y) + s1numrow + s2numrow != 10): #logic operator to check if answer is greater than 10 for row 2
            ansf = f1numrow + f3numrow - 10  # logic operator to check if answer is right for row 1
            ansf2 = s1numrow + s2numrow - 10  # logic operator to check if answer is right for row 2
            ansf3 = t2numrow + t3numrow - 10  # logic operator to check if answer is right for row 3

            if (abs(ansf)) != int(
                    x):  # logic operator to check if answer is not correct to display the answer for row 1

                print('                                                      ' + str(f1numrow) + ' | ' + str(
                    f3numrow) + ' | ' + str(x) + ' | = ' + str(abs(ansf)) + " - 1st row wrong ")
            else:
                print('                                                      ' + str(f1numrow) + ' | ' + str(
                    f3numrow) + ' | ' + str(x) + ' | = ' + str(abs(ansf)) + " - 1st row correct  ")
            if (abs(ansf2)) != int(y):# logic operator to check if answer is not correct to display the answer for row 2

                print(
                    '                                                      ' + str(s1numrow) + ' | ' + str(
                        y) + ' | ' + str(
                        s2numrow) + ' | = ' + str(abs(ansf2)) + ' - 2nd row wrong  ')
            else:
                print(
                    '                                                      ' + str(s1numrow) + ' | ' + str(
                        y) + ' | ' + str(
                        s2numrow) + ' | = ' + str(abs(ansf2)) + ' - 2nd row correct  ')
            if (abs(ansf3)) != int(z):# logic operator to check if answer is not correct to display the answer for row 3
                print('                                                      ' + str(z) + ' | ' + str(
                    t2numrow) + ' | ' + str(
                    t3numrow) + ' | = ' + str(abs(ansf3)) + ' - 3rd row wrong ')
            else:
                print('                                                      ' + str(z) + ' | ' + str(
                    t2numrow) + ' | ' + str(
                    t3numrow) + ' | = ' + str(abs(ansf3)) + ' - 3rd row correct ')
        elif(int(z) + t2numrow + t3numrow != 10):
            ansf = f1numrow + f3numrow - 10  # logic operator to check if answer is right for row 1
            ansf2 = s1numrow + s2numrow - 10  # logic operator to check if answer is right for row 2
            ansf3 = t2numrow + t3numrow - 10  # logic operator to check if answer is right for row 3

            if (abs(ansf)) != int(
                    x):  # logic operator to check if answer is not correct to display the answer for row 1

                print('                                                      ' + str(f1numrow) + ' | ' + str(
                    f3numrow) + ' | ' + str(x) + ' | = ' + str(abs(ansf)) + " - 1st row wrong ")
            else:
                print('                                                      ' + str(f1numrow) + ' | ' + str(
                    f3numrow) + ' | ' + str(x) + ' | = ' + str(abs(ansf)) + " - 1st row correct  ")
            if (abs(ansf2)) != int(y):# logic operator to check if answer is not correct to display the answer for row 2

                print(
                    '                                                      ' + str(s1numrow) + ' | ' + str(
                        y) + ' | ' + str(
                        s2numrow) + ' | = ' + str(abs(ansf2)) + ' - 2nd row wrong  ')
            else:
                print(
                    '                                                      ' + str(s1numrow) + ' | ' + str(
                        y) + ' | ' + str(
                        s2numrow) + ' | = ' + str(abs(ansf2)) + ' - 2nd row correct  ')
            if (abs(ansf3)) != int(z):# logic operator to check if answer is not correct to display the answer for row 3
                print('                                                      ' + str(z) + ' | ' + str(
                    t2numrow) + ' | ' + str(
                    t3numrow) + ' | = ' + str(abs(ansf3)) + ' - 3rd row wrong ')
            else:
                print('                                                      ' + str(z) + ' | ' + str(
                    t2numrow) + ' | ' + str(
                    t3numrow) + ' | = ' + str(abs(ansf3)) + ' - 3rd row correct ')
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Wow your answer is all correct !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("                        #########################################################################################")
            print('                                                      ' + str(f1numrow) + ' | ' + str(
                f3numrow) + ' | ' + str(x) + ' | = ' + str(x) + " - 1st row correct  ")
            print(
                '                                                      ' + str(s1numrow) + ' | ' + str(
                    y) + ' | ' + str(
                    s2numrow) + ' | = ' + str(y) + ' - 2nd row correct  ')
            print('                                                      ' + str(z) + ' | ' + str(
                t2numrow) + ' | ' + str(
                t3numrow) + ' | = ' + str(z) + ' - 3rd row correct ')
            print("                         #########################################################################################")






print("------------------------------------------------ Input the answer per row -----------------------------------------------------------")
x = input("First Row Answer: ")
y = input("Second Row Answer: ")
z = input("Third Row Answer: ")


p1 = Puzzle(x,y,z)

p1.myfunc()

