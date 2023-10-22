
def levenshtein_distance(str1, str2):

    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,        # Deletion
                dp[i][j - 1] + 1,        # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )
    return dp[m][n]


import requests
from bs4 import BeautifulSoup

# Define the URL of the subreddit you want to scrape
subreddit_url = 'https://www.reddit.com/r/ethz/'

# Send an HTTP GET request to the subreddit URL
response = requests.get(subreddit_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the post titles
    post_titles = []
    for post in soup.find_all('div', class_='scrollerItem'):
        title = post.find('h3', class_='fMFpW9')
        if title:
            post_titles.append(title.text)

    # Print the post titles
    for i, title in enumerate(post_titles):
        print(f"{i + 1}. {title}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
