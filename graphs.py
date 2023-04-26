# all graphs here
import requests, pandas as pd, numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation
from matplotlib import rc
from matplotlib.figure import Figure

def initialize():
    household_type = pd.read_excel("raw_data.xlsx",sheet_name="T1",header=10,nrows=9)
    household_occupier_type = pd.read_excel("raw_data.xlsx",sheet_name="T2",header=10,nrows=25)
    household_size = pd.read_excel("raw_data.xlsx",sheet_name="T3",header=9,nrows=16)
    household_type_tenancy = pd.read_excel("raw_data.xlsx",sheet_name="T4",header=9,nrows=12)
    household_child = pd.read_excel("raw_data.xlsx",sheet_name="T5",header=10,nrows=11)
    household_type = household_type.drop(axis=0,index=[0,1])
    household_type = household_type.drop(columns="1980")
    return household_type, household_occupier_type, household_size, household_type_tenancy, household_child


def household_dwelling_line(household_type):
    selected_household_type = household_type.melt(id_vars=["Data Series"],
            value_vars=[str(i) for i in range(1983,2023)])
    selected_household_type = selected_household_type.rename(columns={"Data Series":"Type of Household",
                                                                  "variable":"year", "value":"noHouseholds"})
    fig = Figure(dpi=60)
    ax = fig.subplots()
    sns.pointplot(y=selected_household_type["noHouseholds"],x=selected_household_type["year"],data=selected_household_type,hue="Type of Household",ax=ax)
    ax.set_title("Number of residential households from 1983 to 2022 based on type of dwelling")
    return fig

def household_dwelling_bar_decade(household_type):
    selected_household_type = household_type.melt(id_vars=["Data Series"],
            value_vars=[str(i) for i in range(1983,2023)])
    selected_household_type = selected_household_type.rename(columns={"Data Series":"Type of Household",
                                                                  "variable":"year", "value":"noHouseholds"})
    selected_household_type_decade = selected_household_type[selected_household_type["year"].astype(int)%10==0]
    
    fig = Figure(dpi=60)
    ax = fig.subplots()
    pd.pivot_table(selected_household_type_decade,values="noHouseholds",index="Type of Household",columns="year").plot(kind="bar",figsize=(18,8),ax=ax)
    ax.set_title("Change of number of households across decades")
    ax.set_xticklabels(ax.get_xticklabels(),rotation=5)
    ax.set_ylabel("Number of household units")
    return fig





