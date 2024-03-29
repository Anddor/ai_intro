import cProfile
import egg_carton
import sa
import carton_image_gen

__author__ = 'anddor'


def main():
    m = 10  # rows
    n = 10  # columns
    k = 6  # allowed collisions

    problem = egg_carton.EggCarton(m, n, k)  # create problem object

    solution = sa.sa_algorithm(problem, 0.4, 0.000001)  # run algorithm and return solution
    print(solution)

    #  Draw imager
    image_gen = carton_image_gen.BoardImgGen(n, m)
    image_gen.draw_world()
    image_gen.draw_open_closed(solution, "o")
    image_gen.show_img()
    image_gen.save(str(m), str(n), str(k))


cProfile.run("main()")
