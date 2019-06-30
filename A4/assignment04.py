import json
import numpy as np
import os
import pandas as pd
from datetime import datetime
from pprint import pprint
import sys
import fhirclient.models.bundle as bu
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt


def read_file(fhir_bundle_path):
    with open(fhir_bundle_path, 'r', encoding='UTF-8') as f:
        s = json.load(f)
        return s


# Get age by birth date
def get_age(birthDate):
    y_m_d = birthDate.split("-")
    birth = datetime(int(y_m_d[0]), int(y_m_d[1]), int(y_m_d[2]))
    today = datetime.now()
    return (today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day)))


def plot_age_by_gender(bundle_path, figure_name='q1_age_by_gender.png'):
    """17 points for correctness, 3 Points for Proficiency
    See https://briankolowitz.github.io/data-focused-python/assignments
    Save the figure to a PNG file with the specified figure_name
    Note : you CANNOT use Numpy or Pandas
    Note : you MUST ONLY use matplotlib
    
    Arguments:
        bundle_path {str} -- path to Synthea generated FHIR bundles
    """
    files = os.listdir(bundle_path)
    map = {'male': {0: 0, 10: 0, 20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0, 80: 0, 90: 0, 100: 0},
           'female': {0: 0, 10: 0, 20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0, 80: 0, 90: 0, 100: 0}}
    for file in files:
        if not os.path.isdir(file):
            path = bundle_path + "/" + file
            dic = read_file(path)
            if dic["entry"][0]["resource"]["resourceType"] != "Patient": continue
            gender = str(dic["entry"][0]["resource"]["gender"])
            age = get_age((dic["entry"][0]["resource"]["birthDate"]))
            age = 100 if age > 100 else age
            map[gender][int(age / 10) * 10] += 1

    top = max(max(map['male'].values()), max(map['female'].values()))
    figure, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)
    male = axes[0]
    female = axes[1]
    plt.suptitle("Patient Age by Gender")

    male.barh(list(map["male"].keys()), list(map["male"].values()), color="darkblue")
    male.invert_xaxis()
    male.set_xlabel("Count")
    male.set_title("Male")
    male.yaxis.tick_right()
    # male.set_xticks([x for x in range(0, top + 2, 2)])
    male.set_yticks([x for x in range(0, 101, 10)])

    female.barh(list(map["female"].keys()), list(map["female"].values()), color="darkred")
    female.set_title("Female")
    female.set_xlabel("Count")
    female.xaxis.set_major_locator(MaxNLocator(integer=True))
    # female.set_xticks([x for x in range(0, top + 2, 2)])
    # Show the plot
    plt.savefig(figure_name)


def plot_by_gender_and_race(bundle_path, figure_name='q2_by_gender_and_race.png'):
    """17 points for correctness, 3 Points for Proficiency
    See https://briankolowitz.github.io/data-focused-python/assignments
    Save the figure to a PNG file with the specified figure_name
    Note : you CANNOT use Numpy or Pandas
    Note : you MUST ONLY use matplotlib
    
    Arguments:
        bundle_path {str} -- path to Synthea generated FHIR bundles
    """
    files = os.listdir(bundle_path)
    map = {}
    for file in files:
        if not os.path.isdir(file):
            path = bundle_path + "/" + file
            dic = read_file(path)
            if dic["entry"][0]["resource"]["resourceType"] != "Patient": continue
            gender = str(dic["entry"][0]["resource"]["gender"])
            for i in dic["entry"][0]["resource"]["extension"]:
                if i["url"] == "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race":
                    for j in i["extension"]:
                        if "valueString" in j.keys():
                            race = j["valueString"]
                            if race not in map.keys():
                                map[race] = {"male": 0, "female": 0}
                            map[race][gender] += 1

    length = len(map)
    fig, ax = plt.subplots(figsize=(12, 5))

    ax.set_xticks([x for x in range(3 * length + 1)])
    x_list = [" "]

    for gender in map.keys():
        x_list.append((gender))
        x_list.append(" ")
        x_list.append(" ")
    x_list.append(" ")

    ax.set_xticklabels(x_list)
    # plt.xticks(rotation=30)
    ax.set_title("Patient by Gender and Race")
    start = 1
    for gender in map.keys():
        ax.bar(start - 0.5, map[gender]['male'], color="darkblue")
        ax.bar(start + 0.5, map[gender]['female'], color="darkred")
        start += 3
    ax.set_xlabel("race")
    ax.legend(['male', 'female'])
    plt.savefig(figure_name)


def plot_by_gender_and_birth_country(bundle_path, figure_name='q3_by_gender_and_birth_country.png'):
    """17 points for correctness, 3 Points for Proficiency
    See https://briankolowitz.github.io/data-focused-python/assignments
    Save the figure to a PNG file with the specified figure_name
    Note : you CANNOT use Numpy or Pandas
    Note : you MUST ONLY use matplotlib
    
    Arguments:
        bundle_path {str} -- path to Synthea generated FHIR bundles
    """
    files = os.listdir(bundle_path)
    map = {}
    for file in files:
        if not os.path.isdir(file):
            path = bundle_path + "/" + file
            dic = read_file(path)
            if dic["entry"][0]["resource"]["resourceType"] != "Patient": continue
            gender = str(dic["entry"][0]["resource"]["gender"])
            for i in dic["entry"][0]["resource"]["extension"]:
                if i["url"] == "http://hl7.org/fhir/StructureDefinition/patient-birthPlace":
                    country = i["valueAddress"]["country"]
                    if country not in map.keys():
                        map[country] = {"male": 0, "female": 0}
                    map[country][gender] += 1

    length = len(map)
    fig, ax = plt.subplots()

    ax.set_xticks([x for x in range(3 * length + 1)])
    x_list = [" "]

    for gender in map.keys():
        x_list.append((gender))
        x_list.append(" ")
        x_list.append(" ")
    x_list.append(" ")

    ax.set_xticklabels(x_list)

    ax.set_title("Patient by Gender and Country")
    start = 1
    for gender in map.keys():
        ax.bar(start - 0.5, map[gender]['male'], color="darkblue")
        ax.bar(start + 0.5, map[gender]['female'], color="darkred")
        start += 3
    ax.set_xlabel("race")
    ax.legend(['male', 'female'])
    plt.savefig(figure_name)


def plot_by_gender_and_mortality(bundle_path, figure_name='q4_by_gender_and_mortality.png'):
    """17 points for correctness, 3 Points for Proficiency
    See https://briankolowitz.github.io/data-focused-python/assignments
    Save the figure to a PNG file with the specified figure_name
    Note : you CANNOT use Numpy or Pandas
    Note : you MUST ONLY use matplotlib
    
    Arguments:
        bundle_path {str} -- path to Synthea generated FHIR bundles
    """
    files = os.listdir(bundle_path)
    map = {'male': 0, 'female': 0}
    map_live = {'male': 0, 'female': 0}
    for file in files:
        if not os.path.isdir(file):
            path = bundle_path + "/" + file
            dic = read_file(path)
            if dic["entry"][0]["resource"]["resourceType"] != "Patient": continue
            dead = False
            for entry in dic["entry"]:
                if "deceasedDateTime" in entry["resource"].keys():
                    map[entry["resource"]["gender"]] += 1
                    dead = True
            if not dead:
                map_live[dic["entry"][0]["resource"]["gender"]] += 1
    figure, ax = plt.subplots()
    ax.set_xticks([x for x in range(0, 5)])
    ax.bar(0.5, map['male'], color="darkblue")
    ax.bar(1.5, map['female'], color="darkred")
    ax.bar(2.5, map_live['male'], color="darkblue")
    ax.bar(3.5, map_live['female'], color="darkred")

    ax.set_xlabel('Gender')
    ax.set_title("Mortality by Gender")
    ax.legend(['male', 'female'])
    ax.set_xticklabels([" ", "DEAD", " ", "ALIVE", " "])
    plt.savefig(figure_name)


def plot_condition_comorbidity_matrix(bundle_path, figure_name='q5_condition_comorbidity_matrix.png'):
    files = os.listdir(bundle_path)
    dic_list = []
    for file in files:
        if not os.path.isdir(file):
            path = bundle_path + "/" + file
            dic = read_file(path)
            if dic["entry"][0]["resource"]["resourceType"] != "Patient": continue
            sub_dic = {}
            for entry in dic["entry"]:
                if entry["resource"]["resourceType"] == "Condition":
                    code = entry["resource"]["code"]["coding"][0]["display"]
                    if code not in dic.keys():
                        sub_dic[code] = 0
                    sub_dic[code] += 1
            dic_list.append(sub_dic)

    data = pd.DataFrame(dic_list)
    data = data.fillna(0)
    data = data.T.dot(data)
    name = list(data.columns)
    fig, ax = plt.subplots(figsize=(20, 20))

    ax.matshow(data.corr())
    ax.set_xticks([x for x in range(0, len(data) + 1)])
    ax.set_xticklabels(name)
    plt.xticks(rotation=90)
    ax.set_yticks([x for x in range(0, len(data) + 1)])
    ax.set_yticklabels(name)
    plt.savefig(figure_name, dpi=300)


def plot_challenge_question_1(bundle_path, figure_name='q6_challenge_question_1.png'):
    """5 Points
    Plot anything you want that uses at least 2 FHIR resources
    Save the figure to a PNG file with the specified figure_name
    Arguments:
        bundle_path {str} -- path to Synthea generated FHIR bundles
    """
    files = os.listdir(bundle_path)
    map = {}
    for file in files:
        if not os.path.isdir(file):
            path = bundle_path + "/" + file
            dic = read_file(path)
            if dic["entry"][0]["resource"]["resourceType"] != "Patient": continue
            gender = str(dic["entry"][0]["resource"]["gender"])
            race = ""
            for i in dic["entry"][0]["resource"]["extension"]:
                if i["url"] == "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race":
                    for j in i["extension"]:
                        if "valueString" in j.keys():
                            race = j["valueString"]
                            if race not in map.keys():
                                map[race] = {"male": 0, "female": 0}
            for entry in dic["entry"]:
                if "deceasedDateTime" in entry["resource"].keys():
                    map[race][entry["resource"]["gender"]] += 1

    length = len(map)
    fig, ax = plt.subplots(figsize=(12, 5))

    ax.set_xticks([x for x in range(3 * length + 1)])
    x_list = [" "]

    for gender in map.keys():
        x_list.append((gender))
        x_list.append(" ")
        x_list.append(" ")
    x_list.append(" ")

    ax.set_xticklabels(x_list)
    ax.set_title("Death  by Gender and Race")

    start = 1
    for gender in map.keys():
        ax.bar(start - 0.5, map[gender]['male'], color="darkblue")
        ax.bar(start + 0.5, map[gender]['female'], color="darkred")
        start += 3
    ax.set_xlabel("race")
    ax.legend(['male', 'female'])
    plt.savefig(figure_name)
    pass


def plot_challenge_question_2(bundle_path, figure_name='q7_challenge_question_2.png'):
    """5 Points
    Plot anything you want that uses at least 2 FHIR resources
    Save the figure to a PNG file with the specified figure_name
    Arguments:
        bundle_path {str} -- path to Synthea generated FHIR bundles
    """
    files = os.listdir(bundle_path)
    map = {}
    for file in files:
        if not os.path.isdir(file):
            path = bundle_path + "/" + file
            dic = read_file(path)
            if dic["entry"][0]["resource"]["resourceType"] != "Patient": continue
            gender = str(dic["entry"][0]["resource"]["gender"])
            country = ""
            for i in dic["entry"][0]["resource"]["extension"]:
                if i["url"] == "http://hl7.org/fhir/StructureDefinition/patient-birthPlace":
                    country = i["valueAddress"]["country"]
                    if country not in map.keys():
                        map[country] = {"male": 0, "female": 0}
            for entry in dic["entry"]:
                if "deceasedDateTime" in entry["resource"].keys():
                    map[country][entry["resource"]["gender"]] += 1

    length = len(map)
    fig, ax = plt.subplots()

    ax.set_xticks([x for x in range(3 * length + 1)])
    x_list = [" "]

    for gender in map.keys():
        x_list.append((gender))
        x_list.append(" ")
        x_list.append(" ")
    x_list.append(" ")

    ax.set_xticklabels(x_list)
    ax.set_title("Death Count by Gender and Country")
    start = 1
    for gender in map.keys():
        ax.bar(start - 0.5, map[gender]['male'], color="darkblue")
        ax.bar(start + 0.5, map[gender]['female'], color="darkred")
        start += 3
    ax.set_xlabel("race")
    ax.legend(['male', 'female'])
    plt.savefig(figure_name)


def plot_challenge_question_3(bundle_path, figure_name='q8_challenge_question_3.png'):
    """5 Points
    Plot anything you want that uses at least 3 FHIR resources
    Save the figure to a PNG file with the specified figure_name
    Arguments:
        bundle_path {str} -- path to Synthea generated FHIR bundles
    """
    files = os.listdir(bundle_path)
    map = {'male': {0: 0, 10: 0, 20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0, 80: 0, 90: 0, 100: 0},
           'female': {0: 0, 10: 0, 20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0, 80: 0, 90: 0, 100: 0}}
    for file in files:
        if not os.path.isdir(file):
            path = bundle_path + "/" + file
            dic = read_file(path)
            if dic["entry"][0]["resource"]["resourceType"] != "Patient": continue
            for entry in dic["entry"]:
                if "deceasedDateTime" in entry["resource"].keys():
                    gender = str(dic["entry"][0]["resource"]["gender"])
                    age = get_age((dic["entry"][0]["resource"]["birthDate"]))
                    age = 100 if age > 100 else age
                    map[gender][int(age / 10) * 10] += 1

    top = max(max(map['male'].values()), max(map['female'].values()))
    figure, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)
    male = axes[0]
    female = axes[1]
    plt.suptitle("Patients' Death Age")

    male.barh(list(map["male"].keys()), list(map["male"].values()), color="darkblue")
    male.invert_xaxis()
    male.set_xlabel("Count")
    male.set_title("Male")
    male.yaxis.tick_right()
    # male.set_xticks([x for x in range(0, top + 2, 2)])
    male.set_yticks([x for x in range(0, 101, 10)])

    female.barh(list(map["female"].keys()), list(map["female"].values()), color="darkred")
    female.set_title("Female")
    female.set_xlabel("Count")
    female.xaxis.set_major_locator(MaxNLocator(integer=True))
    # female.set_xticks([x for x in range(0, top + 2, 2)])
    # Show the plot
    plt.savefig(figure_name)


# do not modify below this line

if __name__ == "__main__":
    bundle_path = sys.argv[1]

    # plot_age_by_gender(bundle_path)
    # plot_by_gender_and_race(bundle_path)
    # plot_by_gender_and_birth_country(bundle_path)
    plot_by_gender_and_mortality(bundle_path)
    # plot_condition_comorbidity_matrix(bundle_path)
    # plot_challenge_question_1(bundle_path)
    # plot_challenge_question_2(bundle_path)
    # plot_challenge_question_3(bundle_path)
