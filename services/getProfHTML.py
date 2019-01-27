from urllib.request import urlopen
from bs4 import BeautifulSoup
from webscrap.DataScraper import parse_url, get_courses, get_reviews, get_tags, get_percentage, get_name, get_rating
from services.historicalGradeAverage import averagePassing

def professorURL(name):
    firstName = name.partition(' ')[0]
    lastName = name.partition(' ')[2]
    url_page = 'https://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=teacherName&schoolName=University+of+British+Columbia&schoolID=1413&query=' + firstName + '+' + lastName

    html_page = urlopen(url_page)
    soup = BeautifulSoup(html_page, 'html.parser')
    try:
        professorListing = soup.find('li', attrs={'class': "listing PROFESSOR"})
        accessHTML = str(professorListing.find('a'))
        link = (accessHTML.partition('<a href="')[2]).partition('">')[0]

        output = "https://www.ratemyprofessors.com" + link
        print(output)
        newSoup = parse_url(output)
        profName = get_name(newSoup)
        firstName = profName[0]
        lastName = profName[1]
        profCourses = get_courses(newSoup)
        profRating = get_rating(newSoup)
        profPercentage = get_percentage(newSoup)
        profTags = get_tags(newSoup)
        profReviews = get_reviews(newSoup)
        avPass = averagePassing(firstName, lastName)
        historicalAverage = avPass[0]
        passing = avPass[1]
        profInfo = [profName, historicalAverage, passing, profCourses, profRating, profPercentage, profTags, profReviews]
        return(profInfo)

    except:
        print("Invalid name or professor could not be found")