# The file can also be run on online platforms like google colab.

# initializing main memory and control stack
main_memory = []
control_stack = []

while k:
    print('CPU executing {}th step of main function'.format(k))
    time.sleep(2)
    print('Would you like to issue an interrupt?')

    # Asks user if they want to issue an interrupt
    try:
        val = int(input('Enter 1(yes) or 0(no): '))
    
    # If user enters invalid character
    except Exception:
        print('Please enter a valid number.\n Interrupt not issued by I/O')
        time.sleep(2)

    # Interrupt is issued for any non-zero input by user
    else:
        if val:
            print('Interrupt Acknowledged\n\t PSW and PC sent to control stack and address bus is available to process interrupt.')
            control_stack.append(k)
            fn = input('Enter the fuction to be excecuted: ')
            # updating the main memory
            main_memory.append(fn)
            print(fn,'has been excecuted\n\t Restoring original PC ...')

            # retrieving the original PC
            k = control_stack.pop()
            time.sleep(2.5)
    
    # incrementing program counter
    k+=1
    # We are randomly executing 6 functions of the main memory by CPU
    # keep a number of your choice, greater than 6
    if k>=12:
        break
