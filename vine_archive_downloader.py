from bs4 import BeautifulSoup as bs
import urllib.request

page = open('packie.html')
soup = bs(page, 'html.parser')
grid_posts = soup.find_all('div', {'class': 'ember-view grid post'})

video_containers = []
for p in grid_posts:
    video_containers.append(p.find('div', {'class': 'video-container'}))

links = []
for c in video_containers:
    link_text = c.get('style')
    start = link_text.find('https')
    end = link_text.find('.mp4', start) + 4
    links.append(link_text[start:end])

index = 0
for l in links:
    index += 1
    try:
        print(f'Downloading {index:03}...')
        urllib.request.urlretrieve(l, f'vines/packie_{index:03}.mp4')
        print(f'{index:03} complete!')
    except Exception as e:
        print(e)




