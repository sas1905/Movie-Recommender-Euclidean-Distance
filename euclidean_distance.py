from dataset_file import dataset
import math

def similarity_score(person1,person2):
	
	# Returns ratio Euclidean distance score of person1 and person2 
 
	both_watched = {}		# To get both rated items by person1 and person2
 
	for movie in dataset[person1]:
		if movie in dataset[person2]:
			both_watched[movie] = 1
 
		# Conditions to check they both have an common rating items	
		if len(both_watched) == 0:
			return 0
 
		# Finding Euclidean distance 
		eclidean_distance_sum = []	
 
		for item in dataset[person1]:
			if item in dataset[person2]:
				eclidean_distance_sum.append((dataset[person1][item] - dataset[person2][item])*(dataset[person1][item] - dataset[person2][item]))
		sum_of_eclidean_distance = sum(eclidean_distance_sum)
 
		return 1/(1+math.sqrt(sum_of_eclidean_distance))

def pearson_correlation(person1,person2):

     both_watched={}
    
     for movie in dataset[person1]:
        if movie in dataset[person2]:
            both_watched[movie]=1

     if len(both_watched) == 0:
            return 0

    
    # Add up all the preferences of each user
     person1_preferences_sum = sum([dataset[person1][movie] for movie in both_watched])
     person2_preferences_sum = sum([dataset[person2][movie] for movie in both_watched])    

    # Sum up the squares of preferences of each user
     person1_square_preferences_sum = sum([pow(dataset[person1][movie],2) for movie in both_watched])
     person2_square_preferences_sum = sum([pow(dataset[person2][movie],2) for movie in both_watched])

    # Sum up the product value of both preferences for each item
     product_sum_of_both_users = sum([dataset[person1][movie] * dataset[person2][movie] for movie in both_watched])

    # Calculate the pearson score
     numerator_value = product_sum_of_both_users - (person1_preferences_sum*person2_preferences_sum/len(both_watched))
     denominator_value = math.sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/len(both_watched)) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/len(both_watched)))

     if denominator_value == 0 :
         return 0
     else :
         r = numerator_value/denominator_value
         return r







