import json
import matplotlib.pyplot as plt
import utils

#main file for testing extent to which people can shift the features of what comes to mind

data_path = '../wctm_data/'

if __name__ == "__main__": 
    #load response data from intrusion study
    #from this data, we want to get response counts for each feature
    with open(data_path + 'study5/responses.json') as f:
        intrusion_responses = json.load(f)
        
    #load response data from study 1
    #we'll compare ft ratings for these responses to ft ratings for the intrusion responses
    with open(data_path + 'study1/response_counts.json') as f:
        general_response_counts = json.load(f)
        
    #load ft ratings from study 3
    #we'll use this to score ppls responses
    with open(data_path + 'study3/ratings.json') as f:
        ft_ratings = json.load(f)
    
    #go thru each category
    for cat, cat_trials in intrusion_responses.items():
        #go thru each response
        for trial in cat_trials:
            #what we care about here are the considerations and responses, aka what came to mind
            responses = []
            for c in trial["considerations"] + [trial["response"]]:
                #deal w special cases and null response
                if c.lower().strip() in ["lions/tigers", "alligators/crocodiles"]:
                    responses.append(utils.code_response(cat, c.split("/")[0])) 
                    responses.append(utils.code_response(cat, c.split("/")[1])) 
                    continue
                coded_response = utils.code_response(cat, c)
                if coded_response != None:
                    responses.append(coded_response) 
            #remove repeats
            responses = list(set(responses))

            