#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:37:35 2023

@author: giannidiarbi    
Gianni Diarbi
DS2000
Spring 2023
HW 2 Problem 1
loans.py
"""

import matplotlib.pyplot as plt

SCHOOL_INFO_FILE = "debt_vs_tuition.txt"

def main():
    # Gather data - read in each school's name, average debt per student,
    # yearly tuition, and school color
    with open(SCHOOL_INFO_FILE, "r") as infile: 
        school1 = infile.readline().strip()
        debt1 = int(infile.readline().strip())
        tuition1 = int(infile.readline().strip())
        color1 = infile.readline().strip()
        
        school2 = infile.readline().strip()
        debt2 = int(infile.readline().strip())
        tuition2 = int(infile.readline().strip())
        color2 = infile.readline().strip()
        
        school3 = infile.readline().strip()
        debt3 = int(infile.readline().strip())
        tuition3 = int(infile.readline().strip())
        color3 = infile.readline().strip()
    
    # Computation - calculate the average debt across all three schools
    avg_debt = ( debt1 + debt2 + debt3 ) / 3
    
    # Communication - plot tuition vs debt
    plt.plot(tuition1, debt1, "o", color = color1, label = school1)
    plt.plot(tuition2, debt2, "o", color = color2, label = school2)
    plt.plot(tuition3, debt3, "o", color = color3, label = school3)
  
    # Add labels to axes, and title
    plt.xlabel("Yearly Tuition ($)")
    plt.ylabel("Average Debt per Student (Federal Loans) ($)")
    plt.title("University Yearly Tuition vs Average Student Debt ($)")
   
    # Plot a horizontal for the average debt
    plt.axhline(avg_debt, color = "magenta", label = "avg debt")
    plt.legend()
    
    # Change the ranges for x and y axes
    plt.xlim(57000, 65500)
    plt.ylim(19500, 25000)
   
    # Put values on the points
    plt.text(tuition1, debt1 - 650, "tuition: " + str(tuition1))
    plt.text(tuition2, debt2 + 200, "tuition: " + str(tuition2))
    plt.text(tuition3, debt3 + 200, "tuition: " + str(tuition3))
    
    plt.text(tuition1, debt1 - 300, "debt: " + str(debt1))
    plt.text(tuition2, debt2 + 450, "debt: " + str(debt2))
    plt.text(tuition3, debt3 + 450, "debt: " + str(debt3))
    
main()