# Thermometer
<h2>Термометър с Raspberry Pi Pico</h2>

![](https://github.com/kele6man/Thermometer/blob/main/GIF.gif)

<br>


Този код показва текущата температура на 7-сегментен дисплей, свързан към Raspberry Pi Pico. Датчик DHT11 измерва температурата и изпраща данни до Pico контролерът, който след това актуализира дисплея.

<h3>Предварителни изисквания:</h3>
<ul>
  <li>Платка Raspberry Pi Pico</li>
  <li>7-сегментен дисплей модул с 4 цифри</li>
  <li>Модул DHT11 сензор</li>
  <li>Скоби или кабели за свързване на сензори и дисплей към Pico контролерът</li>
</ul>

<h3>Инструкции:<h3/>
Свържете сензора DHT11 и 7-сегментния дисплей към Pico според пиновата диаграма:
  
![](https://i.ibb.co/jJ428J9/Shema.jpg)

<br>

<h3>Сегментите (A - G, DP):</h3>
<ul>
  <li>Пин 2 на Raspberry Pi Pico -> A сегмент на дисплея</li>
  <li>Пин 3 на Raspberry Pi Pico -> B сегмент на дисплея</li>
  <li>Пин 4 на Raspberry Pi Pico -> C сегмент на дисплея</li>
  <li>Пин 5 на Raspberry Pi Pico -> D сегмент на дисплея</li>
  <li>Пин 6 на Raspberry Pi Pico -> E сегмент на дисплея</li>
  <li>Пин 7 на Raspberry Pi Pico -> F сегмент на дисплея</li>
  <li>Пин 8 на Raspberry Pi Pico -> G сегмент на дисплея</li>
  <li>Пин 9 на Raspberry Pi Pico -> DP сегмент на дисплея</li>
</ul>

<br>
<h3>Цифрите (D1 - D4):</h3>
<ul>
  <li>Пин 13 на Raspberry Pi Pico -> D1 на дисплея</li>
  <li>Пин 12 на Raspberry Pi Pico -> D2 на дисплея</li>
  <li>Пин 11 на Raspberry Pi Pico -> D3 на дисплея</li>
  <li>Пин 10 на Raspberry Pi Pico -> D4 на дисплея</li>
</ul>

<br>
<h3>Пинове на DHT11 сензора:</h3>
<ul>
  <li>Пин 18 на Raspberry Pi Pico -> + на DHT11</li>
  <li>Пин 19 на Raspberry Pi Pico -> out на DHT11</li>
  <li>Пин GND на Raspberry Pi Pico -> - на DHT11</li>
</ul>




Пиновете на моя дисплей са:

![](https://i.ibb.co/8c6Q7N9/4d7s.jpg)
  
<br>

Използвах модифицирания вариант на DHT11, но можете да използвате и стандартния като пропуснете третия пин.

![](https://i.ibb.co/w4ZvPB8/dht11.jpg)

<br>

</h3>
Температурата ще бъде показана на 7-сегментния дисплей в градуси по Целзий. Цифрите се актуализират на всеки 500 милисекунди.

<h3>отстраняване на неизправности</h3>
<ul>
  <li>Уверете се, че сензорът DHT11 е правилно свързан към Pico дъската.</li>
  <li>Проверете връзките между Pico дъската, 7-сегментния дисплей и сензора DHT11.</li>
  <li>Уверете се, че използвате правилната версия на сензора DHT. В този случай е 11, но може да бъде заменен с 22 или всяка друга подходяща версия.</li>
  <li>Проверете съвместимостта на 7-сегментния дисплей с Pico дъската и нейния интерфейс (I2C или SPI).</li>
</ul>
