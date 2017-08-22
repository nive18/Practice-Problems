#Function to calculate the miles to inches
def miles_to_inches(miles):
    feet = miles * 5280
    return feet
a1 = miles_to_inches(10)
print a1
#############################################################
#Function to calculate hours and seconds and minutes
def total_seconds(hours, minutes,seconds):
    return hours*3600+minutes * 60+seconds
print total_seconds(1,20,30)
print total_seconds(7,21,37)
############################################################
#Functions to calculate rectangular perimeter
def rectangle_perimeter(width, height):
    area = 2 * width + 2 * height
    return area
def test(width, height):
    print  "width is " +str(width)+" Height is "+str(height)+ " area is "+str(rectangle_perimeter(width, height))
   
    
    
test(2,2)    
################################################################
#Function to define area of the triangle
def rectangle_area(width, height):
    return width*height
def test(width, height):
    print "width and height is "+str(rectangle_area(width,height))
test(2, 4) 
##############################################################
def circle_circumfrence(radius):
    return 2*3.14*radius
def test(radius):
    print str(circle_circumfrence(radius))
test(2)   
###########################################################
#area of circle
def circle_area(radius):
    return 3.14*radius*radius
def test(radius):
    print str(circle_area(radius))
test(10)   
###########################################################
#Function for distance formula
def distance(x0,y0,x1,y1):
    area = ((x0-x1)**2 + (y0-y1)**2)**0.5
    return area
def test(x0,y0,x1,y1):
    print  str(distance(x0,x1,y0,y1))

test(2, 2, 5, 6)  
#######################################################333
#Challenge 2
def triangle_area(x0,y0,x1,y1,x2,y2):
    a = ((x0-x1)**2 + (y0-y1)**2)**0.5
    b = ((x1-x2)**2 + (y1-y2)**2)**0.5
    c = ((x2-x0)**2 + (y2-y0)**2)**0.5
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area
def test(x0,y0,x1,y1,x2,y2):
    print str(triangle_area(x0,y0,x1,y1,x2,y2))
test(0, 0, 3, 4, 1, 1)    
#############################################################
#Challenge 3
def print_digits(numbers):
    ones = numbers % 10
    tens = numbers / 10
    a1 = str(ones) +" "+str(tens)

    return a1
def test(numbers):
    print str(print_digits(numbers))
test(45) 
##########################################################33

    