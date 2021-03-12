def search(keywords, captions):  # checking if the keyword is present in the csv
    count = 1
    for i in captions.index:
        for keyword in keywords:
            if captions["Caption"][i].find(keyword) != -1:
                count += 1
                if count > 0 and count <= len(keywords):
                    print(captions["Time"][i], captions["Camera"][i])
