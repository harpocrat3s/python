# This Python script searches for the given keywords on Google, filters the results 
# based on two exclude lists, and prints the remaining websites.

# I developed this script during my time working in Digital Marketing, aiming to 
# automate a common daily task using my newly acquired Python knowledge.

# The keywords.txt file contains a list of keywords that will be used for querying Google.
# The exclude_list.txt file contains a list of websites that are not relevant to us 
# (e.g., Amazon) and should be excluded from the results.
# The affiliate.txt file contains a list of affiliate websites. In the results, affiliate 
# sites will be highlighted with ** before and after the URL to easily identify them. 
# This allows me to track the presence of affiliates on the first page of Google and monitor 
# any changes.

# IMPORTANT: Ensure that the .txt files do not have empty lines before or after the keywords. 
# If the results are empty (assuming the script is functioning correctly), check for any empty 
# lines in the list (e.g., at the bottom of the file).


try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

from re import search as regexsearch

print('\n')

def queryGoogle(query):
    #Queries Google, pass a str and returns a list of str with SERPs results
    serpsTemp = []
    for j in search(query.strip(), tld="com", num=20, stop=20, pause=2):
        serpsTemp.append(j)
    return serpsTemp

def createListFromFile(fileName):
    #passed parameter must be a str, returns a list of str
    #open list file
    temp_list = open(fileName, 'r')
    file_list = []
    print(fileName)
    for line in temp_list:
        strippedLine = line.strip()
        if not strippedLine.startswith(("#", "-")):
            file_list.append(strippedLine)
            print(strippedLine)
    temp_list.close()
    print('\n')
    return file_list

def printListOfProspect(serps, keyword, exclude_list, affiliate_list):
    #Iterate the serps results
    final_list = []

    for result in serps:
        found = False

        #Iterate the exclusion list
        for domain in exclude_list:

            #If the domain is in the exclusion list do nothing
            if regexsearch(domain, result):
                found = True
                break

        for domain in affiliate_list:
            #If the domain is in an affiliate add it to the list
            #with some ** to make them standing out
            if regexsearch(domain, result):
                final_list.append(f'** {result} **')
                found = True


        #If the domain is not on the exlusion list, or affiliate list,
        #Add the domain to the final list
        if found == False:
            final_list.append(result)

    print('\n')

    print(f'Prospects for {keyword}: ')
    for site in final_list:
        print(site)
    print('\n')

keywordList = createListFromFile('keywords.txt') #list file of keywords str
exclude_list = createListFromFile('exclude_list.txt')
affiliate_list = createListFromFile('affiliates.txt')


for keyword in keywordList:
    serps = queryGoogle(keyword)
    printListOfProspect(serps, keyword, exclude_list, affiliate_list)
    serps.clear()
