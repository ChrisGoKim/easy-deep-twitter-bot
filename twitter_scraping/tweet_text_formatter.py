


tweet_output = "frogdetective.txt"
formatted_output = "frogdetective_formatted.txt"
response = []

with open(tweet_output, 'r', encoding="utf-8") as original:
    with open(formatted_output, 'w', encoding="utf-8") as formatted:
        #Read each line in the original
        for line in original.readlines():
            if "==========" not in line:
                line_list = line.strip().split(" ")
                removeIndexList = []
                #Removing any '@tag' from all words in a sentence
                if "@" in line:
                    #Marking all words that start with '@' in a sentence
                    for i, l in enumerate(line_list):
                        if l[0] == "@":
                            removeIndexList.append(i)
                    #Deleting all these words in reverse order so we don't throw off the indices
                    for i in sorted(removeIndexList, reverse=True):
                        del line_list[i]
                
                #Reset the removeIndex
                removeIndexList = []
                if "http" in line:
                    #Marking all words that have 'http'
                    for i, l in enumerate(line_list):
                        if "http" in l:
                            removeIndexList.append(i)
                    #Deleting all these words in reverse order so we don't throw off the indices
                    for i in sorted(removeIndexList, reverse=True):
                        del line_list[i]

                #Append final response to list
                final_list = ' '.join(line_list)
                response.append(str(final_list))

            else:
                #'==========' lines that just get appended
                response.append("\n==========\n")
        formatted.writelines(response)



