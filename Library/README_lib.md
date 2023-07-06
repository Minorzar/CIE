# Library

All the PY file are some "libraries" that may be use in your code.

They are not really libraries but part of code you may need, feel free to use them.

This document follow t

- [pyb.infos](#infos)
- [Functions](#Functions)
	- [delay](#mdelay)
	- [udelay](#udelay)
	- [millis](#millis)
	- [micros](#micros)
	- [hard](#hard)
	- [disable](#disable)
	- [enable](#enable)
	- [stop](#stop)
	- [rng](#rng)
- [Classes](#Classes)

The board comes already with some function that allow the user to code.

<a id="infos"></a>
# pyb.infos

It will give informations as describe below:

### ID
ID of the board.

### DEVID
The device ID.

### REVID
The device revision.

### S, H, P1 and P2
Indicate the adresses of the flash memory and RAM memory.

### \_sstack and \_estack
The adresses of Start and End of the stack.

### \_etext, \_sidata, \_sdata, \_edata, \_sbss, \_ebss
Adresses of Start and End of the executable data, initialized data and uninitialized data.

### \_ram start, \_heap start, \_heap end, \_ram end
Adresses of Start and End of the RAM and HEAP.

### qstr
Indicate the numbre of pools, of qstrings, number of byte used to store string and number of byte used for qstrings overall.

### GC
Memory management of the Garbage Collector: total size, used and usage.

### LFS free
Indicate the free space in the LittleFS for file storage inside the firmware.


If you have any question about this, do not hesitate to ask a student of a teacher.


<a id="Functions"></a>
# Functions available

<a id="mdelay"></a>
### <span style="color: blue;">pyb.delay: int -&gt; void</span>
Wait for n milliseconds.

<a id="udelay"></a>
### pyb.udelay: int -> void
Wait for n microseconds.

<a id="millis"></a>
### pyb.millis: void -> int
Gives the number of milliseconds since last hard reset.

<a id="micros"></a>
### pyb.micros: void -> int
Gives the number of microseconds since last hard reset.

<a id="hard"></a>
### pyb.hard\_reset: void -> void
Hard reset the board.

<a id="disable"></a>
### pyb.disable\_irq, void -> bool
Disable the interrupt requests. The boolean return is the previous state of the IRQ.

<a id="enable"></a>
### pyb.enable\_irq, bool -> void
Enable (if True) the interrupt requests.

<a id="stop"></a>
### pyb.stop: void -> void
Set the board in a sleeping state. The only way to remove this state is a hard reset (external) or a RTC event (see below). Execution will continue where it stops.

<a id="rng"></a>
### pyb.rng: void -> int
Return a 30 bit hardware generated random number.

<a id="Classes"></a>
# Classes


## Timer

### pyb.Timer: int -> Timer
Create a timer object, the integer in parameter can be 1 to 14 (you may need to look the board documentation to be sure to use the correct integer).

The methods are:

### init:
Initialise the timer. Initialisation must be made either by frequency (in Hz) with timer.init(freq = ...) or by prescaler and period (much more complex) with timer.init(prescaler = ..., period = ...).
Note that there are other parameters that may be initialise, but there are specific methods to do so.

### deinit:
Deinitialises the timer (set to default every parameters).

### callback(fun):
Allow user to make a callback function. If fun is None, callback will be disable.

### counter:
If a value is given, it will set the counter to the value, otherwise, it will get the current value of the counter.

### freq:
Set or get the value of the frequency.

### period:
Set or get the value of the period.

### prescaler:
Set or get the value of the prescaler.

### source\_freq:
Get the frequency of the source of the timer.

There is another type of timer (timerchannel), but I don't think you'll need it. If you need it, feel free to ask students or teacher about them.


## ADC

### pyb.ADC: str -> ADC
Create an analog to digital converter associated to the pin entered as a string.

The methods are:

### read:
Read the analog value of the pin and return it.

### read\_timed(buf, freq):
Buf is an array or a bytearray, freq an integer (in Hz).
It read the analog values into the buf at a rate set by freq.

### read\_timed\_multi((ADC), (buf), freq):
It is basically the previous methods but use for more than one ADC pin. Parameters in parenthesis must be tuple of the same size.

### read\_channel(channel):
Allow to read directly the value of the channel enter in parameter.

### read\_core\_vref:
Return the MCU VREF (REFerence Voltage).

### read\_core\_temp:
Return the MCU temperature.

### read\_core\_vbat:
Return the MCU VBAT (BATtery Voltage).

### read\_vref:
Return the MCU supply voltage.


## DAC:

### pyb.DAC: str -> DAC
Create a digital to analog converter associated to the pin entered as a string.

The methods are:

### init(bit,buffering):
Set the bit (value may be 8 or 12) and buffering may be None, True or False (None -> default, True -> enable, False -> disable).

### deinit:
Free the ressources link to the DAC.

### write(value):
Write a value in the DAC, value must be between 0 and 4095.

### write\_timed(buf, freq):
Write a serie of value (stored in the buf variable (either an array or a bytearray)) in the DAC at the frequency entered in parameter in Hz.

### write\_timed\_multi(bufs, freq):
Same as before but with multiple DAC channel. bufs this time is an array of array or array of bytearray.

### triangle(freq):
Generate a triangular wave at the frequency entered as a parameter (the amplitude will probably be either 3.3V or 5V).

### noise:
generate a noise signal on the DAC.


## Switch

### pyb.Switch: void -> Switch
Create a switch object.

The methods are:

### \_\_call\_\_:
Call switch object directly to get its state.

### value:
Return True or False depending of the state of the switch. (not really sure about the difference with \_\_call\_\_)

### callback:
Allow the user to define a callback function (exemple in the library)


## LED

## pyb.LED: int -> LED
Create a LED object associated to the integer send (pyb.LED(1) will create the object LED for the user LED 1).

The methods are:

### on:
Turn on the LED

### off:
Turn off the LED

### toggle:
Change the state of the LED

### intensity(n):
Set the intensity of the LED to n (do not work on our board as far as I know)


## Pin

### pyb.Pin: str -> Pin
Create a Pin object associated to the pin entered as a string.

The methods are:

### debug:
Get or set the debugging state (using a boolean).

### dict:
Get or set the pin mapper dictionary.

### mapper:
Get or set the pin mapper function.

### value:
Return 0 or 1 depending on the state of the pin
value({0,1}), set the pin to high (1) or low (0).

### init(mode, pull):
Where the mode can be: 
		pyb.Pin.IN (input pin)
		pyb.Pin.OUT\_PP (output in push-pull)
		pyb.Pin.OUT\_OD (output in open-drain)
		pyb.Pin.ALT (alternate, use for I2C and SPI for example
and pull can be:
		pyb.Pin.PULL\_UP
		pyb.Pin.PULL\_DOWN
		None

### mode:
Get the current mode of the pin (is not a set function).

### af\_list:
Return an array of alternate functions available for the pin.

### af:
Return the current alternate function of the pin.

### pull:
Return the current pull configuration of the pin.

### pin:
Return the pin number.

### port:
Return the port number.

### names:
Return the cpu and board names for the pin.

### name:
Return the name of the pin.

### gpio:
Return the address of the GPIO block associated with the pin.


## ExtInt

### pyb.ExtInt: str -> int -> int -> (ExtInt -> void) -> ExtInt
Create an external interrupt on the pin enter as a str. The first int is the trigger and can be:
		pyb.ExtInt.IRQ\_RISING (trigger on rising edge)
		pyb.ExtInt.IRQ\_FALLING (trigger on falling edge)
		pyb.ExtInt.IRQ\_RISING_FALLING (trigger on a change of state)
the second int is the pull of the pin and can be:
		pyb.ExtInt.PULL_NONE
		pyb.ExtInt.PULL_UP
		pyb.ExtInt.PULL_DOWN
the function is the callback function that'll be use when the interrupt is trigger
It has three methods:
enable -> enable the external interrupt
disable -> disable the external interrupt
line -> return the pin number



pyb.RTC -> allow the user to manipulate the Real Time Clock inside the board. Here's the most commun and used methods:
datetime -> return (year, month, day, day of the week, hours, minutes, secondes, milliseconds)
datetime(date) -> set the time to the time send (must be the same type as the one above)
Other methods can existe and may be used, but this are the most used one.

py