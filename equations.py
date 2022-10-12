import pygame, tkinter, sys, math, random
from pygame.locals import *

pygame.init()

screen_width = screen_height = 1000
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Graphing Calculator")

class MainScreen:

    def __init__(self):
        self.bg = (255, 255, 255)
        self.y_axis = Rect(screen_width // 2, 0, 1, screen_height)
        self.x_axis = Rect(0, screen_height // 2, screen_width, 1)

    def reset(self):
        window.fill(self.bg)
        pygame.draw.rect(window, (0, 0, 0), self.y_axis)
        pygame.draw.rect(window, (0, 0, 0), self.x_axis)
        x1 = x2 = x3 = x4 = screen_width // 2
        y1 = y2 = y3 = y4 = screen_height // 2
        while x1 != screen_width:
            pygame.draw.line(window, (0, 0, 0), (x1, y1), (x1, y1+2))
            pygame.draw.line(window, (0, 0, 0), (x2, y2), (x2-2, y2))
            pygame.draw.line(window, (0, 0, 0), (x3, y3), (x3, y3+2))
            pygame.draw.line(window, (0, 0, 0), (x4, y4), (x4-2, y4))
            x1 += 25
            y2 -= 25
            x3 -= 25
            y4 += 25

class OptionScreen:

    def __init__(self):
        self.options = tkinter.Tk()
        self.options.title("Options")
        self.created_lines = []

    def create(self):
        self.frm_selection = tkinter.Frame(master=self.options, relief=tkinter.SUNKEN, borderwidth=1)
        self.frm_selection.pack()
        self.lbl_selection = tkinter.Label(master=self.frm_selection, text="Choose what to plot.")
        self.lbl_selection.grid(row=0, column=1)
        self.but_select_linear = tkinter.Button(master=self.frm_selection, text="Linear")
        self.but_select_linear.bind("<Button-1>", self.createLinear)
        self.but_select_linear.grid(row=1, column=0)
        self.but_select_quadratic = tkinter.Button(master=self.frm_selection, text="Quadratic")
        self.but_select_quadratic.bind("<Button-1>", self.createQuadratic)
        self.but_select_quadratic.grid(row=1, column=1)
        self.but_select_cubic = tkinter.Button(master=self.frm_selection, text="Cubic")
        self.but_select_cubic.bind("<Button-1>", self.createCubic)
        self.but_select_cubic.grid(row=1, column=2)
        self.but_select_polynomial = tkinter.Button(master=self.frm_selection, text="Polynomial")
        self.but_select_polynomial.bind("<Button-1>", self.setupPolynomial)
        self.but_select_polynomial.grid(row=2, column=1)

    def createLinear(self, null):
        self.linear = tkinter.Tk()
        self.linear.title("Linear")
        self.frm_main_linear = tkinter.Frame(master=self.linear, relief=tkinter.SUNKEN, borderwidth=1)
        self.frm_main_linear.pack()
        self.lbl_linear_equation = tkinter.Label(master=self.frm_main_linear, text="y=")
        self.ent_linear_equation = tkinter.Entry(master=self.frm_main_linear, width=50)
        self.lbl_linear_equation.grid(row=0, column=0, sticky="e")
        self.ent_linear_equation.grid(row=0, column=1)
        self.but_linear_create = tkinter.Button(master=self.frm_main_linear, text="Create!")
        self.but_linear_create.bind("<Button-1>", self.drawLinear)
        self.but_linear_create.grid(row=1, column=1)

    def drawLinear(self, null):
        line = self.ent_linear_equation.get()
        if line == "x":
            line = "1x+0"
        elif line =="-x":
            line = "-1x+0"
        line = line.replace(" ", "")
        if 'x' in line:
            line_segments = line.split('x')
            if not line_segments[1]:
                line_segments[1] = 0
            line_segments[1] = float(line_segments[1])
            if line_segments[0] == "":
                line_segments[0] = 1
            elif line_segments[0] == "-":
                line_segments[0] = -1
            line_segments[0] = float(line_segments[0])
            
        else:
            try:
                line_segments = [0, float(line)]
            except:
                line_segments = [0, 0]
        y_intercept = line_segments[1]
        x, y = 0, -y_intercept
        while x != 20:
            x += 1
            y -= line_segments[0]
        right_coord = (round(500 + (x*25)), round(500 + (y*25)))
        x, y = 0,  -y_intercept
        while x!= -20:
            x -= 1
            y += line_segments[0]
        left_coord = (round(500 + (x*25)), round(500 + (y*25)))
        centre_coord = (500, round(500 - (y_intercept*25)))
        end_line = ["Linear", left_coord, centre_coord, right_coord]
        self.created_lines.append(end_line)
        return

    def createQuadratic(self, null):
        self.quadratic = tkinter.Tk()
        self.quadratic.title("Quadratic")
        self.frm_main_quadratic = tkinter.Frame(master=self.quadratic, relief=tkinter.SUNKEN, borderwidth=1)
        self.frm_main_quadratic.pack()
        self.lbl_quadratic_equation_1 = tkinter.Label(master=self.frm_main_quadratic, text="y=")
        self.lbl_quadratic_equation_1.grid(row=0, column=0, sticky="e")
        self.ent_quadratic_equation_1 = tkinter.Entry(master=self.frm_main_quadratic, width=10)
        self.ent_quadratic_equation_1.grid(row=0, column=1)
        self.lbl_quadratic_equation_2 = tkinter.Label(master=self.frm_main_quadratic, text="x^2 + ")
        self.lbl_quadratic_equation_2.grid(row=0, column=2)
        self.ent_quadratic_equation_2 = tkinter.Entry(master=self.frm_main_quadratic, width=10)
        self.ent_quadratic_equation_2.grid(row=0, column=3)
        self.lbl_quadratic_equation_3 = tkinter.Label(master=self.frm_main_quadratic, text="x + ")
        self.lbl_quadratic_equation_3.grid(row=0, column=4)
        self.ent_quadratic_equation_3 = tkinter.Entry(master=self.frm_main_quadratic, width=10)
        self.ent_quadratic_equation_3.grid(row=0, column=5)
        self.but_quadratic_create = tkinter.Button(master=self.frm_main_quadratic, text="Create!")
        self.but_quadratic_create.bind("<Button-1>", self.drawQuadratic)
        self.but_quadratic_create.grid(row=1, column=3)

    def drawQuadratic(self, null):
        line = [self.ent_quadratic_equation_1.get(), self.ent_quadratic_equation_2.get(), self.ent_quadratic_equation_3.get()]
        for i in range(len(line)):
            if line[i] == "":
                line[i] = 1
            else:
                line[i] = float(line[i])
        full_equation = []
        x = -20
        while x != 20:
            y = round((line[0] * (x**2)) + (line[1] * x) + line[2], 1)
            full_equation.append((500 + (x*25), 500 - (y*25)))
            x += 0.25
        end_line = ["Quadratic", full_equation]
        self.created_lines.append(end_line)
        return

    def createCubic(self, null):
        self.cubic = tkinter.Tk()
        self.cubic.title("Cubic")
        self.frm_main_cubic = tkinter.Frame(master=self.cubic, relief=tkinter.SUNKEN, borderwidth=1)
        self.frm_main_cubic.pack()
        self.lbl_cubic_equation_1 = tkinter.Label(master=self.frm_main_cubic, text="y=")
        self.lbl_cubic_equation_2 = tkinter.Label(master=self.frm_main_cubic, text="x^3 + ")
        self.lbl_cubic_equation_3 = tkinter.Label(master=self.frm_main_cubic, text="x^2 + ")
        self.lbl_cubic_equation_4 = tkinter.Label(master=self.frm_main_cubic, text="x + ")
        self.labels = [self.lbl_cubic_equation_1, self.lbl_cubic_equation_2, self.lbl_cubic_equation_3, self.lbl_cubic_equation_4]
        for i in range(len(self.labels)):
            self.labels[i].grid(row=0, column=i*2)
        self.cubic_entries = []
        for i in range(4):
            self.cubic_entries.append(tkinter.Entry(master=self.frm_main_cubic, width=10))
        for i in range(len(self.cubic_entries)):
            self.cubic_entries[i].grid(row=0, column=(i*2 + 1))
        self.but_cubic_create = tkinter.Button(master=self.frm_main_cubic, text="Create!")
        self.but_cubic_create.bind("<Button-1>", self.drawCubic)
        self.but_cubic_create.grid(row=1, column=4)

    def drawCubic(self, null):
        line = []
        for i in self.cubic_entries:
            line.append(i.get())
        for i in range(len(line)):
            if line[i] == "":
                line[i] = 1
            else:
                line[i] = float(line[i])
        full_equation = []
        x = -20
        while x != 20:
            y = round((line[0] * (x**3)) + (line[1] * (x**2)) + (line[2] * x) + line[3], 1)
            full_equation.append((500 + (x*25), 500 - (y*25)))
            x += 0.25
        end_line = ["Cubic", full_equation]
        self.created_lines.append(end_line)
        return

    def setupPolynomial(self, null):
        self.polynomial = tkinter.Tk()
        self.frm_poly = tkinter.Frame(master=self.polynomial, relief=tkinter.SUNKEN, borderwidth=1)
        self.frm_poly.pack()
        self.lbl_poly_setup = tkinter.Label(master=self.frm_poly, text="Highest power of x:")
        self.lbl_poly_setup.grid(row=0, column=0)
        self.ent_poly_setup = tkinter.Entry(master=self.frm_poly, width=5)
        self.ent_poly_setup.grid(row=0, column=1)
        self.but_poly_setup = tkinter.Button(master=self.frm_poly, text="Setup")
        self.but_poly_setup.bind("<Button-1>", self.resetPolynomial)
        self.but_poly_setup.grid(row=1, column=0, sticky="w")
    
    def resetPolynomial(self, null):
        try:
            for i in self.poly_labels:
                i.destroy()
            for i in self.poly_entries:
                i.destroy()
        except:
            pass
        self.createPolynomial(None)

    def createPolynomial(self, null):
        self.poly_size = int(self.ent_poly_setup.get())
        self.lbl_poly_start = tkinter.Label(master=self.frm_poly, text="y=")
        self.lbl_poly_start.grid(row=2, column=0, sticky="e")
        self.poly_labels = []
        for i in range(self.poly_size):
            if (i+1) == 1:
                self.poly_labels.append(tkinter.Label(master=self.frm_poly, text="x + "))
            else:
                self.poly_labels.append(tkinter.Label(master=self.frm_poly, text=("x^" + str(i+1) + " + ")))
        self.poly_entries = []
        for i in range(self.poly_size+1):
            self.poly_entries.append(tkinter.Entry(master=self.frm_poly, width=10))
        for i in range(self.poly_size):
            self.poly_labels[-(i+1)].grid(row=2, column=((i*2)+2))
        for i in range(len(self.poly_entries)):
            self.poly_entries[i].grid(row=2, column=((i*2)+1))
        self.but_create_poly = tkinter.Button(master=self.frm_poly, text="Create!")
        self.but_create_poly.bind("<Button-1>", self.drawPolynomial)
        self.but_create_poly.grid(row=3, column=0, sticky="e")

    def drawPolynomial(self, null):
        line = []
        for i in self.poly_entries:
            line.append(i.get())
        for i in range(len(line)):
            if line[i] == "":
                line[i] = 1
            else:
                line[i] = float(line[i])
        full_equation = []
        x = -20
        while x != 20:
            y = 0
            for i in range(len(line)-1):
                y += line[i] * (x ** (self.poly_size - i))
            y += line[-1]
            y = round(y, 1)
            full_equation.append((500 + (x*25), 500 - (y*25)))
            x += 0.25
        end_line = ["Polynomial", full_equation]
        self.created_lines.append(end_line)
        return


    def setupReciprocal(self, null):
        self.reciprocal = tkinter.Tk()
        self.frm_reci_main = tkinter.Frame(master=self.reciprocal, relief=tkinter.SUNKEN, borderwidth=1)
        self.frm_reci_main.pack()
        self.lbl_reci_setup = tkinter.Label(master=self.frm_reci_main, text="Highest power of x:")
        self.lbl_reci_setup.grid(row=0, column=0)
        self.ent_reci_setup = tkinter.Entry(master=self.frm_reci_main, width=5)
        self.ent_reci_setup.grid(row=0, column=1)
        self.but_reci_setup = tkinter.Button(master=self.frm_reci_main, text="Setup")
        self.but_reci_setup.bind("<Button-1>", self.createReciprocal)
        self.but_reci_setup.grid(row=1, column=0)
    
    def resetReciprocal(self, null):
        try:
            for i in reci_labels:
                i.destroy()
            for i in reci_entries:
                i.destroy()
        except:
            pass
        self.createReciprocal(None)

    def createReciprocal(self, null):
        self.reci_size = int(self.ent_poly_setup.get())
        self.lbl_reci_start = tkinter.Label(master=self.frm_reci_main, text="y=")
        self.lbl_reci_start.grid(row=2, column=0, sticky="e")
        self.lbl_reci_second = tkinter.Label(master=self.frm_reci_main, text= " / (")
        self.lbl_reci_second.grid(row=2, column=2)
        self.lbl_reci_final = tkinter.Label(master=self.frm_reci_main, text=")")
        self.reci_labels = []
        for i in range(self.reci_size):
            if (i+1) == 1:
                self.reci_labels.append(tkinter.Label(master=self.frm_reci_main, text="x + "))
            else:
                self.reci_labels.append(tkinter.Label(master=self.frm_reci_main, text="x^" + str(i+1) + " + "))
        self.reci_entries = []
        for i in range(self.reci_size + 2):
            self.reci_entries.append(tkinter.Entry(master=self.frm_reci_main, width=10))
        for i in range(len(self.reci_entries)):
            self.reci_entries[i].grid(row=2, column=((i*2)+1))
        for i in range(len(self.reci_labels)):
            pass
            #CONTINUE HERE# 





screen = MainScreen()
options = OptionScreen()
options.create()

while True:
    screen.reset()

    for i in options.created_lines:
        if i[0] == "Linear":
            pygame.draw.line(window, (255, 0, 0), i[1], i[3])
        elif i[0] == "Quadratic" or i[0] == "Cubic" or i[0] == "Polynomial":
            pygame.draw.lines(window, (128, 0, 128), False, i[1])

    pygame.display.update()
    options.options.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
