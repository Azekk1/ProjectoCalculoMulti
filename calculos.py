def T(x, y):
    resultado = ((0.0160743634706346 * (x ** 3)) + (-0.0299717756251621 * (y ** 3)) + (-0.000409375351095420 * (
            x ** 2) * y) +( -0.125435603627039 * x * (y ** 2) )+ (-0.0842903336554173 * (x ** 2)) +
                 (0.853906304682340 * (y ** 2)) + (1.01637198527351 * x * y) + (-1.28414513927032 * x) + (
                             -5.24815217032369 * y + 17.7505634568843))
    return resultado


print(T(6.49,8))

