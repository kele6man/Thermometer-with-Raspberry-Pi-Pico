from machine import Pin
import utime
import dht
# Дефиниране на пиновете за всеки сегмент и десетична точка
segment_pins = [
    Pin(2, Pin.OUT),  # Segment A
    Pin(3, Pin.OUT),  # Segment B
    Pin(4, Pin.OUT),  # Segment C
    Pin(5, Pin.OUT),  # Segment D
    Pin(6, Pin.OUT),  # Segment E
    Pin(7, Pin.OUT),  # Segment F
    Pin(8, Pin.OUT),  # Segment G
    Pin(9, Pin.OUT),  # Decimal Point
    Pin(10, Pin.OUT), # Digit 1
    Pin(11, Pin.OUT), # Digit 2
    Pin(12, Pin.OUT), # Digit 3
    Pin(13, Pin.OUT)  # Digit 4
]
# Речник, който картографира всяка цифра към нейната съответна стойност на сегмента
digit_to_segments = {
    0: (1, 1, 1, 1, 1, 1, 0, 0),
    1: (0, 1, 1, 0, 0, 0, 0, 0),
    2: (1, 1, 0, 1, 1, 0, 1, 0),
    3: (1, 1, 1, 1, 0, 0, 1, 0),
    4: (0, 1, 1, 0, 0, 1, 1, 0),
    5: (1, 0, 1, 1, 0, 1, 1, 0),
    6: (1, 0, 1, 1, 1, 1, 1, 0),
    7: (1, 1, 1, 0, 0, 0, 0, 0),
    8: (1, 1, 1, 1, 1, 1, 1, 0),
    9: (1, 1, 1, 1, 0, 1, 1, 0),
    'C': (1, 0, 0, 1, 1, 1, 0, 0)  
}

# Функция за показване на конкретна цифра на дадена позиция
def display_digit(position, digit):
   
    if position < 4:
       
        for pin in segment_pins:
            pin.value(1)
            segments = digit_to_segments.get(digit, (0, 0, 0, 0, 0, 0, 0))
        for i, segment in enumerate(segments):
            segment_pins[i].value(segment)
        
        for pin in segment_pins[8:]:
            pin.value(1)
        segment_pins[8 + position].value(0)
# Функция за показване на текущата температура
def temp():
	try:
		sensor = dht.DHT11(Pin(19))
		power = Pin(18, Pin.OUT)
		power.value(1)
	
		utime.sleep(0.1)
		sensor.measure()
		temp = sensor.temperature()
		temp_f = temp * (9/5) + 32.0
		return str(temp)
	except OSError as e:
		return 'Няма връска със сензора.'
		



while True:
	temperature_c = "{}0C".format(temp())
	for i in range(4):
		if i == 3:
			display_digit(i, temperature_c[i])
		elif i == 1:#Слага десетична точка на втора цифра		
			display_digit(i, int(temperature_c[i]))
			segment_pins[7].value(1)
		else:
			display_digit(i, int(temperature_c[i]))	
		utime.sleep_ms(500)
        
