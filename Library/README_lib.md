# Library

All the PY file are some "libraries" that may be use in your code. They are not really libraries but part of code you may need, feel free to use them.

This document contains most if not all the information you may need for your challenge. It follows this arrangement:

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
- [Usual classes](#Usual)
	- [Pin](#Pin)
	- [PinAF](#PinAF)
	- [ADC](#ADC)
	- [DAC](#DAC)
	- [Timer](#Timer)
	- [LED](#LED)
	- [Switch](#Switch)
- [Communication classes](#Comm)
	- [I2C](#I2C)
	- [SPI](#SPI)
	- [UART](#UART)
- [Extra classes](#Extra)
	- [Timerchannel](#Timerchannel)
	- [RTC](#RTC)
	- [ExtInt](#ExtInt)
	- [CAN](#CAN)

For each functions describe, if a parameter has a default value, a lot of time, it's better to leave it that way. Otherwise, if you still need to change it, you can do like so:

```
def hello(repeat=1):
	for _ in range(repeat):
		print("hello world !")
	return None

hello()		# will print one time "hello world !"

hello(repeat=1)		# will do the same (do not do that, you are losing storage in the microprocessor for nothing)

hello(repeat=2)		# will print two times "hello world !" 
```


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
Indicate the addresses of the flash memory and RAM memory.

### \_sstack and \_estack
The addresses of Start and End of the stack.

### \_etext, \_sidata, \_sdata, \_edata, \_sbss, \_ebss
Addresses of Start and End of the executable data, initialized data and uninitialized data.

### \_ram start, \_heap start, \_heap end, \_ram end
Addresses of Start and End of the RAM and HEAP.

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
### pyb.delay: int &rarr; void
Wait for n milliseconds.


<a id="udelay"></a>
### pyb.udelay: int &rarr; void
Wait for n microseconds.


<a id="millis"></a>
### pyb.millis: void &rarr; int
Gives the number of milliseconds since last hard reset.


<a id="micros"></a>
### pyb.micros: void &rarr; int
Gives the number of microseconds since last hard reset.


<a id="hard"></a>
### pyb.hard\_reset: void &rarr; void
Hard reset the board.


<a id="disable"></a>
### pyb.disable\_irq, void &rarr; bool
Disable the interrupt requests. The boolean return is the previous state of the IRQ.


<a id="enable"></a>
### pyb.enable\_irq, bool &rarr; void
Enable (if True) the interrupt requests.


<a id="stop"></a>
### pyb.stop: void &rarr; void
Set the board in a sleeping state. The only way to remove this state is a hard reset (external) or a RTC event (see below). Execution will continue where it stops.


<a id="rng"></a>
### pyb.rng: void &rarr; int
Return a 30 bit hardware generated random number.


<a id="Usual"></a>
# Usual classes


<a id="Pin"></a>
## Pin

### pyb.Pin: str &rarr; Pin
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
- pyb.Pin.IN (input pin)
- pyb.Pin.OUT\_PP (output in push-pull)
- pyb.Pin.OUT\_OD (output in open-drain)
- pyb.Pin.ALT (alternate, use for I2C and SPI for example
and pull can be:
- pyb.Pin.PULL\_UP
- pyb.Pin.PULL\_DOWN
- None

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


<a id="PinAF"></a>
## PinAF

To create the object, you need to use (for the pin X1):

```
pinaf = pyb.Pin(pyb.Pin.board.X1, mode=pyb.Pin.ALT, alt=1)
```
With alt beeing the index of the alternate function in pyb.Pin.board.X1.af_list().

The methods are:

### \_\_str\_\_:
Return a string to describe the function use.

### index:
Return the function index.

### name:
Return the name of the function.

### reg:
Return the base register associated with the peripheral assigned to the function.


<a id="ADC"></a>
## ADC

### pyb.ADC: str &rarr; ADC
Create an analog to digital converter associated to the pin entered as a string.

The methods are:

### read:
Read the analog value of the pin and return it.

### read\_timed:
It read the analog values into the buf at a rate set by freq. So it has two parameters:
- buf &rarr; an array or a bytearray.
- freq &rarr; an integer (in Hz).

### read\_timed\_multi:
It is basically the previous methods but use for more than one ADC pin. The parameters are:
- ADC &rarr; a tuple of ADC pin.
- buf &rarr; a tuple of array or bytearray.
- freq &rarr; an integer (in Hz).
Be aware that the tuple have to be of the same size.

### read\_channel:
Allow to read directly the value of the channel enter in parameter (as an integer).

### read\_core\_vref:
Return the MCU VREF (REFerence Voltage).

### read\_core\_temp:
Return the MCU temperature.

### read\_core\_vbat:
Return the MCU VBAT (BATtery Voltage).

### read\_vref:
Return the MCU supply voltage.


<a id="DAC"></a>
## DAC:

### pyb.DAC: str &rarr; DAC
Create a digital to analog converter associated to the pin entered as a string.

The methods are:

### init:
Reinitialise the DAC with a new bit and buffering. The parameters are:
- bit &rarr; may be 8 or 12.
- buffering &rarr; may be None, True or False (None &rarr; default, True &rarr; enable, False &rarr; disable).

### deinit:
Free the ressources link to the DAC.

### write:
Write a value in the DAC. Only one parameter:
- value &rarr; must be between 0 and 4095.

### write\_timed:
Write a serie of value in the DAC at a given frequency. Parameters are:
- buf &rarr; thing that will be written in the DAC (either an array or a bytearray).
- freq &rarr; the frequency rate used (in Hz).

### write\_timed\_multi:
Same as before but with multiple DAC channel. Same parameters as before too but buf is an array of array or array of bytearray this time.

### triangle:
Generate a triangular wave (the amplitude will probably be either 3.3V or 5V). The parameter is:
- frequency &rarr; frequency of the wave.

### noise:
generate a noise signal on the DAC.


<a id="Timer"></a>
## Timer

### pyb.Timer: int &rarr; Timer
Create a timer object, the integer in parameter can be 1 to 14 (you may need to look the board documentation to be sure to use the correct integer).

The methods are:

### init:
Initialise the timer. Initialisation must be made either by frequency (in Hz) with timer.init(freq = ...) or by prescaler and period (much more complex) with timer.init(prescaler = ..., period = ...).
Note that there are other parameters that may be initialise, but there are specific methods to do so.
It also has the parameter brk which can be:
- Timer.BRK\_OFF &rarr; kill the output when the timer is off.
- Timer.BRK\_LOW &rarr; kill the output when the pin is set low.
- Timer.BRK\_HIGH &rarr; kill the output when the pin is set high.

### deinit:
Deinitialises the timer (set to default every parameters).

### callback:
Allow user to make a callback function. Parameter is:
- fun &rarr; if None, callback will be disable, otherwise it will be the function use.

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


<a id="LED"></a>
## LED

## pyb.LED: int &rarr; LED
Create a LED object associated to the integer send (pyb.LED(1) will create the object LED for the user LED 1).

The methods are:

### on:
Turn on the LED.

### off:
Turn off the LED.

### toggle:
Change the state of the LED.

### intensity:
Get or set the intensity of the LED to a given value (do not work on our board as far as I know).


<a id="Switch"></a>
## Switch

### pyb.Switch: void &rarr; Switch
Create a switch object.

The methods are:

### \_\_call\_\_:
Call switch object directly to get its state.

### value:
Return True or False depending of the state of the switch. (not really sure about the difference with \_\_call\_\_).

### callback:
Allow the user to define a callback function (exemple in the library).


<a id="Comm"></a>
# Communication classes


<a id="I2C"></a>
## I2C

### pyb.I2C: int &rarr; int &rarr; int &rarr; bool &rarr; bool &rarr; I2C
Create an I2C object on the bus given in argument.
Parameters are:
- bus &rarr; The bus on which the I2C will be define.
- mode &rarr; The mode on which the I2C bus will work, can be:
	- I2C.CONTROLLER
	- I2C.PERIPHERAL
- addr &rarr; The 7-bit address of the peripheric (use only in peripheral). Default is 0x12.
- baudrate &rarr; The SCL clock rate (use only in controller). Default is 400000.
- gencall &rarr; If True, the bus will support general call mode. Default is False.
- dma &rarr; if True, DMA will be allow for the I2C transfers. Default is False.

You may at first only use pyb.I2C as an int &rarr; I2C function with only the bus specify and the use then method init with the other parameters.

The methods are:

### init:
Initialise the I2C bus. Parameters are:
- mode &rarr; The mode on which the I2C bus will work, can be:
	- I2C.CONTROLLER
	- I2C.PERIPHERAL
- addr &rarr; The 7-bit address of the peripheric (use only in peripheral).
- baudrate &rarr; The SCL clock rate (use only in controller).
- gencall &rarr; If True, the bus will support general call mode.
- dma &rarr; If True, DMA will be allow for the I2C transfers.

### deinit:
Turn off the I2C bus. Reset all parameters set for the bus.

### is\_ready:
Check if the I2C device responds to the given address. Parameter is:
addr &rarr; address that should be tested.
Will only work if the I2C bus has been set to controller.

### mem\_ready:
Read the memory of an I2C device. Parameters are:
- data &rarr; Can be:
	- An int &rarr; number of byte to read.
	- A buffer &rarr; will be use to store the data read.
- addr &rarr; The I2C device address.
- memaddr &rarr; The memory location within the I2C device.
- timeout &rarr; Timeout to wait for the read in ms. Default is 5000.
- addr\_size &rarr; Select the width of memaddr. Can either be 8 or 16. Default is 8.
It will return the read data. Will only work if the I2C bus has been set to controller.

### mem\_write:
Write to the memory of an I2C device. Parameters are:
- data &rarr; Can be an integer or a buffer to write from.
- addr &rarr; The I2C device address.
- memaddr &rarr; The memory location within the I2C device.
- timeout &rarr; Timeout to wait for the write. Default is 5000.
- addr\_size &rarr; Select the width of memaddr. Can either be 8 or 16. Default is 8.
Will only work if the I2C bus has been set to controller.

### recv:
Receive the data on the bus. Parameters are:
- recv &rarr; Can be an integer (number of byte received) or a buffer where the data will be stored.
- addr &rarr; The address to receive from (only in controller mode).
- timeout &rarr; Timeout to wait for the receive in ms. Default is 5000.
It will return a buffer if an integer has been pass as recv, otherwise the buffer given in parameter will be modified.

### send:
Send data on the bus. Parameters are:
- send &rarr; The data to send. Can be an integer or a buffer.
- addr &rarr; The address where you want to send. Only needed in controller mode. Default is 0x00.
- timeout &rarr; Timeout to wait for the send in ms. Default is 5000.

### scan:
Return a list of the all the I2C addresses (from 0x01 to 0x7f) that respond. Will only work in controller mode.


<a id="SPI"></a>
## SPI

### pyb.SPI: int &rarr; int &rarr; int &rarr; int &rarr; int &rarr; int &rarr; int &rarr; int &rarr; bool &rarr; bool &rarr; SPI
Create a SPI object. Parameters are:
- bus &rarr; The bus on which the SPI object will be created.
- mode &rarr; The mode on which the SPI object will work, it can be:
	- SPI.CONTROLLER
	- SPI.PERIPHERAL
- baudrate &rarr; The SCK clock rate. Default is 328125.
- prescaler &rarr; Use to derive the SCK from the APB bus frequency. It will overrides the baudrate. It can be a power of two up to 256 starting at 2. Default is -1 (meaning deactivated).
- polarity &rarr; Level on which the idle clock sit at. Can be 0 or 1. Default is 1.
- phase &rarr; Sample the data on the first or second clock edge. Can be 0 or 1 respectively. Default is 0.
- bits &rarr; Size of the world that will be transfer in bits. Can be 8 or 16. Default is 8.
- firstbit &rarr; Select the first bit of the world. It can be:
	- SPI.LSB &rarr; Set the first bit to be the least significant bit.
	- SPI.MSB &rarr; Set the first bit to be the most significant bit.
- ti &rarr; Indicate Texas Instrument signal is set to True. Default is False (meaning Motorola signal conventions).
- crc &rarr; Define the CRC using a polynomial specifier (a binary definition of the polynome (example: 1011 =x^3+x+1). First and last bit must be 1). Default is None (no crc used).

You may at first only use pyb.SPI as an int &rarr; SPI function with only the bus specify and then use the method init with the other parameters.

Methods are:

### init:
Initialse the SPI bus if it has not be made previously or if the bus was deinit. Parameters are:
- mode &rarr; The mode on which the SPI object will work, it can be:
	- SPI.CONTROLLER
	- SPI.PERIPHERAL
- baudrate &rarr; The SCK clock rate. Default is 328125.
- prescaler &rarr; Use to derive the SCK from the APB bus frequency. It will overrides the baudrate. It can be a power of two up to 256 starting at 2. Default is -1 (meaning deactivated).
- polarity &rarr; Level on which the idle clock sit at. Can be 0 or 1. Default is 1.
- phase &rarr; Sample the data on the first or second clock edge. Can be 0 or 1 respectively. Default is 0.
- bits &rarr; Size of the world that will be transfer in bits. Can be 8 or 16. Default is 8.
- firstbit &rarr; Select the first bit of the world. It can be:
	- SPI.LSB &rarr; Set the first bit to be the least significant bit.
	- SPI.MSB &rarr; Set the first bit to be the most significant bit.
- ti &rarr; Indicate Texas Instrument signal is set to True. Default is False (meaning Motorola signal conventions).
- crc &rarr; Define the CRC using a polynomial specifier (a binary definition of the polynome (example: 1011 =x^3+x+1). First and last bit must be 1). Default is None (no crc used).

### deinit:
Turn off the SPI bus and reset all parameters to default.

### recv:
Receive data on the bus. Parameters are:
- recv &rarr; Number of byte to receive if it's an integer, if you have given a buffer, the data will be written in the buffer.
- timeout &rarr; The timeout to wait for the receive in ms. Default is 5000.
If recv is a buffer, the data receive will be stored directly in it, otherwise, you must use this function as a function that returns a buffer.

### send:
Send data on the bus. Parameters are:
- send &rarr; The data that will be send. It must be either an integer or a buffer.
- timeout &rarr; The timeout to wait for the send in ms. Default is 5000.

### send\_recv:
Send and receive data on the bus at the same time. Parameters are:
- send &rarr; The data that will be send. It must be either an integer or a buffer.
- recv &rarr; A buffer that will be used to stored the receive data. Default is None.
- timeout &rarr; The timeout to wait for the receive in ms. Default is 5000.
If recv is not specify (left to None), the function must be use a function that returns a buffer.


<a id="UART"></a>
## UART

### pyb.UART: int &rarr; int &rarr; int &rarr; int &rarr; int &rarr; int &rarr; int &rarr; int &rarr; int &rarr; UART
Create an UART object. Parameters are:
- bus &rarr; The pins on which the UART will be configure.
- baudrate &rarr; The clock rate.
- bits &rarr; Number of bit per character. Can be 7, 8 or 9.
- parity &rarr; The detection use to check for integrity during the transmission. Can be None, 0 (even) or 1 (odd).
- stop &rarr; Number of stop bits. Can be 1 or 2.
- flow &rarr; St the flow control type. Can be:
	- 0
	- UART.RTS
	- UART.CTS
	- UART.RTS | UART.CTS
- timeout &rarr; The timeout to wait for writing and reading the first character.
- timeout\_char &rarr; Timeout to wait between each character while writing or reading.
- read\_buf\_len &rarr; The caracter length of the read buffer. Set it to 0 to disable it.
You may only specify the pins to use, but you'll need to use the init method before using the UART port.

Methods are:

### init:
Initialise the UART port with the specify options. Parameters are:
- baudrate &rarr; The clock rate.
- bits &rarr; Number of bit per character. Can be 7, 8 or 9. Default is 8.
- parity &rarr; The detection use to check for integrity during the transmission. Can be None, 0 (even) or 1 (odd). Default is None.
- stop &rarr; Number of stop bits. Can be 1 or 2. Default is 1.
- flow &rarr; St the flow control type. Can be:
	- 0
	- UART.RTS
	- UART.CTS
	- UART.RTS | UART.CTS
Default is 0.
- timeout &rarr; The timeout to wait for writing and reading the first character. Default is 0.
- timeout\_char &rarr; Timeout to wait between each character while writing or reading. Default is 0.
- read\_buf\_len &rarr; The caracter length of the read buffer. Set it to 0 to disable it. Default is 64.

### deinit:
Turn off the UART port. Reset all value to default value before doing so.

### any:
Returns the number of bytes wainting (if none is waiting, it will return 0).

### read:
Read character that are waiting. Parameter is:
- nbytes &rarr; If specified, the reading will be at most nbytes bytes. If the buffer use to store the return value has nbytes available, it returns immediately the value, otherwise it will return it only when the buffer is full or timeout elapses. If not specified, return as much data as possible and returns the data only when timeout has elapsed. (It may be a bit tricky, feel free to ask for help).

### readchar:
Receive a single character on the bus. The character will be return as an integer (ASCII code). Returns -1 on timeout.

### readinto:
Read bytes into the buffer specified in parameter. Parameters are:
- buf &rarr; The buffer in which the data will be stored.
- nbytes &rarr; Number of byte to be read. If not specified, it will read at most len(buf) bytes.
Return the number of byte read and stored or None on timeout.

### readline:
Read a line (must end by a newline character '\r'). If a '\r' character exists, the line is return immediately. If the timeout elapses, all the data available will be return. If no data is available, it will return None.

### write:
Write the buffer given in parameter to the bus. If the characters are 7 or 8 bits wide, the each byte is one character, if they are 9 bits wide, then two bytes are used for each character (so the buffer must have an even size). Parameter is:
- buf &rarr; The buffer on which the data to write is.
Return the number of byte written. If timeout occurs with no byte written, it returns None.

### writechar:
Write a signle character on the bus. Parameter is:
- char &rarr; The character to write. It must be an interger (ASCII code).

### sendbreak:
Send a break condition on the bus, thus driving the bus low for a duration of 13 bits.


<a id="Extra"></a>
# Extra classes


<a id="Timerchannel"></a>
## Timerchannel

### pyb.Timer.channel: int &rarr; int &rarr; Timerchannel
Create a timerchannel object. Parameters are:
- mode &rarr; Mode on which the timer will be, it can be Timer:
	- PWM &rarr; active high.
	- PMW\_INVERTED &rarr; active low.
	- OC\_TIMING &rarr; no pin is driven.
	- OC\_ACTIVE &rarr; pin active if a compare match occurs.
	- OC\_INACTIVE &rarr; pin will be inactive if a compare match occurs.
	- OC\_TOGGLE &rarr; pin toggle if a compare match occurs.
	- OC\_FORCED\_ACTIVE &rarr; forced active (compare match ignored).
	- OC\_FORCED\_INACTIVE &rarr; forced inactive (compare match ignored).
	- IC &rarr; Input Capture mode.
	- ENC\_A &rarr; Encoder mode, counter update when CH1 changes.
	- ENC\_B &rarr; Encoder mode, counter update when CH2 changes.
	- ENC\_AB &rarr; Encoder mode, counter update when CH1 or CH2 changes.
- callback &rarr; Callback function (see callback method).
- pin &rarr; Either None or a Pin. If specified (and not None) this will cause the alternate function of the the indicated pin to be configured for this timer channel. An error will be raised if the pin doesn’t support any alternate functions for this timer channel.

They are other keyword depending of the mode:
- PWM
	- pulse\_width &rarr; determines the initial pusle width value to use.
	- pusle\_width\_percent &rarr; determines the initial pulse width percentage to use.
- OC
	- compare &rarr; determines the initial value of the compare register.
	- polarity:
		- Timer.HIGH &rarr; active high.
		- Timer.LOW &rarr; active low.
- IC
	- polarity:
		- Timer.RISING &rarr; capture on rising edge.
		- Timer.FALLING &rarr; capture on falling edge.
		- Timer.BOTH &rarr; capture on both edge.

The methods are:

### callback:
Define the callback function, if set to None, it will be disable. The parameter is:
- fun &rarr; the callback function, it get only one parameter which is the timer object.

### capture:
Get or set the capture value associated with a channel. Use it for input mode. Parameter is:
- value &rarr; The value that will be set. If none is given, it will get the value of the channel.

### compare:
Get or set the compare value associated with a channel. Use it for output mode. Parameter is:
- value &rarr; The value that will be set. If none is given, it will get the value of the channel.

### pulse\_width:
Get or set the pulse width value associated with a channel. Use it for PWM mode. Parameter is:
- value &rarr; The value that will be set. If none is given, it will get the value of the channel.

### pulse\_width\_percent:
Get or set the pulse width percentage associated with a channel. The value is a number between 0 and 100. Parameter is:
- value &rarr; The value of the percent that will be set. If none is given, it will get the current value.


<a id="RTC"></a>
## RTC

### pyb.RTC
Allow the user to manipulate the Real Time Clock inside the board.

The methods are:

### datetime:
Return or set (year, month, day, day of the week, hours, minutes, secondes, milliseconds).

### wakeup(timeout, callback=None):
Set the RTC wakeup timer to trigger at every timeout given in parameter. Parameters are:
- timeout &rarr; time of timeout in ms.
- callback &rarr; function to execute at each trigger. Default is None.
This is another way to wake the board from a sleep state.

### info:
Get the information about the startup time and reset source.

### calibration:
Get or set the RTC calibration.


<a id="ExtInt"></a>
## ExtInt

### pyb.ExtInt: str &rarr; int &rarr; int &rarr; (ExtInt &rarr; void) &rarr; ExtInt
Create an external interrupt on the pin enter as a str. The first int is the trigger and can be:
- pyb.ExtInt.IRQ\_RISING &rarr; trigger on rising edge.
- pyb.ExtInt.IRQ\_FALLING &rarr; trigger on falling edge.
- pyb.ExtInt.IRQ\_RISING_FALLING &rarr; trigger on a change of state.
the second int is the pull of the pin and can be:
- pyb.ExtInt.PULL_NONE
- pyb.ExtInt.PULL_UP
- pyb.ExtInt.PULL_DOWN
The function is the callback function that'll be use when the interrupt is trigger

The methods are:

### enable:
Enable the external interrupt.

### disable:
Disable the external interrupt.

### line:
Return the pin number.


<a id="CAN"></a>
## CAN

### pyb.CAN: int/str &rarr; CAN
Create a CAN object on the given bus (as an integer or string).
For the integer, it can be either 1 or 2 and the string either 'YA' or 'YB'. (You should prefer using integer).

The methods are:

### init:
Initialise the CAN. It has a few parameters:
- mode &rarr; It can be:
	- NORMAL
	- LOOPBACK
	- SILENT
	- SILENT\_LOOPBACK
- prescaler &rarr; integer by which the clock input of the CAN will be devided to generate the nominal bit time quanta (default is 100).
- sjw &rarr; resynchronisation jump width. Can be from 1 to 4. Default is 1.
- bs1 &rarr; define the location of the sample point in units of the time quanta for nominal bit. Can be from 1 to 16. Default is 6.
- bs2 &rarr; define the location of the transmit point in units of the time quanta for nominal bit. Can be from 1 to 8. Default is 8.
- auto\_restart &rarr; sets whether the controller will automatically try and restart communications after entering the bus-off state. Default False.
- baudrate &rarr; if not 0, the function will calculate (if possible) the CAN nominal bit time (overrinding prescaler, bs1 and bs2) that satisfies the baudrate and the sample\_point. Default 0.
- sample\_point &rarr; Given a percentage of the nominal bit time, it specifies the position of the bit sample with respet to the whole nominal bit time. Default 75.
- num\_filter\_bank &rarr; number of banks assigned to CAN(1), the reste of the 28 will be assigned to CAN(2).
The other parameters are the same but with brs\_ before them and are use for the CAN FD. Default 14.

### deinit:
Turn off the CAN bus.

### restart:
Force a software restart of the CAN without resetting the configuration.

### state:
Return the state of the controller. Value can be:
- CAN.STOPPED &rarr; off and reset
- CAN.ERROR\_ACTIVE &rarr; on and both TEC and REC are less than 96.
- CAN.ERROR\_WARNING &rarr; on and TEC or REC is 96 or more.
- CAN.ERROR\_PASSIVE &rarr; on and TEC or REC is 128 or more.
- CAN.BUS\_OFF &rarr; on and TEC is over 255.

### info
Get information about the controller’s error states and TX and RX buffers. It will return them in a list like:
```
[TEC, REC, num_of_ERROR_WARNING, num_of_ERROR_PASSIVE, num_of_BUS_OFF, TX, RX0, RX1]
```

### setfilter:
This function configure a filter bank. The different parameters are:
- bank &rarr; a CAN controller filter bank (or CAN FD filter index) it's an integer from 0 to num\_filter\_banks -1.
- mode &rarr; the mode on which the filter should operate, it can be:
	- CAN.LIST16 (Four 16 bit ids that will be accepted).
	- CAN.LIST32 (Two 32 bit ids that will be accepted).
	- CAN.MASK16 (Two 16 bit id/mask pairs. The first pair, 1 and 3 will accept all ids that have bit 0 = 1 and bit 1 = 0. The second pair, 4 and 4, will accept all ids that have bit 2 = 1).
	- CAN.MASK32 (same but with 32 bit id/mask pairs).
for CAN.
	- CAN.RANGE (Two ids that represent a range of accepted ids).
	- CAN.DUAL (Two ids that will be accepted).
	- CAN.MASK (One filter ID and a mask).
for CAN FD.

- rtr (ignore for CAN FD) &rarr; an array of booleans that states if a filter should accept a remote transmission request message. The array has different size depending on the mode:
	- CAN.LIST16 &rarr; 4.
	- CAN.LIST32 &rarr; 2.
	- CAN.MASK16 &rarr; 2.
	- CAN.MASK32 &rarr; 1.
- extframe &rarr; a boolean that, if set to True, gives the frame a 29 bits identifier (otherwise it would be the classical 11 bits).

### clearfilter:
It clears and disables a filter bank. Parameters are:
- bank &rarr; the CAN controller filter bank or the CAN FD filter index.
- extframe (use for CAN FD) &rarr; if True, it will clear an extended filter otherwise, it will clear a standard one.

### any:
Return a boolean that indicate if there is anything in the given FIFO. Parameter is:
- fifo &rarr; an integer that represent the FIFO you want to check.

### recv:
Use to receive data on the bus, it will return a tuple:
- ID of the message.
- is the message ID extended.
- is the message an RTR message.
- the FMI (Filter Match Index) value.
- an array containing the data receive.
Parameters are:
- fifo &rarr; the FIFO you want to check.
- list &rarr; optional, if None, it create a new tuple, otherwise, it must be a five-length tuple with the corresponding output type.
- timeout &rarr; time the pin will wait for the receive (in ms).

### send:
Send a message on the bus. Parameters are:
- data &rarr; the data that will be send (either an integer or a buffer object).
- id &rarr; the id of the message to be sent.
- timeout &rarr; time the pin will wait for the transmit (in ms).
- rtr &rarr; a boolean that specifies if the message will be send as a RTR request.
- extframe &rarr; a boolean that, if set to True, gives the frame a 29 bits identifier (otherwise it would be the classical 11 bits).
- fdf (CAN FD only) &rarr; if set to True, it will have a FD frame format (meaning it will support data payloads up to 64 bytes).
- brs (CAN FD only) &rarr; if set to True, the bitrate switching mode is enabled, in which the data phase is transmitted at a different bitrate (used if brs has been modified in init).

### rxcallback:
Give the user the possibility to register a callback function on a given fifo. It has two parameters:
- fifo &rarr; the receiving fifo.
- fun &rarr; the function executed when the fifo becomes non empty.
In general, the callback function must necessarily get two parameters which are:
- bus &rarr; the CAN object itself.
- reason &rarr; the reason of callback that can be:
	- 0 &rarr; A message has been accepted into an empty FIFO.
	- 1 &rarr; The FIFO is full.
	- 2 &rarr; A message has been lost because the FIFO was full.