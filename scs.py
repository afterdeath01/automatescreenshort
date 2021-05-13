import pathlib
import time
import pyscreeze
TGREEN =  '\033[31m' # Green Text
def takeshort():
    Take_Input = int(input("Enter the number of screenshort you want to take\n"))
    Take_Time = int(input("Enter the time gap\n"))
    i = 0
    for i in range(Take_Input ):
        Screenshort = pyscreeze.grab().save(fr'{pathlib.Path().absolute()}\screnshort{i}.png')
        print(f"screen short done {i}")
        time.sleep(Take_Time)
        i = i+1
        
        
if __name__ == "__main__":
    takeshort()
    print(TGREEN +"done ")
    