#!/usr/bin/env python3

# ASCII Art - Audi Logo
# Four interlocking rings representing the merged companies
#Due June 15 2025
# Class: CS152DLU1A2025 Introduction to Python Programming
# Authored By: Larry Grace

def get_audi_text():
    return [
        " █████  ██    ██ ██████  ██",
        "██   ██ ██    ██ ██   ██ ██",
        "███████ ██    ██ ██   ██ ██",
        "██   ██ ██    ██ ██   ██ ██",
        "██   ██  ██████  ██████  ██"
    ]

def get_ring():
    return [
        "     oooo     ",
        "   oo    oo   ",
        " oo        oo ",
        "oo          oo",
        "oo          oo",
        " oo        oo ",
        "   oo    oo   ",
        "     oooo     "
    ]

def draw_audi_logo():
    # Print AUDI text
    print('\n'.join(get_audi_text()))
    print('\n' * 2)
    
    # Create and print the four rings
    ring = get_ring()
    rings = []
    for line in range(len(ring)):
        rings.append(ring[line] + '    ' + ring[line] + '    ' + ring[line] + '    ' + ring[line])
    
    print('\n'.join(rings))

if __name__ == '__main__':
    draw_audi_logo()
