from machine import UART

uart1 = UART(1, baudrate=9600, tx=4, rx=17)



track1 = bytes([0x7E, 0xFF, 0x06, 0x12, 0x00, 0x00, 0x1, 0xFE, 0xE8, 0xEF])
track2 = bytes([0x7E, 0xFF, 0x06, 0x12, 0x00, 0x00, 0x2, 0xFE, 0xE7, 0xEF])


print("UART1")

       
def offensive () :
    uart1.write(track1)
def defensive () :
    uart1.write(track2)

    
uart1.write(track2)
  