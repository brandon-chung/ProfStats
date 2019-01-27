from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.ratemyprofessors.com/ShowRatings.jsp?tid=13305"
html_page = urlopen(url)
soup = BeautifulSoup(html_page, 'html.parser')

# Gets name of professor-> string, string
def get_name():
    find_name = soup.find('h1', class_='profname')
    find_first_name = find_name.find('span', class_='pfname')
    first_name = find_first_name.get_text().strip()
    find_last_name = find_name.find('span', class_='plname')
    last_name = find_last_name.get_text().strip()
    return first_name, last_name

# Gets every course a person has taken-> array
def get_courses():
    aList = []
    result = soup.findAll('span')
    for line in result:
        if "name" in str(line):
            course_name = line.find('span', class_='response')
            if course_name != None:
                aList.append(course_name.get_text())
    return aList

# Gets value of the professor's rating-> float
def get_rating():
    container = soup.find('div', class_='breakdown-container quality')
    find_rating = container.find('div', class_='grade')
    rating = float(find_rating.get_text())
    return rating

# Gets value of professor's would take again-> int
def get_percentage():
    container = soup.find('div', class_='breakdown-section')
    find_take_again = container.find('div', class_='grade')
    if find_take_again.get_text().strip() != 'N/A':
        take_again = int(find_take_again.get_text().strip().strip('%'))
    else:
        take_again = find_take_again.get_text().strip()
    return take_again

print(get_name())
print(get_courses())
print(get_rating())
print(get_percentage())




