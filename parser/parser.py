from bs4 import BeautifulSoup
from selenium import webdriver


def get_html_content():
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    driver.get('https://adm.pl.court.gov.ua/sud1670/gromadyanam/csz/')

    driver.find_element_by_id('cleardate').click()
    driver.find_element_by_id('filter').send_keys('Фісенко Віталій')

    html_content = driver.page_source
    driver.close()

    return html_content


def parse(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    html_table = soup.find('table', {'id': 'assignments'})
    # html_table = soup.find('table', {'id': 'assignments'}).find('td', {'class':'dataTables_empty'})
    # assign_container = main_div.find('div', {'id': 'assign_container'})

    return html_table


if __name__ == '__main__':
    html = get_html_content()
    table = parse(html)
    print(table)




