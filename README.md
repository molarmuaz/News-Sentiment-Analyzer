# News Sentiment Analyzer

## Description

News Sentiment Analyzer is a Python project that analyzes the sentiment of news articles based on a given keyword. It fetches articles using the News API, analyzes their content using the newspaper and textblob libraries, and calculates an average sentiment score. The sentiment score is categorized as very negative, negative, neutral, positive, or very positive based on the polarity of keywords extracted from each article.

## Features

- Fetches news articles using the News API.
- Analyzes article content using newspaper3k and textblob.
- Calculates an average sentiment score for a given keyword or name.
- Provides a sentiment summary (positive, negative, or neutral).

## Future Plans

- Expand the number of articles processed for more accurate sentiment analysis.
- Implement functionality to compare sentiments from left-leaning and right-leaning news sources, highlighting differences in perspectives.
- Improve sentiment accuracy by refining the analysis and handling edge cases where negative words are not correctly scored.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/news-sentiment-analyzer.git
   ```

2. Navigate to the project directory:
   ```sh
   cd news-sentiment-analyzer
   ```

3. Install dependencies:
   ```sh
   pip install requests nltk textblob newspaper3k
   ```

4. Set up your News API key:
   - Obtain an API key from [News API](https://newsapi.org/).
   - Replace `'API_KEY'` in the `api_key` variable in `main.py` with your actual API key.

## Example

### Example Cases

#### Case 1: Analyzing Sentiment for "Palestine" vs "Ukraine"

To analyze the sentiment of articles related to "Palestine", make the following edit:

```
keyword = "Palestine"
```

![image](https://github.com/molarmuaz/News-Sentiment-Analyzer/assets/112881407/707b6c80-2ec0-4dd1-a02f-c2f6c36a0312)


To analyze the sentiment of articles related to "Ukraine", make the following edit:

```
keyword = "Ukraine"
```

![image](https://github.com/molarmuaz/News-Sentiment-Analyzer/assets/112881407/67a4e86a-074c-4e5a-a731-a8c26c758d70)

The difference in sentiment scores between "Palestine" and "Ukraine" suggests a nuanced approach by news sources in reporting these issues. The neutral sentiment for Palestine indicates a tendency to use more moderate language, which can influence public perception by presenting the situation in a less dire manner compared to the more negative sentiment associated with Ukraine. This analysis highlights the importance of language in journalism and its impact on how news is conveyed to the audience.

#### Case 2: Analyzing Sentiment for "Donald Trump"

To analyze the sentiment of articles related to "Donald Trump", run the following command:

```
keyword = "Donald Trump"
```
![image](https://github.com/molarmuaz/News-Sentiment-Analyzer/assets/112881407/ba4ba048-39a5-4616-a5e3-17e6fd45a7db)

Donald Trump received a positive sentiment score, likely due to his opposition to Joe Biden, who has recently faced criticism for economic and political failures. The media's portrayal of Biden's challenges might be influencing a more favorable view of Trump in comparison.

![image](https://github.com/molarmuaz/News-Sentiment-Analyzer/assets/112881407/47034bd3-1127-4f80-ab6b-813face06f95)
![image](https://github.com/molarmuaz/News-Sentiment-Analyzer/assets/112881407/ef0e1b5b-61bc-4e6f-a85a-557b4b6c2762)

In the analysis, leftist news sources such as BBC, Al Jazeera English, and Naked Capitalism have exhibited a predominantly negative polarity towards Donald Trump. This is consistent with the expected sentiment, as Trump represents right-wing views, which often contrast sharply with the perspectives and editorial stances of these left-leaning outlets.

I hope to revisit this project someday and incorporate a left-right division to compare sentiment differences across the political spectrum. This enhancement would provide a deeper understanding of how left-leaning and right-leaning news sources report on the same topics, offering valuable insights into media bias and perspective.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request.

## Acknowledgements

- [News API](https://newsapi.org/)
- [newspaper3k](https://newspaper.readthedocs.io/en/latest/)
- [textblob](https://textblob.readthedocs.io/en/dev/)
