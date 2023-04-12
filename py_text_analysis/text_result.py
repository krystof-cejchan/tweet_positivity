from transformers import pipeline


class TextAnalysisResult:
    def __init__(self, mood, score):
        self.mood = mood
        self.score = score


def text_analysis(text_for_analysis):
    # create a sentiment analysis pipeline
    sentiment_analysis = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

    # analyze the sentiment of the text
    result = sentiment_analysis(text_for_analysis)

    return TextAnalysisResult(result[0]['label'], result[0]['score'])
