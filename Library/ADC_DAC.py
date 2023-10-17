# For ADC pins, use the ADC port already defined on the board

# You can use:
adc0 = pyb.ADC(0)
adc1 = pyb.ADC(1)
adc2 = pyb.ADC(2)
adc3 = pyb.ADC(3)
adc4 = pyb.ADC(4)
adc5 = pyb.ADC(5)
adc6 = pyb.ADC(6)

# Any other number won't work or will force you to reset the board (the black button)