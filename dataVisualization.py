import matplotlib.pyplot as plt
import numpy as np
import dataBase
import pandas as pd


def plotAVGSalaryPerProfession():
    professions, salaryAVG = dataBase.avergPerJob()
    fig, ax = plt.subplots()

    plt.barh(professions, salaryAVG)
    plt.ylabel('Professions')
    plt.xlabel('Average salary')
    plt.yticks([])
    plt.xlim([0, 4500000])
    plt.title("Average salary per profession")
    for bar, profession, salaryAVGunit in zip(ax.patches, professions[::-1], salaryAVG):
        ax.text(0.1, bar.get_y()+bar.get_height()/2, (profession+" $"+str(round(salaryAVGunit/1000000, 2))+"M"),
                color='white', ha='left', va='center')

    plt.show()

    plt.savefig("graphics/pieChartAvgSalary.png", dpi=300, bbox_inches='tight')


plotAVGSalaryPerProfession()
