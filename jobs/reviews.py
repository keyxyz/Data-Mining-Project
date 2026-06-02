from mrjob.job import MRJob
import json

class MRReviewsCount(MRJob):

    def mapper(self, _, line):
        try:
            review = json.loads(line)
            asin = review.get('asin')
            if asin:
                yield asin, 1
        except json.JSONDecodeError:
            pass

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    MRReviewsCount.run()