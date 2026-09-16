import pygame
from random import randint


pygame.init()
back = (75, 41, 234)
window = pygame.display.set_mode((500,500))

class TextArea():
    def __init__(self, x, y, color, height, width):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_fill = color

    def set_text(self, text, fsize, t_color):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, t_color)

    def draw(self, shift_x, shift_y):
        pygame.draw.rect(window, self.color_fill, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


window.fill(back)
clock = pygame.time.Clock()
question = TextArea(75, 50, (82, 51, 51), 100, 350)
question.set_text('Вопрос', 40, (60, 130, 140))
question.draw(130, 32)
answer = TextArea(75, 250, (82, 51, 51), 100, 350)
answer.set_text('Ответ', 40, (60, 130, 140))
answer.draw(130, 32)
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                random_num = randint(1, 5)
                if random_num == 1:
                    question.set_text('Где Эйфелева башня?', 30, (60, 130, 140))
                elif random_num == 2:
                    question.set_text('Как звали Ньютона?', 30, (60, 130, 140))
                elif random_num == 3:
                    question.set_text('На каком языке говорят в Аргентине?', 30, (60, 130, 140))
                elif random_num == 4:
                    question.set_text('Какого цвета солнце?', 30, (60, 130, 140))
                elif random_num == 5:
                    question.set_text('Какой формы яблоко?', 30, (60, 130, 140))  

            elif event.key == pygame.K_a:
                random_num2 = randint(1, 5)
                if random_num2 == 1:
                    answer.set_text('Париж', 30, (60, 130, 140))
                elif random_num2 == 2:
                    answer.set_text('Исаак', 30, (60, 130, 140))
                elif random_num2 == 3:
                    answer.set_text('Испанский', 30, (60, 130, 140))
                elif random_num2 == 4:
                    answer.set_text('Шар', 30, (60, 130, 140))
                elif random_num2 == 5:
                    answer.set_text('Желтый', 30, (60, 130, 140))

            question.draw(40, 32)
            answer.draw(120,32)


    clock.tick(40)
    pygame.display.update()


