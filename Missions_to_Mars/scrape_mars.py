from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Setup Splinter
    executable_path = {'executable_path':'C:\\Users\\david\\chromedriver_win32\\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # BeautifulSoup
    html = browser.html
    soup = bs(html, 'html.parser')

    # News
    news_title = soup.find('div', class_='content_title').text.strip()
    paragraph_text = soup.find('div', class_='article_teaser_body').text.strip()

    # Image
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    img_source = soup.find('img', class_='headerimage fade-in').get('src')
    full_img_url = f'{url}{img_source}'

    # Mars Facts
    url = 'https://galaxyfacts-mars.com/'
    mars_facts = pd.read_html(url)
    mars_df = mars_facts[0]
    mars_html = mars_df.to_html()

    # Mars Hemispheres
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    browser.links.find_by_partial_text('Cerberus').click()
    img_link = browser.links.find_by_text('Sample').first
    cerberus = img_link['href']

    browser.visit(url)
    browser.links.find_by_partial_text('Schiaparelli').click()
    img_link = browser.links.find_by_text('Sample').first
    schiaparelli = img_link['href']

    browser.visit(url)
    browser.links.find_by_partial_text('Syrtis').click()
    img_link = browser.links.find_by_text('Sample').first
    syrtis = img_link['href']

    browser.visit(url)
    browser.links.find_by_partial_text('Valles').click()
    img_link = browser.links.find_by_text('Sample').first
    valles = img_link['href']

    #Hemishpere Dictionary
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles},
        {"title": "Cerberus Hemisphere", "img_url": cerberus},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis},
    ]

    browser.quit()

    # Scraped Dictionary
    scrape_dict={
        'news_title':news_title,
        'paragraph_text':paragraph_text,
        'full_img_url':full_img_url,
        'mars_html':mars_html,
        'hemisphere_image_urls':hemisphere_image_urls
    }

    return scrape_dict







