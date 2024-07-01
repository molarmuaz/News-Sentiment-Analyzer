import requests
from newspaper import Article
from textblob import TextBlob

api_key = 'API_KEY'  # ENTER API
newsapi_endpoint = 'https://newsapi.org/v2/everything'

def get_articles(keyword, api_key, page=1):  # Fetches articles with the given keyword in title
    parameters = {
        'qInTitle': keyword,
        'apiKey': api_key,
        'language': 'en',
        'pageSize': 100,  # Fetch more articles to account for skipping
        'page': page
    }
    response = requests.get(newsapi_endpoint, params=parameters)
    data = response.json()

    if 'articles' in data:
        return data['articles']
    else:
        print(f"Error fetching articles: {data.get('message', 'Unknown error')}")
        return []

def analyze_article(url):  # Parses through and analyzes the article
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    summary = article.keywords
    emotion = 0
    for keyword in summary:
        emotion += float(format(TextBlob(keyword).sentiment.polarity))
    emotion = emotion / len(summary)
    return float(emotion)

def emotionconvert(polarity):  # Adjusted function to convert polarity to emotion
    if polarity == 0:
        return "Not Enough Data"
    if polarity < 0.01 and polarity > 0:
        return "Neutral"
    elif polarity >= 0.01 and polarity < 0.03:
        return "Positive"
    elif polarity >= 0.03:
        return "Very Positive"
    elif polarity < 0 and polarity > -0.01:
        return "Neutral"
    elif polarity <= -0.01 and polarity > -0.03:
        return "Negative"
    elif polarity <= -0.03:
        return "Very Negative"

# Main function to perform the analysis
def analyze_sentiment(keyword):
    page = 1
    sentiments = []

    while len(sentiments) < 20:
        articles = get_articles(keyword, api_key, page)
        if not articles:
            print("No more articles found for the given keyword.")
            break

        for article in articles:
            if len(sentiments) >= 20:
                break
           
            
            try:
                polarity = analyze_article(article['url'])
                if polarity != 0.0:  # Skip articles with polarity 0.0
                    print(f"Processing article from source: {article['source']['name']}, URL: {article['url']}")
                    print(f"Polarity for article: {polarity}")
                    sentiments.append(polarity)
            except Exception as e:
                print(f"Error analyzing article {article['url']}: {e}")
                continue

        page += 1

    avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
    overall_emotion = emotionconvert(avg_sentiment)
    print("Keyword: ", keyword)
    print(f"Sentiment: {overall_emotion}")

# Example usage
keyword = ""
analyze_sentiment(keyword)
