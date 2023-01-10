from selenium import webdriver
import bs4
import os

driver = webdriver.Chrome()
driver.get("https://leetcode.com/problems/two-sum/")

driver.implicitly_wait(3)

soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

# title
title = soup.find('div', class_='h-full').find('span', class_='mr-2').text
title_l = title.split()[1:] # remove the number
title = ' '.join(title_l) # join the list
folder_name = "".join(title_l)

difficulty = soup.find('div', class_='mt-3').div.div.text

description_tag = soup.find('div', class_='_1l1MA').contents

print(description_tag)

# create a folder with the name of the problem
path = f"./{folder_name}"
if not os.path.exists(path):
    os.mkdir(path)

# storing the problem description in a README.md file
with open(f'./{folder_name}/README.md', 'w') as file:
    file.write(f"# {title}\n\n")
    file.write(f"Difficulty: {difficulty}\n")
    file.write(f"## Description\n")

    for line in description_tag:
        if line != '\n':
            file.write(f"{line}\n")

driver.quit()