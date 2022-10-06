# ft_and_inch_to_m converts height in ft and inches to m
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

# lb_to_kg converts weight in lbs to kg
def lb_to_kg(lb):
    return lb * 0.4535923

# bmi calculates bmi with height in m and weight in kg as parameters
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print(bmi(weight = lb_to_kg(157), height = ft_and_inch_to_m(5, 10)))