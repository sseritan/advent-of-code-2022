"""Day 6
"""

import sys

# Defaults for Part 2
def find_packet_start(fname: str = 'input.txt', header_size:int = 14) -> None:
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Run through multiple lines (for example)
    for l in lines:
        header = ''

        packet_start = -1
        for i, c in enumerate(l):
            try:
                repeat_index = header.index(c)
                
                # If we found one, skip to the repeat
                header = header[repeat_index+1:] + c
            except ValueError:
                # Not a repeat, add and check if done
                header += c

                if len(header) == header_size:
                    packet_start = i+1
                    break

        print(f'Packet starts at {packet_start}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_packet_start(sys.argv[1])
    elif len(sys.argv) == 3:
        find_packet_start(sys.argv[1], header_size=sys.argv[2])
    else:
        find_packet_start()