# Library

All the PY file are some "libraries" that may be use in your code.

They are not really libraries but part of code you may need, feel free to use them.

The board comes already with some function that allow the user to code.
One of this function (pyb.info) will give you adresses as well as the memory. To be more precise:


ID -> ID of the board

DEVID -> the device ID

REVID -> the device revision
S, H, P1 and P2 -> indicate the adresses of the flash memory and RAM memory

\_sstack and \_estack -> the adresses of Start and End of the stack

\_etext, \_sidata, \_sdata, edata, sbss, ebss -> adresses of Start and End of the executable data, initialized data and uninitialized data

\_ram start, \_heap start, \_heap end, \_ram end -> adresses of Start and End of the RAM and HEAP

qstr -> indicate the numbre of pools, of qstrings, number of byte used to store string and number of byte used for qstrings overall

GC -> memory management of the Garbage Collector: total size, used and usage

LFS free -> indicate the free space in the LittleFS for file storage inside the firmware


If you have any question about this, do not hesitate to ask a student of a teacher.

Here's a small summary of the function available:


pyb.delay: int -> int, wait for n milliseconds

pyb.millis: void -> int, gives the number of milliseconds since last hard reset

pyb.Switch: void -> Switch, create a switch, it has two main methods: value -> return True or False depending of the state of the switch, callback -> allow the user to define a callback function (exemple in the library)

pyb.LED: int -> LED, create a LED object associated to the integer send (pyb.LED(1) will create the object LED for the user LED 1). It has different methods: on -> turn on the LED, off -> turn off the LED, toggle -> change the state of the LED, intensity(n) -> set the intensity of the LED to n (do not work on our board as far as I know)

pyb.Pin: str -> Pin, create a Pin object associated to the pin entered as a string. Different methods can be used: value -> return 0 or 1 depending on the state of the pin, value({0,1}), set the pin to high (1) or low (0), init(mode, pull) where the mode can be pyb.Pin.IN (input pin), pyb.Pin.OUT PP (output in push-pull), pyb.Pin.OUT OD (output in open-drain), pyb.Pin.ALT (alternate, use for I2C and SPI for example) and pull can be pyb.Pin.PULL UP, pyb.Pin.PULL DOWN or None.

pyb.Pin: str -> int -> int -> Pin, create a Pin object associated to the pin entered as a string with the mode enter as the first int (use the macro describe above) and the pull define as the second int (same)

