from mrjob.job import MRJob
import json
from mrjob.step import MRStep


class MRHelpfulness(MRJob):

    def mapper(self, _, line):
        try:
            review = json.loads(line)
            vote = review.get('helpful_vote')
            if vote == 0:
                yield 'unhelpful', 1
            else:
                yield 'helpful', 1
        except json.JSONDecodeError:
            pass

    def reducer(self, vote, values):
        yield None, (vote, sum(values))

    def reducerAvg(self, _, values):
        helpful = 0
        unhelpful = 0

        for vote , count in values:
            if vote ==  "helpful":
                helpful = count
            else:
                unhelpful = count

        total = helpful + unhelpful

        avg = helpful/total

        yield "ave_helpful_score", avg

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer= self.reducerAvg)       
        ]

if __name__ == "__main__":
    MRHelpfulness.run()
