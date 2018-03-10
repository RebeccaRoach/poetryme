'''
analysis of the recommendation system pilot


format of the data is:
pilot name/base poem/base score/recommended poem/similarity/liking

pilot name: name of person
base poem: a poem the pilot liked that we used to recommend other poems
base score: how much the pilot likes the base poem
recommmended poem: the poems algorithmically similar to the base poem
similarity: similarity measure in absolute terms of recommended poem to base
liking: how much the pilot liked the recommended poem

if our recommendation system works then we expect to see a positive
correlation between similarity and liking.

because we have not weighted any of our features they are currently all of
equal importance. It is worthwhile to determine optimal weightings for 
features.

the relation between similarity and liking need not be linear. Any positive
monotonic relation will be considered a success. we will investigate linear
correlations first as they are simplest.

'''

import numpy as np
import matplotlib.pyplot as plt
#from tkinter import askopenfilename

#poem_scores = askopenfilename("")

#poem_scores = np.loadtxt("Pilot Analysis - Sheet1.csv", skiprows=1, usecols=[0,1,2,3,4,5],dtype=str)
# np.loadtxt is eating shit so read in the file the old fashioned way
poem_scores = []
with open("Pilot Analysis - Sheet1.csv", 'r') as poem_file:
	fields = poem_file.readline().split(',')
	for line in poem_file:

		entry = line.rstrip().split(',')# this sometimes splits on commas in titles

		if entry[-1].startswith('Estimated') or entry[-1]=='':
			entry.pop()

		# re assemble titles if they were accidentally split by a comma
		if len(entry)==7: # only one title was split
			# check if base poem title was split
			if entry[1].startswith('\"') and not entry[1].endswith('\"'):
				new_entry = [entry[0], entry[1]+entry[2]]
				#print('len(entry)',len(entry))
				new_entry.extend( [entry[i] for i in range(3,len(entry)) ] )
				entry = new_entry
				#print(entry)
				# seems ok
			# check if recommended poem title was split 	
			elif entry[3].startswith('\"') and not entry[3].endswith('\"'):
				#print("original entry", entry)
				new_entry = [entry[i] for i in range(3)]
				#print("first 2 cols", new_entry)
				new_entry.extend([entry[3]+entry[4]])
				#print("first 2 and concatenated",new_entry)
				new_entry.extend( [entry[i] for i in range(5,len(entry)) ] )
				entry = new_entry
				#print('final', entry)

			else:
				print('huh?')
				print(entry)
				#entry = new_entry

		if len(entry)==8: # both titles were split
			new_entry = [entry[0],
						entry[1]+entry[2],
						entry[3],
						entry[4]+entry[5],
						entry[6]]
			entry = new_entry

		poem_scores.append(entry)

	poem_file.close()

# drop any entries that have NA
poem_scores = [poem_scores[i] for i in range(len(poem_scores)) if poem_scores[i][4] != 'NA']

# drop any entries that have *** as a ranking
poem_scores = [poem_scores[i] for i in range(len(poem_scores)) if poem_scores[i][5] != '***']


# first lets look at the total stats of all piolots
similarity = [int(poem_scores[i][4]) for i in range(len(poem_scores))]
rankings = [float(poem_scores[i][5]) for i in range(len(poem_scores))]

plt.figure()
plt.plot(similarity, rankings, 'x')
pearson_product_moment = np.corrcoef(similarity, rankings)
r2 = pearson_product_moment[0,1]
print(pearson_product_moment)
plt.title("correlation between similarity score & liking %0.3f" %r2)
plt.xlabel("similarity to base poem")
plt.ylabel("reader rankings")


# now lets look at individuals
pilots = [poem_scores[i][0] for i in range(len(poem_scores))] 
pilot_set = list(set(pilots))
#markers = ['b.','kx','co','+','d','h','^','>','<','v','*','s','p']
#pilot_markers = {pilot_set[i]:markers[i] for i in range(len(pilot_set))}
#print(pilot_markers)

plt.figure()
index = 1
for pilot in pilot_set:
	a = [poem_scores[i] for i in range(len(poem_scores)) if poem_scores[i][0]==pilot]
	similarity = [int(a[i][4]) for i in range(len(a))]
	rankings = [float(a[i][5]) for i in range(len(a))]
	pearson_product_moment = np.corrcoef(similarity, rankings)
	r2 = pearson_product_moment[0,1]
	plt.subplot(3,5,index)
	plt.plot(similarity, rankings, 'x')
		
	plt.title("%s  %0.3f" %(pilot,r2))
	plt.xlabel("similarity to base poem")
	plt.ylabel("reader rankings")
	index += 1


'''
'''
plt.subplots_adjust(hspace=0.5)
#plt.tight_layout()
plt.show()