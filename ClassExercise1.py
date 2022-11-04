# implement a method called get_json_str(p) that receives a point p as
# input and returns a json string that describes the object as output
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def setX(self,x):
        self.__x = x

    def setY(self,y):
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

a = Point(1,2)

def get_json_str(x):
    return {"__class__": "Point", "x": x.getX(), "y": x.getY()}

z = get_json_str(a)
print(z)      

# implement a function called read_json_str(s) that receives a string
# s as input and returns a point object as output.

def read_json_str(s):
    b = Point(int(s),0)
    return get_json_str(b)

z = read_json_str("5")
print(z)