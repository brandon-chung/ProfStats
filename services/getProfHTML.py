from urllib.request import urlopen
from bs4 import BeautifulSoup

def professorURL(firstName, lastName):
    url_page = 'https://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=teacherName&schoolName=University+of+British+Columbia&schoolID=1413&query=' + firstName + '+' + lastName

    html_page = urlopen(url_page)
    soup = BeautifulSoup(html_page, 'html.parser')

    try:
        professorListing = soup.find('li', attrs={'class': "listing PROFESSOR"})
        accessHTML = str(professorListing.find('a'))
        link = (accessHTML.partition('<a href="')[2]).partition('">')[0]

        output = "https://www.ratemyprofessors.com" + link

        return(output)
    except:
        print("Invalid name or professor could not be found")