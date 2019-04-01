#!/usr/bin/env python3


def main():
    network_lists =[]
    with open('driverip.txt', 'r') as _f:
        for line in _f:
            network_lists.append(line.rstrip().split(" "))

    print(network_lists)

    for driverandip in network_lists:
        print("ssh to " + driverandip[0] + " with ip" + driverandip[1])

main()
