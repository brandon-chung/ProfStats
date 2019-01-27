from urllib.request import urlopen
from bs4 import BeautifulSoup
from services.DataScraper import parse_url, get_courses, get_reviews, get_tags, get_percentage, get_name, get_rating
from services.historicalGradeAverage import averagePassing
from services.visualizer.visualizer import generateImage

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
        profInfo = {'name':profName, 'first_name': firstName, 'last_name': lastName, 'url': url, 'average': historicalAverage,
            'average_passing':passing,'courses': profCourses, 'rating':profRating,
            'take_again': profPercentage, 'tags':profTags, 'reviews': profReviews}
        # generateImg(profName, profCourses, profRating, profPercentage, historicalAverage, passing)
        print("GENERATE IMAGE")
        generateImage("Cinda Heeren", "CPSC 213, CPSC 221", "4.5", "0", "80%", "90%")
        print("END GENERATION")
        return(profInfo)

    except Exception as e:
        print(e)
        print("Invalid name or professor could not be found")
        return None