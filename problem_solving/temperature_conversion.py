int = input ("enter temp in  fahrenhite:")
try:
    fahr = float(int)
    cel = (fahr -32)*5.0/9.0
    print("temp in celcius:",cel)

except:
    print("error please enter a n")  