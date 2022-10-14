#fahrenheit to celsius
f2c = float(5/9)
tempF = float(input('Temperature(f):'))


def f_to_c(tempF):
    tempC = (tempF -32)*f2c
    return tempC


temp1 = f_to_c(tempF)
print(temp1, 'degrees Celsius')
