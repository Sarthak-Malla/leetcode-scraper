from selenium import webdriver
import bs4
import os
import sys

# path to my LeetCode git repo
PATH = ".,/,,/LeetCode/"

# create a folder with the name of the problem if not exists
def create_folder(folder_name):
    if not os.path.exists(PATH):
        print(f"Path {PATH} does not exist")
        exit()
    
    path_ = f"{PATH}{folder_name}"
    if not os.path.exists(path_):
        os.mkdir(path_)
    else:
        print(f"Folder {folder_name} already exists")
        exit()

    print("------------------------------")
    print(f"Folder {folder_name} created!")
    print("------------------------------")

# write README.md file
def write_readme(title, difficulty, description_tag, folder_name):
    with open(f'{PATH}{folder_name}/README.md', 'w') as file:
        file.write(f"# {title}\n\n")
        file.write(f"Difficulty: {difficulty}\n")
        file.write(f"## Description\n")

        for line in description_tag:
            if line != '\n':
                file.write(f"{line}\n")
    print("------------------------------")
    print(f"README.md file created!")
    print("------------------------------")

    # create .gitignore file
    with open(f'{PATH}{folder_name}/.gitignore', 'w') as file:
        file.write(f"*.out\n")

    # create main.cpp file
    with open(f"{PATH}{folder_name}/main.cpp", 'w') as file:
        file.write(f"#include <bits/stdc++.h>\n\nusing namespace std;\n\nint main(){{\n\n\treturn 0;\n}}")

# runs selenium to extract the problem description
def extract_problem(url):    
    driver = webdriver.Chrome()
    driver.get(url)

    driver.implicitly_wait(15)

    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

    # title
    title = soup.find('div', class_='h-full').find('span', class_='mr-2').text
    folder_name = title.strip(); # folder name
    title_l = title.split()[1:] # remove the number
    title = ' '.join(title_l) # join the list

    difficulty = soup.find('div', class_='mt-3').div.text

    description_tag = soup.find('div', class_='_1l1MA').contents

    # create folder + also checks if the path is valid
    create_folder(folder_name)

    # storing the problem description in a README.md file
    write_readme(title, difficulty, description_tag, folder_name)

    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        exit()

    url = sys.argv[1]

    if not url.startswith("https://leetcode.com/problems/"):
        print("Invalid URL")
        exit()

    extract_problem(url)