from mrjob.job import MRJob
from nltk.sentiment import SentimentIntensityAnalyzer
import json

class MRSentimentAnalysis(MRJob):

    def mapper_init(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def mapper(self, _, line):
        try:
            review = json.loads(line)

            text = review.get("text", "")

            if text:
                score = self.analyzer.polarity_scores(text)["compound"]

                if score >= 0.05:
                    yield "positive", 1
                elif score <= -0.05:
                    yield "negative", 1
                else:
                    yield "neutral", 1

        except Exception:
            pass

    def reducer(self, sentiment, counts):
        yield sentiment, sum(counts)

if __name__ == "__main__":
    MRSentimentAnalysis.run()