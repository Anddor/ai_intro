import egg_carton
import sa
import carton_image_gen

__author__ = 'anddor'

problem = egg_carton.EggCarton(5, 5, 1)

solution = sa.sa_algorithm(problem, 5000, 1)
print(solution)

image_gen = carton_image_gen.Board_img_gen(5, 5)
image_gen.draw_world()
image_gen.draw_open_closed(solution, "o")

