from nltk.sentiment.vader import SentimentIntensityAnalyzer
        import nltk
        nltk.download('vader_lexicon') # Download the VADER lexicon

        analyzer = SentimentIntensityAnalyzer()
        text = "This is a fantastic product, I love it!"
        sentiment_scores = analyzer.polarity_scores(text)
        print(sentiment_scores)
        # Example output: {'neg': 0.0, 'neu': 0.417, 'pos': 0.583, 'compound': 0.8316}
