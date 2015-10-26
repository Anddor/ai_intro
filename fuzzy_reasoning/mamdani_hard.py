__author__ = 'anddor'


def triangle(position, x0, x1, x2, clip=1):
    """Membership function for triangle"""
    # ___/\___
    # x0 x1 x2

    value = 0.0
    if x0 <= position <= x1:
        value = (position - x0) / (x1 - x0)
    elif x1 <= position <= x2:
        value = (x2 - position) / (x1 - x0)
    value = min(value, clip)
    return value


def grade(position, x0, x1, clip=1):
    """Membership function for grade:"""
    #     ___
    # ___/
    # x0  x1
    value = 0.0
    if position >= x1:
        value = 1.0
    elif position <= x0:
        value = 0.0
    else:
        value = (position - x0) / (x1 - x0)
    value = min(value, clip)
    return value


def reverse_grade(position, x0, x1, clip=1):
    """Membership function for reverse grade"""
    # ___
    #    \___
    # x0  x1
    value = 0.0
    if position <= x0:
        value = 1.0
    elif position >= x1:
        value = 0.0
    else:
        value = (x1 - position) / (x1 - x0)
    value = min(value, clip)
    return value


def mamdani(distance_pos, delta_pos):
    # step 1, fuzzification
    very_small = reverse_grade(distance_pos, 1, 2.5)
    small = triangle(distance_pos, 1.5, 3, 4.5)
    perfect = triangle(distance_pos, 3.5, 5, 6.5)
    big = triangle(distance_pos, 5.5, 7, 8.5)
    very_big = grade(distance_pos, 7.5, 9)

    shrinking_fast = reverse_grade(delta_pos, -4, -2.5)
    shrinking = triangle(delta_pos, -3.5, -2, -0.5)
    stable = triangle(delta_pos, -1.5, 0, 1.5)
    growing = triangle(delta_pos, 0.5, 2, 3.5)
    growing_fast = grade(delta_pos, 2.5, 4)

    # step 2, rule eval
    # Rule 1: Distance small and delta is growing
    clip_none = min(small, growing)
    # rule 2: distance small AND delta is stable
    clip_slow_down = min(small, stable)
    # rule 3: distance perfect and delta is growing
    clip_speed_up = min(perfect, growing)
    # rule 4: distance is very big AND (delta is not growing or delta is not growing fast)
    clip_floor_it = min(very_big, max(1 - growing, 1 - growing_fast))
    # rule 5: distance very small then action is brake hard
    clip_break_hard = very_small


    # actions

    # step 3: aggregate

    f = []
    for x in range(-10, 11):
        part_sum = 0
        f_break_hard = reverse_grade(x, -8, -5, clip_break_hard)
        part_sum = max(part_sum, f_break_hard)
        f_slow_down = triangle(x, -7, -4, -1, clip_slow_down)
        part_sum = max(part_sum, f_slow_down)
        f_none = triangle(x, -3, 0, 3, clip_none)
        part_sum = max(part_sum, f_none)
        f_speed_up = triangle(x, 1, 4, 7, clip_speed_up)
        part_sum = max(part_sum, f_speed_up)
        f_floor_it = grade(x, 5, 8, clip_floor_it)
        part_sum = max(part_sum, f_floor_it)
        f.append(part_sum)


    # step 4: defuzz

    s = 0
    for i in range(0, 21):
        x = i - 10
        s += f[i] * x

    if sum(f): # avoid divide by zero
        ans = s / sum(f)
    else:
        ans = 0

    return ans

print(mamdani(3.9, 0.9))
