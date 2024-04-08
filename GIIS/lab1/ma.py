import pygame, os
from PIL import Image

class wuzAlgorithm:
    def __init__(self, img, point1, point2, clr):
        self.image = img
        self.colour = clr
        self.x1, self.y1 = point1
        self.x2, self.y2 = point2
        self.dx, self.dy = self.x2 - self.x1, self.y2 - self.y1
        self.steep = abs(self.dy) > abs(self.dx)
        self.calc_details()
        self.startX, self.endX = self.calc_endPoint(point1) + 1, self.calc_endPoint(point2)
        self.draw_lines()

        
    def calc_points(self, xCoOrd, yCoOrd):
        return ((xCoOrd, yCoOrd), (yCoOrd, xCoOrd))[self.steep]


    def fPart(self, x):
        return x - int(x)


    def rfPart(self, x):
        return 1 - self.fPart(x)


    def calc_endPoint(self, point):
        x, y = point
        return int(round(x))


    def fill_colour(self, point, alpha=1):
        colour = tuple(map(lambda background, foreground: int(round(alpha * foreground + (1-alpha) * background)), self.image.getpixel(point), self.colour))
        self.image.putpixel(point, colour)


    
    def calc_details(self):
        if self.steep:
            self.x1, self.x2, self.y1, self.y2, self.dx, self.dy = self.y1, self.y2, self.x1, self.x2, self.dy, self.dx
        if self.x2 < self.x1:
            self.x1, self.x2, self.y1, self.y2 = self.x2, self.x1, self.y2, self.y1
        self.gradient = self.dy / self.dx
        self.yIntersection = self.y1 + self.rfPart(self.x1) * self.gradient


    def draw_lines(self):
        for x in range(self.startX, self.endX):
            y = int(self.yIntersection)
            self.fill_colour(self.calc_points(x, y), self.rfPart(self.yIntersection))
            self.fill_colour(self.calc_points(x, y + 1), self.fPart(self.yIntersection))
            self.yIntersection += self.gradient



class wuzWindow:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.resolution = self.width, self.height
        self.screen = pygame.display.set_mode(self.resolution)
        self.display = pygame.Surface(self.resolution)
        self.clock = pygame.time.Clock()

    
    def display_line(self, img, point1, point2, clr):
        self.wuzAlgo = wuzAlgorithm(img, point1, point2, clr)
        self.mode, self.size, self.data = img.mode, img.size, img.tobytes()
        self.output_image = pygame.image.fromstring(self.data, self.size, self.mode)


    def load_window(self):
        self.display.fill('black')
        self.screen.blit(self.display, (0, 0))
        self.screen.blit(self.output_image, (0,0))


    def save_image(self):
        #os.chdir(r"C:\Users\rebor\Desktop\Skywalker\Internships\OpenGenus\Xiaolin Wuz Algorithm")
        directory = os.getcwd() + r"\Wu's Line Drawing Algorithm Output.jpg"
        pygame.image.save(self.screen, directory)
        print("Image has been successfully saved at the following location:\n", directory)


    def run_window(self, img, start, end, step):
        self.buttonFont = pygame.font.SysFont('times new roman', 14, bold=True)
        t1 = self.buttonFont.render("", True, (0, 0, 255))
        t2 = self.buttonFont.render('[Press SPACE to save image]', True, (0, 0, 255))
        pygame.display.set_caption("")
        for line in range(start, end, step):
            self.display_line(img, (20, 20), (450, line), (0, 128, 128))
            # self.display_line(img, (80, 80), (150, 80), (0, 128, 128))
            # self.display_line(img, (250, 80), (320, 80), (0, 128, 128))
            # self.display_line(img, (165, 140), (220, 140), (0, 128, 128))
            # self.display_line(img, (80, 200), (320, 200), (0, 128, 128))

        while True:
            self.load_window()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.save_image()
            self.screen.blit(t1, (self.width - 280, self.height - self.height + 10))
            self.screen.blit(t2, (self.width - 280, self.height - self.height + 30))
            pygame.display.flip()
            self.clock.tick(60)


black = (255, 255, 255)
image = Image.new("RGB", (500, 500), black)
obj1 = wuzWindow()
obj1.run_window(image, 10, 450, 30)