#!/usr/bin/python3
##
## EPITECH PROJECT, 2020
## 202unsold_2019
## File description:
## 202unsold
##

import sys, os
import time
import math
import statistics

def printUsage():
    print("SYNOPSIS\n\t", sys.argv[0], " period\n\nDESCRIPTION\n\tperiod\tthe number of days defining a period", sep='')

def error_gestion():
    if ((len(sys.argv) == 2 and sys.argv[1].isdigit() == False) or int(sys.argv[1]) == 0):
        raise ValueError("Error: input must be a positive number")

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    return (float(n))

def get_input_value(command):
    temperature = is_integer(command)
    if (temperature == False):
        print ("Error : Please give a temperature")
        return (get_command())
    return (temperature)

def get_command():
    command = input()
    if (command == "STOP"):
        return ("STOP")
    return (get_input_value(command))

def calc_golbal_average(list_temperature, periode):
    start = len(list_temperature) - periode
    mean = 0
    for x in range(start, len(list_temperature)):
        tmp = list_temperature[x] - list_temperature[x - 1]
        if (tmp < 0):
            mean += 0
        else:
            mean += tmp
    return (mean / periode)

def calc_mean_of_n_day(list_temperature, periode):
    start = len(list_temperature) - periode
    mean = 0
    for x in range (start, len(list_temperature)):
        mean += list_temperature[x]
    return (mean / periode)

def calc_standard_deviation(list_temperature, periode):
    mean = calc_mean_of_n_day(list_temperature, periode)
    start = len(list_temperature) - periode
    std = 0
    for x in range(start, len(list_temperature)):
        std += (list_temperature[x] - mean) ** 2
    variance = (1 / periode) * std
    std = math.sqrt(variance)
    return (std)

def calc_relative_temperature_evolution(list_temperature, periode, va):
    pos = len(list_temperature) - (periode + 1)
    vd = list_temperature[pos]
    print("va = ", va)
    print("vd = ", vd)
    res = ((va - vd) / vd) * 100
    return (res)

def calculate_last_rte(list_temperature, periode):
    pos = len(list_temperature) - 1 - (periode + 1)
    if (pos < 0):
        return (0)
    vd = list_temperature[pos]
    va = list_temperature[len(list_temperature) - 2]
    res = ((va - vd) / vd) * 100
    return (res)

def check_occurs(list_temperature, relative_evolution, periode):
    if (len(list_temperature) - 1 <= periode):
        return (False)
    last = calculate_last_rte(list_temperature, periode)
    if (((last < 0 and relative_evolution >= 0) or (last >= 0 and relative_evolution < 0)) and last != 0):
        return (True)
    return (False)

def calc_output_from_list(list_temperature, periode, new_temperature, nb_occurs):
    length = len(list_temperature)
    if (length < periode):
        print("g=nan\tr=nan%\ts=nan")
        return (False)
    elif (length == periode):
        std = calc_standard_deviation(list_temperature, periode)
        print("g=nan\tr=nan%\ts={:.2f}".format(std))
        return (False)
    global_average = calc_golbal_average(list_temperature, periode)
    relative_evolution = calc_relative_temperature_evolution(list_temperature, periode, new_temperature)
    std = calc_standard_deviation(list_temperature, periode)
    print("g={:.2f}\tr={:.0f}%\ts={:.2f}".format(global_average,relative_evolution, std), end="")
    if (check_occurs(list_temperature, relative_evolution, periode) == True) :
        print("\ta switch occurs")
        nb_occurs += 1
    else :
        print("")
    return (nb_occurs)

def start_groundhog():
    error_gestion()
    list_temperature = list()
    periode = int(sys.argv[1])
    nb_occurs = 0
    new_temperature = get_command()

    while (new_temperature != "STOP"):
        list_temperature.append(new_temperature)
        nb_occurs = calc_output_from_list(list_temperature, periode, new_temperature, nb_occurs)
        new_temperature = get_command()
    print("Global tendency switched {} times".format(nb_occurs))

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        printUsage()
    elif (len(sys.argv) == 2):
        start_groundhog()
    else:
        raise ValueError("Error: The program only take periode as argument")

if __name__ == "__main__":
    try:
        main()
    except ValueError as ve:
        print(ve)
        sys.exit(84)
