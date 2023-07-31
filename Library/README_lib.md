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
### pyb.delay: int -> void
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


<a id="Usual"></a>
# Usual classes


<a id="Pin"></a>
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

### pyb.ADC: str -> ADC
Create an analog to digital converter associated to the pin entered as a string.

The methods are:

### read:
Read the analog value of the pin and return it.

### read\_timed:
It read the analog values into the buf at a rate set by freq. So it has two parameters:
- buf -> an array or a bytearray.
- freq -> an integer (in Hz).

### read\_timed\_multi:
It is basically the previous methods but use for more than one ADC pin. The parameters are:
- ADC -> a tuple of ADC pin.
- buf -> a tuple of array or bytearray.
- freq -> an integer (in Hz).
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

### pyb.DAC: str -> DAC
Create a digital to analog converter associated to the pin entered as a string.

The methods are:

### init:
Reinitialise the DAC with a new bit and buffering. The parameters are:
- bit -> may be 8 or 12.
- buffering -> may be None, True or False (None -> default, True -> enable, False -> disable).

### deinit:
Free the ressources link to the DAC.

### write:
Write a value in the DAC. Only one parameter:
- value -> must be between 0 and 4095.

### write\_timed:
Write a serie of value in the DAC at a given frequency. Parameters are:
- buf -> thing that will be written in the DAC (either an array or a bytearray).
- freq -> the frequency rate used (in Hz).

### write\_timed\_multi:
Same as before but with multiple DAC channel. Same parameters as before too but buf is an array of array or array of bytearray this time.

### triangle:
Generate a triangular wave (the amplitude will probably be either 3.3V or 5V). The parameter is:
- frequency -> frequency of the wave.

### noise:
generate a noise signal on the DAC.


<a id="Timer"></a>
## Timer

### pyb.Timer: int -> Timer
Create a timer object, the integer in parameter can be 1 to 14 (you may need to look the board documentation to be sure to use the correct integer).

The methods are:

### init:
Initialise the timer. Initialisation must be made either by frequency (in Hz) with timer.init(freq = ...) or by prescaler and period (much more complex) with timer.init(prescaler = ..., period = ...).
Note that there are other parameters that may be initialise, but there are specific methods to do so.
It also has the parameter brk which can be:
- Timer.BRK\_OFF -> kill the output when the timer is off.
- Timer.BRK\_LOW -> kill the output when the pin is set low.
- Timer.BRK\_HIGH -> kill the output when the pin is set high.

### deinit:
Deinitialises the timer (set to default every parameters).

### callback:
Allow user to make a callback function. Parameter is:
- fun -> if None, callback will be disable, otherwise it will be the function use.

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

## pyb.LED: int -> LED
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

### pyb.Switch: void -> Switch
Create a switch object.

The methods are:

### \_\_call\_\_:
Call switch object directly to get its state.

### value:
Return True or False depending of the state of the switch. (not really sure about the difference with \_\_call\_\_).

### callback:
Allow the user to define a callback function (exemple in the library).


<a id="I2C"></a>
## I2C

### pyb.I2C: int -> int -> int -> bool -> bool -> I2C
Create an I2C object on the bus given in argument.
Parameters are:
- bus -> The bus on which the I2C will be define.
- mode -> The mode on which the I2C bus will work, can be:
	- I2C.CONTROLLER
	- I2C.PERIPHERAL
- addr -> The 7-bit address of the peripheric (use only in peripheral). Default is 0x12.
- baudrate -> The SCL clock rate (use only in controller). Default is 400000.
- gencall -> If True, the bus will support general call mode. Default is False.
- dma -> if True, DMA will be allow for the I2C transfers. Default is False.

You may at first only use pyb.I2C as an int -> I2C function with only the bus specify and the use the method init with the other parameters.

The methods are:

### init:
Initialise the I2C bus. Parameters are:
- mode -> The mode on which the I2C bus will work, can be:
	- I2C.CONTROLLER
	- I2C.PERIPHERAL
- addr -> The 7-bit address of the peripheric (use only in peripheral).
- baudrate -> The SCL clock rate (use only in controller).
- gencall -> If True, the bus will support general call mode.
- dma -> If True, DMA will be allow for the I2C transfers.

### deinit:
Turn off the I2C bus. Reset all parameters set for the bus.

### is\_ready:
Check if the I2C device responds to the given address. Parameter is:
addr -> address that should be tested.
Will only work if the I2C bus has been set to controller.

### mem\_ready:
Read the memory of an I2C device. Parameters are:
- data -> Can be:
	- An int -> number of byte to read.
	- A buffer -> will be use to store the data read.
- addr -> The I2C device address.
- memaddr -> The memory location within the I2C device.
- timeout -> Timeout to wait for the read in ms. Default is 5000.
- addr\_size -> Select the width of memaddr. Can either be 8 or 16. Default is 8.
It will return the read data. Will only work if the I2C bus has been set to controller.

### mem\_write:
Write to the memory of an I2C device. Parameters are:
- data -> Can be an integer or a buffer to write from.
- addr -> The I2C device address.
- memaddr -> The memory location within the I2C device.
- timeout -> Timeout to wait for the write. Default is 5000.
- addr\_size -> Select the width of memaddr. Can either be 8 or 16. Default is 8.
Will only work if the I2C bus has been set to controller.

### recv:
Receive the data on the bus. Parameters are:
- recv -> Can be an integer (number of byte received) or a buffer where the data will be stored.
- addr -> The address to receive from (only in controller mode).
- timeout -> Timeout to wait for the receive in ms. Default is 5000.
It will return a buffer if an integer has been pass as recv, otherwise the buffer given in parameter will be modified.

### send:
Send data on the bus. Parameters are:
- send -> The data to send. Can be an integer or a buffer.
- addr -> The address where you want to send. Only needed in controller mode. Default is 0x00.
- timeout -> Timeout to wait for the send in ms. Default is 5000.

### scan:
Return a list of the all the I2C addresses (from 0x01 to 0x7f) that respond. Will only work in controller mode.


<a id="SPI"></a>
## SPI

### pyb.SPI: int -> int -> int -> int -> int -> int -> int -> int -> bool -> bool -> SPI
Create a SPI object. Parameters are:



<a id="UART"></a>
## UART



<a id="Extra"></a>
# Extra classes


<a id="Timerchannel"></a>
## Timerchannel

### pyb.Timer.channel: int -> int -> Timerchannel
Create a timerchannel object. Parameters are:
- mode -> Mode on which the timer will be, it can be Timer:
	- PWM -> active high.
	- PMW\_INVERTED -> active low.
	- OC\_TIMING -> no pin is driven.
	- OC\_ACTIVE -> pin active if a compare match occurs.
	- OC\_INACTIVE -> pin will be inactive if a compare match occurs.
	- OC\_TOGGLE -> pin toggle if a compare match occurs.
	- OC\_FORCED\_ACTIVE -> forced active (compare match ignored).
	- OC\_FORCED\_INACTIVE -> forced inactive (compare match ignored).
	- IC -> Input Capture mode.
	- ENC\_A -> Encoder mode, counter update when CH1 changes.
	- ENC\_B -> Encoder mode, counter update when CH2 changes.
	- ENC\_AB -> Encoder mode, counter update when CH1 or CH2 changes.
- callback -> Callback function (see callback method).
- pin -> Either None or a Pin. If specified (and not None) this will cause the alternate function of the the indicated pin to be configured for this timer channel. An error will be raised if the pin doesn’t support any alternate functions for this timer channel.

They are other keyword depending of the mode:
- PWM
	- pulse\_width -> determines the initial pusle width value to use.
	- pusle\_width\_percent -> determines the initial pulse width percentage to use.
- OC
	- compare -> determines the initial value of the compare register.
	- polarity:
		- Timer.HIGH -> active high.
		- Timer.LOW -> active low.
- IC
	- polarity:
		- Timer.RISING -> capture on rising edge.
		- Timer.FALLING -> capture on falling edge.
		- Timer.BOTH -> capture on both edge.

The methods are:

### callback:
Define the callback function, if set to None, it will be disable. The parameter is:
- fun -> the callback function, it get only one parameter which is the timer object.

### capture:
Get or set the capture value associated with a channel. Use it for input mode. Parameter is:
- value -> The value that will be set. If none is given, it will get the value of the channel.

### compare:
Get or set the compare value associated with a channel. Use it for output mode. Parameter is:
- value -> The value that will be set. If none is given, it will get the value of the channel.

### pulse\_width:
Get or set the pulse width value associated with a channel. Use it for PWM mode. Parameter is:
- value -> The value that will be set. If none is given, it will get the value of the channel.

### pulse\_width\_percent:
Get or set the pulse width percentage associated with a channel. The value is a number between 0 and 100. Parameter is:
- value -> The value of the percent that will be set. If none is given, it will get the current value.


<a id="RTC"></a>
## RTC

### pyb.RTC
Allow the user to manipulate the Real Time Clock inside the board.

The methods are:

### datetime:
Return or set (year, month, day, day of the week, hours, minutes, secondes, milliseconds).

### wakeup(timeout, callback=None):
Set the RTC wakeup timer to trigger at every timeout given in parameter. Parameters are:
- timeout -> time of timeout in ms.
- callback -> function to execute at each trigger. Default is None.
This is another way to wake the board from a sleep state.

### info:
Get the information about the startup time and reset source.

### calibration:
Get or set the RTC calibration.


<a id="ExtInt"></a>
## ExtInt

### pyb.ExtInt: str -> int -> int -> (ExtInt -> void) -> ExtInt
Create an external interrupt on the pin enter as a str. The first int is the trigger and can be:
- pyb.ExtInt.IRQ\_RISING -> trigger on rising edge.
- pyb.ExtInt.IRQ\_FALLING -> trigger on falling edge.
- pyb.ExtInt.IRQ\_RISING_FALLING -> trigger on a change of state.
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

### pyb.CAN: int/str -> CAN
Create a CAN object on the given bus (as an integer or string).
For the integer, it can be either 1 or 2 and the string either 'YA' or 'YB'. (You should prefer using integer).

The methods are:

### init:
Initialise the CAN. It has a few parameters:
- mode -> It can be:
	- NORMAL
	- LOOPBACK
	- SILENT
	- SILENT\_LOOPBACK
- prescaler -> integer by which the clock input of the CAN will be devided to generate the nominal bit time quanta (default is 100).
- sjw -> resynchronisation jump width. Can be from 1 to 4. Default is 1.
- bs1 -> define the location of the sample point in units of the time quanta for nominal bit. Can be from 1 to 16. Default is 6.
- bs2 -> define the location of the transmit point in units of the time quanta for nominal bit. Can be from 1 to 8. Default is 8.
- auto\_restart -> sets whether the controller will automatically try and restart communications after entering the bus-off state. Default False.
- baudrate -> if not 0, the function will calculate (if possible) the CAN nominal bit time (overrinding prescaler, bs1 and bs2) that satisfies the baudrate and the sample\_point. Default 0.
- sample\_point -> Given a percentage of the nominal bit time, it specifies the position of the bit sample with respet to the whole nominal bit time. Default 75.
- num\_filter\_bank -> number of banks assigned to CAN(1), the reste of the 28 will be assigned to CAN(2).
The other parameters are the same but with brs\_ before them and are use for the CAN FD. Default 14.

### deinit:
Turn off the CAN bus.

### restart:
Force a software restart of the CAN without resetting the configuration.

### state:
Return the state of the controller. Value can be:
- CAN.STOPPED -> off and reset
- CAN.ERROR\_ACTIVE -> on and both TEC and REC are less than 96.
- CAN.ERROR\_WARNING -> on and TEC or REC is 96 or more.
- CAN.ERROR\_PASSIVE -> on and TEC or REC is 128 or more.
- CAN.BUS\_OFF -> on and TEC is over 255.

### info
Get information about the controller’s error states and TX and RX buffers. It will return them in a list like:
```
[TEC, REC, num_of_ERROR_WARNING, num_of_ERROR_PASSIVE, num_of_BUS_OFF, TX, RX0, RX1]
```

### setfilter:
This function configure a filter bank. The different parameters are:
- bank -> a CAN controller filter bank (or CAN FD filter index) it's an integer from 0 to num\_filter\_banks -1.
- mode -> the mode on which the filter should operate, it can be:
	- CAN.LIST16 (Four 16 bit ids that will be accepted).
	- CAN.LIST32 (Two 32 bit ids that will be accepted).
	- CAN.MASK16 (Two 16 bit id/mask pairs. The first pair, 1 and 3 will accept all ids that have bit 0 = 1 and bit 1 = 0. The second pair, 4 and 4, will accept all ids that have bit 2 = 1).
	- CAN.MASK32 (same but with 32 bit id/mask pairs).
for CAN.
	- CAN.RANGE (Two ids that represent a range of accepted ids).
	- CAN.DUAL (Two ids that will be accepted).
	- CAN.MASK (One filter ID and a mask).
for CAN FD.

- rtr (ignore for CAN FD) -> an array of booleans that states if a filter should accept a remote transmission request message. The array has different size depending on the mode:
	- CAN.LIST16 -> 4.
	- CAN.LIST32 -> 2.
	- CAN.MASK16 -> 2.
	- CAN.MASK32 -> 1.
- extframe -> a boolean that, if set to True, gives the frame a 29 bits identifier (otherwise it would be the classical 11 bits).

### clearfilter:
It clears and disables a filter bank. Parameters are:
- bank -> the CAN controller filter bank or the CAN FD filter index.
- extframe (use for CAN FD) -> if True, it will clear an extended filter otherwise, it will clear a standard one.

### any:
Return a boolean that indicate if there is anything in the given FIFO. Parameter is:
- fifo -> an integer that represent the FIFO you want to check.

### recv:
Use to receive data on the bus, it will return a tuple:
- ID of the message.
- is the message ID extended.
- is the message an RTR message.
- the FMI (Filter Match Index) value.
- an array containing the data receive.
Parameters are:
- fifo -> the FIFO you want to check.
- list -> optional, if None, it create a new tuple, otherwise, it must be a five-length tuple with the corresponding output type.
- timeout -> time the pin will wait for the receive (in ms).

### send:
Send a message on the bus. Parameters are:
- data -> the data that will be send (either an integer or a buffer object).
- id -> the id of the message to be sent.
- timeout -> time the pin will wait for the transmit (in ms).
- rtr -> a boolean that specifies if the message will be send as a RTR request.
- extframe -> a boolean that, if set to True, gives the frame a 29 bits identifier (otherwise it would be the classical 11 bits).
- fdf (CAN FD only) -> if set to True, it will have a FD frame format (meaning it will support data payloads up to 64 bytes).
- brs (CAN FD only) -> if set to True, the bitrate switching mode is enabled, in which the data phase is transmitted at a different bitrate (used if brs has been modified in init).

### rxcallback:
Give the user the possibility to register a callback function on a given fifo. It has two parameters:
- fifo -> the receiving fifo.
- fun -> the function executed when the fifo becomes non empty.
In general, the callback function must necessarily get two parameters which are:
- bus -> the CAN object itself.
- reason -> the reason of callback that can be:
	- 0 -> A message has been accepted into an empty FIFO.
	- 1 -> The FIFO is full.
	- 2 -> A message has been lost because the FIFO was full.