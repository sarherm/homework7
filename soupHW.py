# To run this, you need to install BeautifulSoup if you aren't using anaconda
# https://pypi.python.org/pypi/beautifulsoup4

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import unittest
import re 

def getSumSpans(url):
    """ return a sum of all of the text values in the span tags at the passed url

        url -- a uniform resource locator - address for a web page

    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False 
    ctx.verify_mode = ssl.CERT_NONE
    
    html = urlopen(url, context = ctx).read()
    beautiful_soup = BeautifulSoup(html, "html.parser")
    span_tags = beautiful_soup.find_all('span')

    overall_total = 0 
    for x in span_tags:
        numbers = re.findall(r'\b\d+\b', x.text)
        num_total = sum([int(x) for x in numbers])
        overall_total += num_total
    return overall_total 



    #pass

def followLinks(url, numAnchor, numTimes):

    """ Repeat for numTimes. Find the url at numAnchor position (the first link is at position 1) at
        the current url and use that as the new url
        return the text in the a tag from the last url that you process

        url -- a uniform resource locator - address for a web page
        numAnchor -- the position of the anchor (a tag) you are looking at on the page - the first link is position 1
        numTimes -- the number of times to repeat the process of finding the new url
    """
    #ctx = ssl.create_default_context()
    #ctx.check_hostname = False 
    #ctx.verify_mode = ssl.CERT_NONE
    
    #html = urlopen(url, context = ctx).read()
   
    #name_list = []
    #for x in range(numTimes):
        #beautiful_soup = BeautifulSoup(html, "html.parser")
       # a_tags = beautiful_soup.find_all('a')
        
        
       # link = a_tags[numAnchor -1]
       # name_list.append(link.text)
        #new_url = url + link.get('href')

       # html = urlopen(new_url, context = ctx).read()
    #return name_list[-1]


    pass

def getGradeHistogram(url):
    """ return a sorted tuple with the grade range (such as 90, 80, etc) and the number of grades in that range
        url -- a uniform resource locator - address for a web page
    """
    #grades = {}
    #ctx = ssl.create_default_context()
   # ctx.check_hostname = False 
    #ctx.verify_mode = ssl.CERT_NONE
    
   # html = urlopen(url, context = ctx).read()
   # beautiful_soup = BeautifulSoup(html, "html.parser")
   # span_tags = beautiful_soup.find_all('span')
   # for x in span_tags:
       # numbers = re.findall(r'\b\d+\b', x.text)
        #for x in numbers:
         #   if len(x) > 1:
         #       grade_range = int(x[0]) * 10 
          #  else: 
          #      grade_range = 0 
           # if grade_range not in grades:
                #grades[grade_range] = 1 
           # else: 
               # grades[grade_range] += 1

    #tuple_list = list(grades.items())
   # sorted_list = sorted(tuple_list, reverse = True)
   # return sorted_list 
            
    pass


class TestHW7(unittest.TestCase):

    def test_sumSpan1(self):
        self.assertEqual(getSumSpans("http://py4e-data.dr-chuck.net/comments_42.html"), 2553)

    def test_sumSpan2(self):
        self.assertEqual(getSumSpans("http://py4e-data.dr-chuck.net/comments_132199.html"), 2714)

    def test_followLinks1(self):
        self.assertEqual(followLinks("http://py4e-data.dr-chuck.net/known_by_Fikret.html",3,4), "Anayah")

    def test_followLinks2(self):
        self.assertEqual(followLinks("http://py4e-data.dr-chuck.net/known_by_Charlie.html",18,7), "Shannah")

    #def test_getGradeHistogram(self):
        #self.assertEqual(getGradeHistogram("http://py4e-data.dr-chuck.net/comments_42.html"), [(90, 4), (80, 4), (70, 7), (60, 7), (50, 6), (40, 3), (30, 5), (20, 4), (10, 6), (0, 4)])


unittest.main(verbosity=2)
