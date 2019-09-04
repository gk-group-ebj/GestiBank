class User:

    def __init__(self, mail, password):
        self.password = password
        self.mail = mail


count = 0
while True:
    userName = input("Hello! Welcome to FaceSnap! \n\nUsername: ")
    password = input("Password: ")
    count += 1
    if count == 3:
        #tells user bye
        print("You didn't give the good login. Bye bye.")
        #exit
        break
    else:
        if userName == 'elmo' and password == 'blue':
            #let them in
            print("Yes! you have successfully logged in.")
            break #they are in, exit loop
        else:
            #tell them it is wrong and have them retry, stay in loop
            print("Too bad! Try again.")
