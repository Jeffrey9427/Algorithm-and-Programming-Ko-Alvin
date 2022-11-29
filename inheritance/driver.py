from cylinder import *

def main():
    c = Cylinder(20.0, 'Yellow', 1.0)
    c.setHeight(12.0)
    print(f'Height: {c.getHeight()}')
    print(c.toString())
    print(f'Volume of the cylinder: {c.getVolume():.2f}')

if __name__ == '__main__':
    main()