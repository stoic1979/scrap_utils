import requests
from bs4 import BeautifulSoup


class IndeedScrapper:

    def __init__(self, pos, location):
        post = pos.replace(" ", "+")
        self.post = post
        loc = location.replace(" ", "+")
        self.location = loc

    def run(self):
        base_url = 'https://www.indeed.co.in/jobs?q=' \
              '%s&l=%s&start=' % (self.post, self.location)
        for j in range(0, 1000, 10):
            try:
                url = base_url + str(j)
                print ''
                print '[url] ::', url
                r = requests.get(url)

                if not r.status_code == 200:
                    print "Failed to get content of url: %s" % url
                    return
                html_doc = r.content

                soup = BeautifulSoup(html_doc, 'html.parser')

                # parsing html content  to fet information about python developer
                # for div in soup.find_all('div', class_='brdr'):
                for div in soup.find_all('div'):
                    # ignore divs with classes
                    if not div.attrs.has_key('class'):
                        continue

                    cls = div.attrs['class']
                    if 'row' in cls and 'result' in cls:
                        self.scrap_result_row(div)
                        # break
            except Exception as exp:
                print 'run() :: Got exception : %s' % exp

    def scrap_result_row(self, div):

        # title
        title = div.find('span', class_='company').text.strip()
        print "title: %s" % title

        # location
        span = div.find('span', class_='location')
        location = span.text.strip()
        print "location: %s" % location

        # salary
        sal = ''
        span = div.find('span', class_='no-wrap')
        if span:
            sal = span.text.strip()
            print "salary: %s" % sal

        # summary
        span = div.find('span', class_='summary')
        summary = span.text.strip()
        print "summery: %s" % summary

if __name__ == '__main__':
    scraper = IndeedScrapper('java', 'mohali punjab')
    scraper.run()
