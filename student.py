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
        self.SAFE_DIST = 350
        self.MIDPOINT = 1600  # what servo command (1000-2000) is straight forward for your bot?
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
                "h": ("Hold position", self.hold_position),
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
        """all dances are inputed here"""
        # check to see its safe
        if not self.safety_check():
            print("Not cool bro. Not doing a dance")
            return #close method
        else:
            print("It's safe let's boogie :P")
        for x in range(3):
            self.shuffle()
            self.dab()
            self.moonwalk()
            self.thecleary()

    def safe_to_dance(self):
        """Does a 360 distance check and returns true if safe"""
        for x in range(4):
            for ang in range(1000, 2001, 100):
                self.servo(ang)
                time.sleep(.1)
                if self.read_distance() < 250:
                    return False
            self.turn_to_deg(90)
        return True

    def shuffle(self):
        """makes the robot do the classic shuffle"""
        for x in range(3):
            self.turn_by_deg(270)
            self.servo(1000)
            time.sleep(.5)
            self.turn_by_deg(15)
            self.servo(2000)
            time.sleep(1)
            self.stop()
    
    def dab(self):
        """ makes the servo move in order to show an arm moving """
        for x in range(3):
            self.servo(1000)
            self.turn_by_deg(270)
            self.left()
            time.sleep(.5)
            self.stop()

    def moonwalk(self):
        """ the classic moonwalk forcing the robot to move backwords the entire time"""
        self.back()
        time.sleep(1)
        self.turn_by_deg(-30)
        self.back
        self.turn_by_deg(60)
        self.back()
        self.stop()

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 250):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """ Does a 360 scan and returns the number of obstacles it see"""
        pass

    def hold_position(self):
        started_at = self.get_heading()
        while True:
            time.sleep(.1)
            current_angle = self.get_heading()
            if abs(started_at - current_angle) > 20:
                self.turn_to_deg(started_at)

    def quick_check(self):
        # three quick checks
        for ang in range(self.MIDPOINT-150, self.MIDPOINT+151, 150):
            self.servo(ang)
            if self.read_distance() < self.SAFE_DIST:
                return False
        #if i get to the end, this means i didn't find anything dangerous
        return True
    def turn_to_exit(self):
        start = self.get_heading()
        self.turn_to_deg(self.EXIT_HEADING)
        if not self.quick_check():
            self.turn_to_deg(start)
            return False
        return True

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        corner_count = 3
        self.EXIT_HEADING = self.get_heading()
        
        while True:    
            self.servo(self.MIDPOINT)
            while self.quick_check():
                corner_count = 0
                self.fwd()
                time.sleep(.01)
            self.stop()
            self.scan()
            # turns out of cornoer if stuck
            corner_count += 1
            if corner_count == 3:
                self.turn_by_deg(90)
            
            #check on exit
            current = self.get_heading()
            self.turn_to_exit()
            if not self.quick_check():
                self.turn_to_deg(current)
            else: continue
            #traversal
            left_total = 0
            left_count = 0
            right_total = 0
            right_count = 0
            for ang, dist in self.scan_data.items():
                if ang < self.MIDPOINT: 
                    right_total += dist
                    right_count += 1
                else:
                    left_total += dist
                    left_count += 1
            left_avg = left_total / left_count
            right_avg = right_total / right_count
            if left_avg > right_avg:            
                self.turn_by_deg(-45)
            else:                
                self.turn_by_deg(45)





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


        