#sandrex cabrales simple math puzzle

import random #to randomize number

#variable name
#f1 = first row first column
#f3 = first row third column
#s1 = second row first column
#s2 = second row second column
#t2 = third row second column
#t3 = third row third column

f1numrow = random.randrange(0, 10)  # first number in first row random number with range from negative 9 to  positive 10
f3numrow = random.randrange(5,10) - f1numrow  # 3rd number random number from 5 to 10

s1numrow = random.randrange(0, 10)  # Same explanation
s2numrow = random.randrange(5,10) - s1numrow  # Same explanation

t2numrow = random.randrange(0, 10)  # Same explanation
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

        if(int(x) + f1numrow + f3numrow != 10): #logic operator to check if answer is greater than 10 for row 1
            ansf = f1numrow + f3numrow - 10 #logic operator to check if answer is right for row 1
            ansf2 = s1numrow + s2numrow - 10 #logic operator to check if answer is right for row 2
            ansf3 = t2numrow + t3numrow - 10 #logic operator to check if answer is right for row 3
            if(ansf != int(x)): #logic operator to check if answer is not correct to display the answer for row 1

                print('                                                      ' + str(f1numrow) + ' | ' + str(
                f3numrow) + ' | ' + str(x) + ' | = ' + str(abs(ansf)) + " - 1st row wrong " )
            if(ansf2 != int(y)):

                print(
                '                                                      ' + str(s1numrow) + ' | ' + str(y) + ' | ' + str(
                    s2numrow))

        elif(int(y) + s1numrow + s2numrow != 10): #logic operator to check if answer is greater than 10 for row 2
            ansf2 = s1numrow + s2numrow - 10

            print('                                                      ' + str(s1numrow) + ' | ' + str(y) + ' | ' + str(
                s2numrow))


print("------------------------------------------------ Input the answer per row -----------------------------------------------------------")
x = input("First Row Answer: ")
y = input("Second Row Answer: ")
z = input("Third Row Answer: ")


p1 = Puzzle(x,y,z)

p1.myfunc()

exit()