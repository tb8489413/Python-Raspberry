import PCF8591 as ADC
ADC.setup(0x48)
trt:
    while True:
        print(ADC.read(0))
        ADC.write(ADC.read(0))
finally:
    ADC.write(0)
