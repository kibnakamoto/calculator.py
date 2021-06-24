import math

def sa_of_rrp(le,wi,he):
    surface_area_of_right_rectangular_pyramid = le*wi + le*math.sqrt((wi/2)**2 + he**2) +  wi*math.sqrt((le/2)**2 + he**2)
    print(f"full equation: {le}*{wi}+{le}*{math.sqrt((wi/2)**2+he**2)}+{wi}*{math.sqrt((le/2)**2+he**2)}")
    print(f"equation: {le*wi}+{le*math.sqrt((wi/2)**2+he**2)}+{wi*math.sqrt((le/2)**2+he**2)}")
    print(f"equation: {le*wi+le*math.sqrt((wi/2)**2+he**2)}+{wi*math.sqrt((le/2)**2+he**2)}")
    print("answer:",surface_area_of_right_rectangular_pyramid)

def area_of_triangle(x, y):
    area = x * y / 2
    print(f"equation: {x} * {y} / 2 ")
    print(f"equation: {x * y} / 2 ")
    print(f"area of triangle: {area}")

def right_cylinder_area(radius,height):
    area_of_right_cylinder = 2 * math.pi * height + 2 * math.pi * radius * radius
    print(f"full equation: 2 * {math.pi} * {height} + 2 * {math.pi} * {radius**2}")
    print(f"equation: {2 * math.pi} * {height} + {2 * math.pi} * {radius**2}")
    print(f"equation: {2 * math.pi * height} + 2 * {math.pi * radius**2}")
    print(f"answer: {area_of_right_cylinder}")

def area_of_right_square_pyramid(nel,neh):
    a_of_rsp = nel*nel + 2*nel * math.sqrt(nel**2 / 4 + neh*neh)
    print(f"equation: {nel}*{nel} + {2}*{nel} * {math.sqrt(nel**2 / 4 + neh*neh)}")
    print(f"equation:{nel*nel} + {2*nel} * {math.sqrt(nel**2 / 4 + neh*neh)}")
    print(f"equation:{nel*nel} + {2*nel * math.sqrt(nel**2 / 4 + neh*neh)}")
    print(f"Area of right square pyramid: {a_of_rsp}")

def sa_of_rpp(edge, heig):
    tanp = math.tan(math.pi*3/10)
    surface_area_of_right_pentagonal_pyramid = 1.25 * tanp * edge*edge + 2.5*edge * math.sqrt(heig**2 + (edge*tanp/2)**2)
    print(f"{1.25}*{tanp}*{edge}*{edge}+{2.5}*{edge}*{math.sqrt(heig**2+(edge*tanp/2)**2)}")
    print(f"{1.25*tanp}*{edge*edge}+{2.5*edge}*{math.sqrt(heig**2+(edge*tanp/2)**2)}")
    print(f"{1.25*tanp*edge*edge}+{2.5*edge*math.sqrt(heig**2+(edge*tanp/2)**2)}")
    print(f"answer: {surface_area_of_right_pentagonal_pyramid}")

def v_of_s(r):
    volume_of_sphere = (4/3) * math.pi * r**3
    print(f"equation: {4}/{3}*{math.pi}*{r}*{r}*{r}")
    print(f"equation: {(4/3)}*{math.pi}*{r**3}")
    print(f"equation: {(4/3)*math.pi}*{r**3}")
    print(f"answer: ",volume_of_sphere)

def v_of_tp(aside,bside, cside, heiight):
    volume_of_triangular_prism = heiight / 4* math.sqrt(-aside**4 + 2*(aside*bside)**2 + 2*(aside*cside)**2 - bside**4 + 2*(cside*bside)**2 - cside**4)
    print(f"equation: {heiight}/{4}*{math.sqrt}({-aside}**4+2*({aside}*{bside})**2+2*({aside}*{cside})**2-{bside}**4+2*({cside}*{bside})**2-{cside}**4)")
    print(f"{heiight/4}*{math.sqrt}({-aside**4}+2*({aside*bside})**2+2*({aside*cside})**2-{bside**4}+2*({cside*bside})**2-{cside**4})")
    print(f"{heiight/4}*{math.sqrt}({-aside**4}+{2*(aside*bside)**2}+{2*(aside*cside)**2}-{bside**4}+{2*(cside*bside)**2}-{cside**4})")
    print(f"{heiight/4}*{math.sqrt(-aside**4+2*(aside*bside)**2+2*(aside*cside)**2-bside**4+2*(cside*bside)**2-cside**4)}")
    print(f"answer: {volume_of_triangular_prism}")
#fix error that doesn't allow big numbers in equations in function: v_of_tp

def a_of_t(abase,bbase,thgieh):
    area_of_trapezoid = ((abase+bbase)/2) * thgieh
    print(f"equation: ({abase}+{bbase})/2*{thgieh}")
    print(f"          ({abase+bbase})/{2*thgieh}")
    print(f"answer: {area_of_trapezoid}")

#calculator
print("list of possible equations: ")
print("Type saorrp or saofrrp for surface area(SA) of right rectangular pyramid")
print("Type aoc or aofc for area(A) of a right angle triangle")
print("Type arc or aofac for area(A) of of right cylinder")
print("Type aofrsp or arsp or area(A) of right square pyramid for area of right square pyramid")
print("Type saofrpp or saorpp for surface area(SA) of right pentagonal pyramid")
print("Type vs or vofs for volume(V) of sphere")
print("Type votp or voftp for volume(V) of triangular prism")
print("Type aot of aoft for area(A) of trapezoid")
choice = input("input: ") #change to print and type input for inputting options only(without printing)
if choice == "saorrp" or choice == "saofrrp" or choice == "surface area of right rectangular pyramid":
    print("calculator for surface area of right rectangular pyramid")
    terminate = False
    while not terminate:
        le = input("length of right rectangular pyramid: ")
        wi = input(" width of right rectangular pyramid: ")
        he = input("height of right rectangular pyramid: ")
        if (le=='quit' or le=='Quit') or (wi=='quit' or wi=='Quit') or (he=='quit' or he=='Quit'):
            terminate = True
        else:
            le = str(le)
            wi = str(wi)
            he = str(he)
            sa_of_rrp(le,wi,he)
elif choice == "aoc" or choice == "aofc" or choice == "area of a right angle triangle": #area of a right angle triangle
    print("calculator for Area of a triangle")
    terminate = False
    while not terminate:
        x = input("input length: ")
        y = input("input height: ")
        if (x == 'quit' or x == 'Quit') or (y == 'quit' or y == 'Quit'):
            terminate = True
        else:
            x = int(x)
            y = int(y)
            area_of_triangle(x, y)
elif choice == "arc" or choice == "aofac" or choice == "area of a right cylinder": #area of a right cylinder
    print("area of right cylinder")
    terminate = False
    while not terminate:
        radius = input("radius: ")
        height = input("height: ")
        if (radius == 'quit' or radius == 'Quit') or (height == 'quit' or height == 'Quit'):
            terminate = True
        else:
            radius = int(radius)
            height = int(height)
            right_cylinder_area(radius,height)
elif choice == "aofrsp" or choice == "arsp" or choice == "area of right square pyramid":
    print("area of a right square pyramid")
    terminate = False
    while not terminate:
        nel = input("length: ")
        neh = input("height: ")
        if (nel == 'quit' or nel == 'Quit') or (neh == 'quit' or neh == 'quit'):
            terminate = True
        else:
            nel = int(nel)
            neh = int(neh)
            area_of_right_square_pyramid(nel,neh)
elif choice == "saofrpp" or choice == "saorpp" or choice == "surface area of right pentagonal pyramid":
    print("surface area of right pentagonal pyramid")
    terminate = False
    while not terminate:
        edge = input("Base edge: ")
        heig = input("height: ")
        if (edge == 'quit' or edge == 'Quit') or (heig == 'quit' or heig == 'Quit'):
            terminate = True
        else:
            edge = int(edge)
            heig = int(heig)
            sa_of_rpp(edge, heig)
elif choice == "vs" or choice == "vofs" or choice == "volume_of_sphere":
    print("volume_of_sphere")
    terminate = False
    while not terminate:
        r = input("radius: ")
        if r == 'quit' or r == 'Quit':
            terminate = True
        else:
            r = int(r)
            v_of_s(r)
elif choice == "votp" or choice == "voftp" or choice == "volume of triangular prism":
    print("volume of triangular prism")
    terminate = False
    while not terminate:
        aside = int(input("Base side base: "))
        bside = int(input("Base side hypotenuse: "))
        cside = int(input("Base side leg: "))
        heiight = int(input("height: "))
        if (aside == 'quit' or aside == 'Quit') or (bside == 'quit' or bside == 'Quit') or (cside == 'quit' or cside == 'Quit') or (heiight == 'quit' or heiight == 'Quit'):
            terminate = True
        else:
            aside = int(aside)
            bside = int(bside)
            cside = int(cside)
            heiight = int(heiight)
            v_of_tp(aside,bside,cside, heiight)
elif choice == "aoft" or choice == "aot" or choice == "area of trapezoid":
    print("area of trapezoid")
    terminate = False
    while not terminate:
        abase = input("short side of trapezoid(top base): ")
        bbase = input("long side of trapezoid(bottom base): ")
        thgieh = input("height: ")
        if (abase == 'quit' or abase == 'Quit') or (bbase == 'quit' or bbase == 'Quit') or (thgieh == 'quit' or thgieh == 'Quit'):
            terminate = True
        else:
            abase = int(abase)
            bbase = int(bbase)
            thgieh = int(thgieh)
            a_of_t(abase,bbase,thgieh)
else:
    print("undifined input")
    print("Try again!")
