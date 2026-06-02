from mrjob.job import MRJob
import json

class MRAverageRating(MRJob):

    def mapper(self, _, line):
        try:
            review = json.loads(line)
            asin = review['asin']
            rating = review['rating']

            yield asin, rating   # ONLY emit rating

        except:
            pass

    def reducer(self, key, values):
        ratings = list(values)

        total = sum(ratings)
        count = len(ratings)

        if count > 0:
            yield key, total / count


if __name__ == "__main__":
    MRAverageRating.run()


