from urllib.request import urlopen
from bs4 import BeautifulSoup
from services.database.models import *

def parse_url(url):
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, 'html.parser')
    return soup

# Gets name of professor-> string, string
def get_name(soup):
    find_name = soup.find('h1', class_='profname')
    find_first_name = find_name.find('span', class_='pfname')
    first_name = find_first_name.get_text().strip()
    find_last_name = find_name.find('span', class_='plname')
    last_name = find_last_name.get_text().strip()
    return first_name, last_name

# Gets every course a person has taken-> array
def get_courses(soup):
    aList = []
    result = soup.findAll('span')
    for line in result:
        if "name" in str(line):
            course_name = line.find('span', class_='response')
            if course_name != None:
                aList.append(course_name.get_text())
    return aList

# Gets value of the professor's rating-> float
def get_rating(soup):
    container = soup.find('div', class_='breakdown-container quality')
    find_rating = container.find('div', class_='grade')
    rating = float(find_rating.get_text())
    return rating

# Gets value of professor's would take again-> int
def get_percentage(soup):
    container = soup.find('div', class_='breakdown-section')
    find_take_again = container.find('div', class_='grade')
    if find_take_again.get_text().strip() != 'N/A':
        take_again = int(find_take_again.get_text().strip().strip('%'))
    else:
        take_again = find_take_again.get_text().strip()
    return take_again

# Gets the tags for professor-> [(tag, value)]
def get_tags(soup):
    container = soup.find('div', class_='tag-box')
    lines = str(container).split('\n')
    aList = []
    for line in lines:
        focused_line = (line.partition('<span class="tag-box-choosetags"> ')[2]).partition(' <b>')
        tag = focused_line[0].capitalize()
        tag_value = focused_line[2].partition('</b>')[0].strip('()')
        if tag != '' and tag != None:
            aList.append((tag, tag_value))
    return aList

def get_reviews(soup):
    lines = soup.find_all('p', class_='commentsParagraph')
    aList = []
    for line in lines:
        aList.append(' '.join(line.get_text().split()))
    return aList

def get_average_and_pass(first, last):
    url = 'https://slacknotes.com/professors?first_name=' + first.lower() + '&last_name=' + last.lower()
    soup = parse_url(url)
    lines = soup.find('h2')
    print(url)
    print(soup)

def make_prof(url):
    """
    Queries for a prof and returns a Prof object with the relevant metadata
    """
    soup = parse_url(url)
    first_name, last_name = get_name(soup)

    prof = Prof(url, first_name, last_name)

    return prof

get_average_and_pass('gregor', 'kiczales')