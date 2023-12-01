"""
Module for running through the local folders, run solutions that haven't been run yet,
and force run the solution for the current day
"""

import os
import subprocess
import re
from datetime import date, datetime
import requests

def run_scripts():
    """run through the folders, check run scripts that haven't been run yet."""
    for year in os.listdir("./years/"):
        if re.match(r'^20[0-9]{2}$', year):
            for file in os.listdir("./years/" + year):
                if re.match(r'^day[0-9]{2}\.py$', file):
                    run_script(year, file[3:5])
    today = str(date.today())
    if today[5:7] == "12" and int(today[8:10]) < 26 and datetime.now().hour > 5:
        run_script(day=today[8:10], year=today[0:4], force=True)

def run_script(year, day, force=False):
    """
    run a single script for a certain year / day
    if "force" is set to True and the script does not exists, it will be created from template.txt
    and the input will be imported from adventofcode.com
    """

    result_file = "./years/" +  year + "/day" + day + "/output.txt"
    if not os.path.exists(result_file) or force:
        print ("\nRunning day " + day + " of year " + year + "\n")

    path = "./years/" + year
    if force and not os.path.exists(path):
        os.mkdir(path)

    path = path + '/day' + day
    if force and not os.path.exists(path):
        os.mkdir(path)

    python_file = path + "/solve.py"
    if force and not os.path.exists(python_file):
        print ("Creating default script\n")

        with open("./template.txt", "r", encoding="utf-8") as template_file:
            data = template_file.read()
            template_file.close()
            with open(python_file, "w", encoding="utf-8") as file:
                file.write(data.replace("{{day}}", day).replace("{{year}}", year))
                file.close()

    test_file = path + "/test_" + year + "_" + day + ".py"
    if force and not os.path.exists(test_file):
        print ("Creating test file\n")

        with open("./testtemplate.txt", "r", encoding="utf-8") as template_file:
            data = template_file.read()
            template_file.close()
            with open(test_file, "w", encoding="utf-8") as file:
                file.write(data.replace("{{day}}", day).replace("{{year}}", year))
                file.close()


    input_file = path + "/input.txt"
    if not os.path.exists(input_file):
        print ("\nFetching input\n")
        file_url = "https://adventofcode.com/" + year + "/day/" + day.lstrip("0") + "/input"

        cookie_file = "./session.txt"
        if not os.path.exists(cookie_file):
            print("no session file found!")
            exit()
        # Cookie for authentication
        f = open(cookie_file, "r", encoding="utf-8")
        cookies = {
            'session': f.readline()
        }
        f.close()

        response = requests.get(file_url, cookies=cookies, timeout=10)
        if response.status_code == 200:
            # Write the content of the response to a file
            with open(input_file, 'wb') as file:
                file.write(response.content.strip())
        else:
            print(f"Failed to download the file. Status code: {response.status_code}")

    if not os.path.exists(result_file) or force:
        output = subprocess.check_output(["python3", python_file], text=True)

        f = open(result_file, "w", encoding="utf-8")
        f.write(output)
        f.close()

        print("\n")

run_scripts()
run_script(day="01", year="2022", force=True)
run_script(day="02", year="2022", force=True)
run_script(day="01", year="2018", force=True)
run_script(day="02", year="2018", force=True)
run_script(day="03", year="2018", force=True)
