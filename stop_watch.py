import sys
import time
import seven_segment

second_left = eval(input("please enter your countdown time (in seconds):"))

try:
    while True:
        # clear the screen by printing new lines
        print('\n'*15)

        # Get hours/minutes/seconds from second_left
        hours = str(second_left // 3600)
        minutes = str((second_left % 3600) // 60)
        seconds = str(second_left % 60)

        # Get the seven segment digit strings
        h = seven_segment.get_sevseg_number(hours, 2)
        h_top, h_mid, h_bottom = h.splitlines()
        m = seven_segment.get_sevseg_number(minutes, 2)
        m_top, m_mid, m_bottom = m.splitlines()
        s = seven_segment.get_sevseg_number(seconds, 2)
        s_top, s_mid, s_bottom = s.splitlines()

        # Display digits
        print(h_top + '     ' + m_top + '     ' + s_top)
        print(h_mid + '  *  ' + m_mid + '  *  ' + s_mid)
        print(h_bottom + '  *  ' + m_bottom + '  *  ' + s_bottom)

        if second_left == 0:
            print()
            break

        print()
        print("Press Crtl-C to quit.")

        time.sleep(1)
        second_left -= 1

except KeyboardInterrupt:
    print("You've quited your stop watch.")
    sys.exit()







