from separateResponses import separate_responses
from table import draw_table
def output(data):    
    responses,list_of_users=separate_responses(data)
    def max_question(responses):
        max_q=0
        for response in responses:
            if max_q<int(response.id_q):
                max_q=int(response.id_q)
        return max_q
    max_q=max_question(responses)
    list_output=[]
    for user in list_of_users:
        list_output.append([user.id, user.average_question(max_q),user.participation_rate()])
    draw_table(list_output)
