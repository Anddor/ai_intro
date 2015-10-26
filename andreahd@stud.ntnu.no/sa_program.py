import egg_carton
import sa
import carton_image_gen

__author__ = 'anddor'

m = 10
n = 10
k = 6

problem = egg_carton.EggCarton(m, n, k)

solution = sa.sa_algorithm(problem, 0.4, 0.000001)
print(solution)

image_gen = carton_image_gen.Board_img_gen(5, 5)
image_gen.draw_world()
image_gen.draw_open_closed(solution, "o")
image_gen.show_img()
image_gen.save(str(m), str(n), str(k))
