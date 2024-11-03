# Thermometer
<h2>Thermometer with Raspberry Pi Pico</h2>

![](https://github.com/kele6man/Thermometer/blob/main/GIF.gif)

<br>

This code displays the current temperature on a 7-segment display connected to a Raspberry Pi Pico. The DHT11 sensor measures the temperature and sends data to the Pico controller, which then updates the display.

<h3>Requirements:</h3>
<ul>
  <li>Raspberry Pi Pico board</li>
  <li>4-digit 7-segment display module</li>
  <li>DHT11 sensor module</li>
  <li>Wires or connectors to link the sensors and display to the Pico controller</li>
</ul>

<h3>Instructions:</h3>
Connect the DHT11 sensor and 7-segment display to the Pico according to the pinout diagram:

![](https://i.ibb.co/jJ428J9/Shema.jpg)

<br>

<h3>Segments (A - G, DP):</h3>
<ul>
  <li>Pin 2 on Raspberry Pi Pico -> A segment on the display</li>
  <li>Pin 3 on Raspberry Pi Pico -> B segment on the display</li>
  <li>Pin 4 on Raspberry Pi Pico -> C segment on the display</li>
  <li>Pin 5 on Raspberry Pi Pico -> D segment on the display</li>
  <li>Pin 6 on Raspberry Pi Pico -> E segment on the display</li>
  <li>Pin 7 on Raspberry Pi Pico -> F segment on the display</li>
  <li>Pin 8 on Raspberry Pi Pico -> G segment on the display</li>
  <li>Pin 9 on Raspberry Pi Pico -> DP segment on the display</li>
</ul>

<br>
<h3>Digits (D1 - D4):</h3>
<ul>
  <li>Pin 13 on Raspberry Pi Pico -> D1 on the display</li>
  <li>Pin 12 on Raspberry Pi Pico -> D2 on the display</li>
  <li>Pin 11 on Raspberry Pi Pico -> D3 on the display</li>
  <li>Pin 10 on Raspberry Pi Pico -> D4 on the display</li>
</ul>

<br>
<h3>DHT11 Sensor Pins:</h3>
<ul>
  <li>Pin 18 on Raspberry Pi Pico -> + on DHT11</li>
  <li>Pin 19 on Raspberry Pi Pico -> out on DHT11</li>
  <li>Pin GND on Raspberry Pi Pico -> - on DHT11</li>
</ul>

The pins on my display are:

![](https://i.ibb.co/8c6Q7N9/4d7s.jpg)
  
<br>

I used the modified version of the DHT11, but you can also use the standard version and skip the third pin.

![](https://i.ibb.co/w4ZvPB8/dht11.jpg)

<br>

</h3>
The temperature will be displayed on the 7-segment display in degrees Celsius. The digits are updated every 500 milliseconds.

<h3>Troubleshooting</h3>
<ul>
  <li>Ensure that the DHT11 sensor is properly connected to the Pico board.</li>
  <li>Check the connections between the Pico board, the 7-segment display, and the DHT11 sensor.</li>
  <li>Make sure you are using the correct version of the DHT sensor. In this case, it's 11, but it can be replaced with 22 or any other suitable version.</li>
  <li>Verify the compatibility of the 7-segment display with the Pico board and its interface (I2C or SPI).</li>
</ul>
