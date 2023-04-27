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
    ax.annotate('Max households: '+str(max(selected_household_type["noHouseholds"])), xy=(2.2, 439000), xycoords='data',
            xytext=(0.2, .95), textcoords='axes fraction',
            va='top', ha='left',
            arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('Min households: '+str(min(selected_household_type["noHouseholds"])), xy=(6.2, 3000), xycoords='data',
            xytext=(0.85, .2), textcoords='axes fraction',
            va='top', ha='left',
            arrowprops=dict(facecolor='black', shrink=0.05))    
    return fig


def household_proportion(household_type, year):
    str_year = str(year)
    labels = household_type['Data Series']
    sizes = household_type[str_year]

    fig = Figure(dpi=60)
    ax = fig.subplots()
    ax.pie(sizes,labels=labels,autopct='%1.1f%%')
    ax.set_title("Proportion of household properties in "+str_year)
    return fig

def household_demographics(household_occupier_type):
    household_occupier_type_collapsed = household_occupier_type.melt(id_vars=["Data Series","Type"],
            value_vars=["1990","1995","2000","2001","2002","2003","2004","2005","2006",
                        "2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019",
                        "2020","2021","2022"])
    household_occupier_type_collapsed = household_occupier_type_collapsed.rename(columns={"variable":"year","value":"noHouseholds"})
    household_occupier_type_selected = household_occupier_type_collapsed[household_occupier_type_collapsed["Type"]=="Resident Households"]
    household_occupier_type_selected

    fig = Figure(dpi=60)
    ax = fig.subplots()
    colors=['b','orange','green','r','gold']
    types = household_occupier_type_selected["Data Series"]
    bottom = None
    for i in range(5):
        data = household_occupier_type_selected[household_occupier_type_selected["Data Series"]==types[i]]
        if (i==0):
            ax.bar(data["year"],data["noHouseholds"],color=colors[i])
            bottom = data["noHouseholds"].to_numpy()
        else:
            ax.bar(data["year"],data["noHouseholds"],bottom=bottom,color=colors[i])
            bottom += data["noHouseholds"].to_numpy()
    ax.set_title("Bar Graph of no. of households based on household demographics from 1990 to 2022")
    ax.set_ylabel("No. of Households")
    ax.legend(types)        

    return fig

def household_reference(household_occupier_type):
    household_occupier_type_collapsed = household_occupier_type.melt(id_vars=["Data Series","Type"],
            value_vars=["1990","1995","2000","2001","2002","2003","2004","2005","2006",
                        "2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019",
                        "2020","2021","2022"])
    household_occupier_type_collapsed = household_occupier_type_collapsed.rename(columns={"variable":"year","value":"noHouseholds"})
    household_occupier_type_grouped = household_occupier_type_collapsed.groupby(by=["Type","year"]).sum()
    household_occupier_type_grouped = household_occupier_type_grouped.reset_index()
    household_occupier_type_grouped = household_occupier_type_grouped[household_occupier_type_grouped["Type"]!="Resident Households"]
    fig = Figure(dpi=55)
    ax = fig.subplots()
    sns.pointplot(y="noHouseholds",x="year",data=household_occupier_type_grouped,hue="Type",ax=ax)
    ax.set_title("Number of residential households from 1990 to 2022 based on household reference")
    ax.legend()

    return fig

def household_demographics_pie(household_occupier_type,year):
    household_occupier_type_demographics = household_occupier_type[household_occupier_type["Type"]!="Resident Households"]
    household_occupier_type_demographics = household_occupier_type_demographics.groupby(by="Data Series").sum()
    household_occupier_type_demographics = household_occupier_type_demographics.reset_index()
    labels = household_occupier_type_demographics['Data Series']
    str_year = str(year)
    fig = Figure(dpi=60)
    ax = fig.subplots()
    sizes = household_occupier_type_demographics[str_year]
    ax.pie(sizes,labels=labels,autopct='%1.1f%%')
    ax.set_title(str_year)

    return fig

def household_age_pie(household_occupier_type,year):
    household_occupier_age = household_occupier_type.groupby(by="Type").sum()
    household_occupier_age = household_occupier_age.rename(index=
        {"Household Reference Persons Aged 35-49 Years":"35 - 45 years","Household Reference Persons Aged 50-64 Years": "50 - 64 years",
        "Household Reference Persons Aged 65 Years & Over":">=65 years","Household Reference Persons Aged Below 35 Years":"<35 years"})
    household_occupier_age = household_occupier_age.reset_index()
    household_occupier_age = household_occupier_age[household_occupier_age["Type"]!="Resident Households"]
    labels = household_occupier_age['Type']

    fig = Figure(dpi=60)
    ax = fig.subplots()
    str_year = str(year)
    sizes = household_occupier_age[str_year]
    ax.pie(sizes,labels=labels,autopct='%1.1f%%')
    ax.set_title("Households based on household reference person's age"+str_year)
    
    return fig

def household_persons(household_size):
    household_size_selected = household_size.drop(columns=["1980"])
    household_size_selected = household_size_selected.melt(id_vars=["Data Series"],
                value_vars=[str(i) for i in range(1983,2023)])
    household_size_selected = household_size_selected[household_size_selected["Data Series"].str.endswith("(Persons)")]
    household_size_selected = household_size_selected.rename(columns={"variable":"year"})
    household_size_selected = household_size_selected[household_size_selected["Data Series"]!="  Total HDB Dwellings (Persons)"]

    fig = Figure(dpi=55)
    ax = fig.subplots()
    ax.set_title("Number of people staying based on type of households from 1983 to 2022")
    sns.pointplot(y="value",x="year",data=household_size_selected,hue="Data Series",ax=ax)
    ax.set_ylabel("No. of people per household")
    ax.legend(bbox_to_anchor=(1,1))
    
    return fig

def household_tenancy_demographics(household_type_tenancy,year):
    household_type_tenancy_selected = household_type_tenancy.drop(index=[0,1,2,3,4])
    household_type_tenancy_selected = household_type_tenancy_selected.set_index("Data Series")
    household_type_tenancy_selected = household_type_tenancy_selected.rename(
        index={"    HDB 1- And 2-Room Flats (Per Cent)":"1-2 Room HDB","    HDB 3-Room Flats (Per Cent)":"3 Room HDB",
            "    HDB 4-Room Flats (Per Cent)":"4 Room HDB",
            "    HDB 5-Room And Executive Flats (Per Cent)":"5 Room and Executive HDB",
            "  Condominiums & Other Apartments (Per Cent)":"Condominiums & Other Apartments",
            "  Landed Properties (Per Cent)":"Landed Properties",
            "  Other Types Of Dwelling (Per Cent)":"Others"})
    household_type_tenancy_selected = household_type_tenancy_selected.reset_index()
    labels = household_type_tenancy_selected['Data Series']
    fig = Figure(dpi=60)
    ax = fig.subplots()
    
    str_year = str(year)
    sizes = household_type_tenancy_selected[str_year]
    ax.pie(sizes,labels=labels,autopct='%1.1f%%')
    ax.set_title("Resident Households by Tenancy"+str_year)

    return fig

def household_living_arrangement(household_child):
    years = ["1990","1995","2000","2001","2002","2003","2004","2005","2006",
                            "2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019",
                            "2020","2021","2022"]
    household_child_selected = household_child.groupby(by="Type").sum()
    household_child_selected = household_child_selected.reset_index()
    household_child_selected = household_child_selected.melt(id_vars=["Type"],
                value_vars=years)
    household_child_selected = household_child_selected.rename(columns={"variable":"year"})
    fig = Figure(dpi=55)
    ax = fig.subplots()
    ax.set_title("Number of people in resident households by living arrangement 1990 to 2022")
    sns.pointplot(y="value",x="year",data=household_child_selected,hue="Type",ax=ax)
    ax.set_ylabel("No. of people per household")
    ax.legend()
    
    return fig 

def household_married_children(household_child, year):
    household_child_with_child_married = household_child[household_child["Type"]=="  Married Couple-Based With Children"]
    household_child_with_child_married = household_child_with_child_married.set_index("Data Series")
    household_child_with_child_married = household_child_with_child_married.rename(
        index={"    With Youngest Child Aged Below 6 Years":"<6 years","    With Youngest Child Aged 6 - 11 Years":"6 - 11 years",
            "    With Youngest Child Aged 12 - 15 Years":"12 - 15 years","    With Youngest Child Aged 16 Years And Over":">=16 years"})
    household_child_with_child_married = household_child_with_child_married.reset_index()
    labels = household_child_with_child_married['Data Series']

    fig = Figure(dpi=60)
    ax = fig.subplots()
    str_year = str(year)
    sizes = household_child_with_child_married[str_year]
    ax.pie(sizes,labels=labels,autopct='%1.1f%%')
    ax.set_title("Resident Households by Age of Youngest Child for Married Households with Children "+str_year)
    
    return fig 

