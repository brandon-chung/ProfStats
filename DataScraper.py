from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid=26388"

html_page = urlopen(url)
soup = BeautifulSoup(html_page, 'html.parser')

# Gets name of professor
find_name = soup.find('h1', class_='profname')
find_first_name = find_name.find('span', class_='pfname')
first_name = find_first_name.get_text().strip()
find_last_name = find_name.find('span', class_='plname')
last_name = find_last_name.get_text().strip()
print(first_name, last_name)

# Gets every course a person has taken
result = soup.findAll('span')
for line in result:
    if "name" in str(line):
        course_name = line.find('span', class_='response')
        if course_name != None:
            print(course_name.get_text())

# Gets value of the professor's rating-> float
container = soup.find('div', class_='breakdown-container quality')
find_rating = container.find('div', class_='grade')
rating = float(find_rating.get_text())
print(rating)

def get_percentage():
    container = soup.find('div', class_='breakdown-section')
    find_take_again = container.find('div', class_='grade')
    if find_take_again.get_text().strip() != 'N/A':
        take_again = int(find_take_again.get_text().strip().strip('%'))
    else:
        take_again = find_take_again.get_text().strip()
    return take_again

print(get_percentage())




