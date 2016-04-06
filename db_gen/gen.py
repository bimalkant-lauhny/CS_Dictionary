from bs4 import BeautifulSoup
import sqlite3

with open("List of programming and computer science terms - LabAutopedia.html","r") as cs_terms:
    soup = BeautifulSoup(cs_terms,"lxml")

main_content = soup.find(id="mw-content-text")

all_ul = main_content.find_all("ul")

alpha_list = []

for letter in all_ul:
     alpha_list.append(letter.find_all("li"))

alpha_list.pop()
temp = str(alpha_list[0][0].text).splitlines()

connection = sqlite3.connect("cs_terms.db")
cursor = connection.cursor()
cursor.execute("create table term_def (term text,def text)")

for li in alpha_list:
    for st in li:
        term = str(st.b.string)
        defn = str(st.text).replace("\n",'').rstrip()
        #print st.b.string+'\t'+temp
        cursor.execute('''insert into term_def values ("%s","%s")''' %(term,defn))

connection.commit()
