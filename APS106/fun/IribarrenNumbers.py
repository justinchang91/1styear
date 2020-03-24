import math


def type_of_wave(wave_dimensions):
    """
    :return: The type of wave "suring or collapsing", "plunging" or "spilling", according to the waves
    Iribarren number
    """

    # Split dimensions and convert to float
    alpha = float(wave_dimensions.split(",")[0])
    h = float(wave_dimensions.split(",")[1])
    l = float(wave_dimensions.split(",")[2])

    # calculate the Iribarren Number
    ir = math.tan(alpha) / math.sqrt(h/l)

    # check the ir
    if ir > 3.3:
        return "surging or collapsing"
    elif 0.5 < ir <= 3.3:
        return "plunging"
    else:
        return "spilling"


print(type_of_wave("1.24,1,3"))
