from mrjob.job import MRJob
import json
from mrjob.step import MRStep

class MRTop10Products(MRJob):

    def mapper(self, _, line):
        try:
            review = json.loads(line)
            asin = review.get('asin')
            if asin:
                yield asin, 1
        except json.JSONDecodeError:
            pass

    def reducer(self, asin, values):
        yield None, (asin, sum(values))

    def reduceTopTen(self, _, values):
        top = sorted(values, reverse=True)[:10]
        for asin, count in top:
            yield asin, count

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer= self.reduceTopTen)       
        ]
if __name__ == "__main__":
    MRTop10Products.run()