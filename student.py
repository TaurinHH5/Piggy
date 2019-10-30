from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 80
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1500  # what servo command (1000-2000) is straight forward for your bot?
        self.load_defaults()


    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        

    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''

    def dance(self):
       #  print("I don't know how to dance. \nPlease give my programmer a zero.")
        #HIGHER-ORDER
        #Check to see if its safe 
         if not self.saftey_check: 
            print("Not cool.I ain't dancing")
            return #return closes ther method
        else:
            print("its safe to dance")

        for x in range(3):
            self.Birdie()
            self.moonwalk()
            self.twist()
            self.dab()

        def safe_to_dance_(self):
            '''does a 360 distnace check and returns true'''
            for x in range (4):
                for ang in range (1000,2001,100)
                    self.servo(ang):
                    time.sleep(.1)
                    if self.read_distance() < 250:
                        return false 
                self. turn_by_deg(90)
            return True

    for x in range (2)
        #self.Birdie()
        #self.moonwalk()
        #self.twist()
        #self.dab
'''
DANCE METHODS
'''


    def twist(self):
        # A classic move, done by the experts who slay the most
        while True: 
        self.MOTOR_LEFT(50)
        time.sleep(.8)
        self.MOTOR_RIGHT(50)

    def moonwalk(self): 
        #A tribute to Micheal Jackson and his love for children 
        self.back
        time.sleep(1)
        self.turn_by_deg(-30)
        self.back
        self.turn_by_deg(60)
        self.back()

    def dab(self):
        # Coming from an origin that should not be named, this move the ultimate party dance move
        self.servo(800)
        self. turn_by_deg(370)
        self.left
        self.sleep(1)
        self.stop
    def Birdie(self):
        #Schimizzi's favorite move when at the club, also has been seen preforming it on the ice
        self.MOTOR_RIGHT(15)
        time.sleep(1)
        while true:
        self.MOTOR_LEFT(15)
        self.MOTOR_RIGHT(15)
        self.servo(22)

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obsticles it sees""" 
        found_something = False 
        starting_position = self.get_heading()
        self.right(primary=60, counter= -60)
        while self.get_heading() != starting_position
            if self.read_distance( )< 250 and not found_something
                found_something = True
                count+= 1 
                print("\nTheres something in my face, i Cannot see\n"):
            elif self.read_distance() > 250 and found_something:
                found_something = False
        self.stop()
        print("I found this many things:%d" % count )
        return count



        print("Im tryan boolinin in this bih dont talk in that rap cap")




    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
       while self.read_distance() > 250:
           self.fwd()
           time.sleep(.02)
        self.stop()
    
###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
