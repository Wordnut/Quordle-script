from bs4 import BeautifulSoup

def extract_answers(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the textarea element
    textarea = soup.find_all('a', class_= 'underline')

    answers = [link.text for link in textarea]

    return (answers)
