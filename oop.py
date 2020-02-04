class parent:
    def move(self):
        print("PARENT MOVEMENT")
class child:
    def move(self):
        print("CHILD MOVEMENT")
ch1=child()
ch1.move()

ch2=parent()
ch2.move()


# ch2=child().move()                #CHILDMOVEMENT
# print(ch2)                        #None
