class User:
    def __init__(self, repondent_id):
        self.id= repondent_id
        self.question_count=0
        self.sum_rate=0
    def average_question(self,max_q):
        return self.question_count/max_q
    def participation_rate(self):
        if self.question_count!=0:
            return self.sum_rate/self.question_count
        else:
            return 0