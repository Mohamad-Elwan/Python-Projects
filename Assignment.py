print("Welcome to Shiny Painting Company for indoor painting\n")

room = int(input("How many rooms do you want to paint?\n"))
print("Thank you!\n")
rooms = []
tic = 0
while room > tic:
    tic += 1
    rooms.append(tic)


def computeRectangleWallsArea():
    length = int(input("Enter the length of the room in feet\n"))
    width = int(input("Enter the width of the room in feet\n"))
    height = int(input("Enter the height of the room in feet\n"))
    a1 = computeRectangleArea(length, height) * 2
    a2 = computeRectangleArea(width, height) * 2
    return a1 + a2


def computeRectangleArea(x, y):
    return x * y


def computeSquareWallsArea():
    length = int(input("Enter the length of one side of the room\n"))
    return computeSquareArea(length)


def computeSquareArea(x):
    return (x ** 2) * 4


def computeWindowsDoorsArea():
    num = int(input("How many windows and doors does the room contain?\n"))
    door = 0
    total = 0
    while num > door:
        door += 1
        length = int(input("Enter window/door length for window/door " + str(door) + " in feet\n"))
        width = int(input("Enter window/door width for window/door " + str(door) + " in feet\n"))
        total += computeRectangleArea(length, width)
    return total


def computeCustomWallsArea():
    num = int(input("How many walls are there in the room\n"))
    wall = 0
    total = 0
    while num > wall:
        wall += 1
        height = int(input("Enter height of wall " + str(wall) + " in feet\n"))
        length = int(input("Enter length of wall " + str(wall) + " in feet\n"))
        total += computeRectangleArea(length, height)
    return total


def computeGallons(a):
    gal = a / 350
    return gal


def computePaintPrice(g):
    price = g * 42
    return price


def computeRoomArea(x):
    x = room
    final_area = 0
    final_gal = 0
    final_cost = 0
    for r in rooms:

        shape = int(input("Select the shape of the room:\n 1 - Rectangular\n 2 - Square\n 3 - Custom (more or less than"
                          "four walls, all square or rectangles\n"))
        if shape == 1:
            area_of_room = computeRectangleWallsArea()
            area_of_doors = computeWindowsDoorsArea()
            total_area = area_of_room - area_of_doors
            final_area += total_area
            gal = computeGallons(total_area)
            final_gal += gal
            cost = computePaintPrice(gal)
            final_cost += cost
            print(f"For Room:{r}, the area to be painted is {total_area:.1f} square ft and will require {gal:.2f} "
                  f"gallons to paint. This\nwill cost the customer ${cost:.2f}")

        if shape == 2:
            area_of_room = computeSquareWallsArea()
            area_of_doors = computeWindowsDoorsArea()
            total_area = area_of_room - area_of_doors
            final_area += total_area
            gal = computeGallons(total_area)
            final_gal += gal
            cost = computePaintPrice(gal)
            final_cost += cost
            print(f"For Room:{r}, the area to be painted is {total_area:.1f} square ft and will require {gal:.2f} "
                  f"gallons to paint. This\nwill cost the customer ${cost:.2f}")
        if shape == 3:
            area_of_room = computeCustomWallsArea()
            area_of_doors = computeWindowsDoorsArea()
            total_area = area_of_room - area_of_doors
            final_area += total_area
            gal = computeGallons(total_area)
            final_gal += gal
            cost = computePaintPrice(gal)
            final_cost += cost
            print(f"For Room:{r}, the area to be painted is {total_area:.1f} square ft and will require {gal:.2f} "
                  f"gallons to paint. This\nwill cost the customer ${cost:.2f}\n")
    print(f"Area to be painted is {final_area:.2f} square ft and will require {final_gal:.2f} "
          f"gallons to paint. This\nwill cost the customer ${final_cost:.2f}")


computeRoomArea(room)
