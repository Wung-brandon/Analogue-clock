from tkinter import *
import time
import math

#height and width of Analog clock window
HEIGHT = 400
WIDTH = 400

root = Tk()
root.title("Analog Clock")

#create clock canvas tkinter
canvas = Canvas(root, width=WIDTH,height=HEIGHT,bg='white')
canvas.pack()

def update_clock():
    canvas.delete("all")  #deletes all previous drawing from the canvas
    now = time.localtime() #fetches the current time from the computer system
    hour = now.tm_hour % 12
    minute = now.tm_min    #hour,minute and second are variable that extract the hour,minutes and seconds from the time structure variable now
    second = now.tm_sec   
    #draw clock face
    canvas.create_oval(2,2,WIDTH,HEIGHT,outline='black',width=2)
    
    #draw hours numbers
    #A for loop to draw hour numbers on the clock face canvas. the loop runs 12 times, one for each hour
    for numbers in range(12):  # number is the hour number
        angle = numbers * math.pi/6 - math.pi/2
        x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(angle)
        y = HEIGHT/2 + 0.7 * WIDTH/2 * math.sin(angle)
        if numbers == 0:
            canvas.create_text(x,y-10,text=str(numbers+12),font=("helvetica",12,'bold'))
        else:
            canvas.create_text(x,y,text=str(numbers),font=("helvetica",12,'bold'))
            
    #draw minute lines
    for numbers in range(60):
        angle = numbers * math.pi/30 - math.pi/2
        x1 = WIDTH/2 + 0.8 * WIDTH/2 * math.cos(angle)
        y1 = HEIGHT/2 + 0.8 * HEIGHT/2 * math.sin(angle) #to draw a line we need a starting point and an endpoint.This is the reason we are defining x1,y1,x2,y2 in code
        x2 = WIDTH/2 + 0.9 * WIDTH/2 * math.cos(angle)
        y2 = HEIGHT/2 + 0.9 * HEIGHT/2 * math.sin(angle)
        if numbers%5 == 0: #to draw minutes line in our clock canvas. We are making the minutes line a littlw bit bolder every 5 minutes using if numbers%5==0
            canvas.create_line(x1, y1, x2, y2,fill='black',width=3)
        else:
            canvas.create_line(x1, y1, x2, y2,fill='black',width=1)
            
    #draw hour hand
    hour_angle  = (hour + minute/60) * math.pi/30 - math.pi/2
    hour_x = WIDTH/2 + 0.5  * WIDTH/2 * math.cos(hour_angle)
    hour_y = WIDTH/2 + 0.5  * WIDTH/2 * math.sin(hour_angle)
    canvas.create_line(WIDTH/2,HEIGHT/2,hour_x,hour_y,fill='black',width=6)        
        
              
    #draw minute hand
    minute_angle  = (minute + second/60) * math.pi/30 - math.pi/2
    minute_x = WIDTH/2 + 0.7  * WIDTH/2 * math.cos(minute_angle)
    minute_y = WIDTH/2 + 0.7  * WIDTH/2 * math.sin(minute_angle)
    canvas.create_line(WIDTH/2,HEIGHT/2,minute_x,minute_y,fill='black',width=4)   
    
              
    #draw second hand
    second_angle  = second * math.pi/30 - math.pi/2
    second_x = WIDTH/2 + 0.6  * WIDTH/2 * math.cos(second_angle)
    second_y = WIDTH/2 + 0.6  * WIDTH/2 * math.sin(second_angle)
    canvas.create_line(WIDTH/2,HEIGHT/2,second_x,second_y,fill='red',width=2) 
    
    canvas.after(1000,update_clock)
     
#calling the function
update_clock()
root.mainloop()



#math.pi/6 term used because the are 12 hour numbers in total and we know the radians of a circle is 2*math.pi.So each number is spaced 2*math.pi/12=math.pi/6 radians
#apart. so in short math.pi/6 represents 1/12 of a circle or 30 degrees

#math.pi/2 represents 90degrees or 1/4 of a circle.The 12 o'clock position in the analog clock is at the top of the clock instead of the right.math.pi/2 is subtracted
#from angle to rotate the entire clock face 90degrees counterclockwise.this is to ensure that the hands are drawn starting from the 12 o'clock position,rather than
#the 3 o'clock(0 degrees) position

#line 29-30 Here WIDTH/2 and HEIGHT/2 erepresent the center of the analog clock face
#0.7*WIDTH/2 is used to reduce the radius of the clock face a little bit
#math.cos(angle) and math.sin(angle) gives the cosine and sine values of the angle at which the number needs to be placed

#line 31-34 This line ia used to finally draw the line markers in the clock canvas by creating text. We are starting from 12 o'clock, this is the reason for using if statement

 