from response import Response
from checkUser import check_user
def separate_responses(data):
    responses=[]
    list_of_users=[]
    for i in range (0,len(data['survey_result_detail']["themes"])):
        x=data['survey_result_detail']["themes"][i]['questions']
        for j in range(0,len(x)):
            l=x[j]["survey_responses"]
            for k in l:
                response=Response(k['respondent_id'],k['question_id'],k['response_content'])
                responses.append(response)
                user=check_user(k['respondent_id'], list_of_users)
                if k['response_content']!='':
                    user.question_count+=1
                    user.sum_rate+=int(k['response_content'])
                    
    return responses,list_of_users