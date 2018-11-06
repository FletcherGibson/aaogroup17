from bs4 import BeautifulSoup as BS
from urllib.request import urlopen


def gleam_options():
    gleam_page = 'http://gleam-vo.icrar.org/gleam_postage/q/form'

    options_page = urlopen(gleam_page)

    soup = BS(options_page, 'html.parser')

    freq_options = soup.find('select', attrs={'name': 'freq'})

    gleam_freq_options = []

    for option in freq_options:
        choice = ('mwagleam_dr1_' + option.text, option.text)
        gleam_freq_options.append(choice)

    return gleam_freq_options
