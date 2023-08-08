import requests
from bs4 import BeautifulSoup

# Get the website URL from the user
url = input("Enter the website URL: ")

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Get the type of data to scrape from the user
print("Select the type of data to scrape:")
print("1. Main Title")
print("2. Introduction Paragraph")
print("3. Section Headings")
print("4. First Reference Link")

choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
    # Find the main title of the page
    main_title = soup.find('h1', id='firstHeading').text
    print(f"Main Title: {main_title}")
elif choice == '2':
    # Find the introduction paragraph
    intro_paragraph = soup.find('div', class_='mw-parser-output').p.text
    print(f"Introduction Paragraph: {intro_paragraph}")
elif choice == '3':
    # Find and print all section headings
    section_headings = soup.find_all('span', class_='mw-headline')
    print("Section Headings:")
    for heading in section_headings:
        print(heading.text)
elif choice == '4':
    # Find the first reference link
    first_reference = soup.find('sup', class_='reference').find_next('a')['href']
    print(f"First Reference Link: {first_reference}")
else:
    print("Invalid choice. Please select a valid option.")
