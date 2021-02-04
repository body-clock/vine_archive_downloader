from bs4 import BeautifulSoup as bs
import urllib.request

name = input('Input the name: ')

page = open(f'html/{name}.html')
soup = bs(page, 'html.parser')

links = []
for c in soup.find_all('div', {'class': 'video-container'}):
    link_text = c.get('style')
    start = link_text.find('https')
    end = link_text.find('.mp4', start) + 4
    links.append(link_text[start:end])

index = 0
for l in links:
    index += 1
    try:
        print(f'Downloading {index:03}...')
        urllib.request.urlretrieve(l, f'{name}_vines/{name}_{index:03}.mp4')
        print(f'{index:03} complete!')
    except Exception as e:
        print(e)




