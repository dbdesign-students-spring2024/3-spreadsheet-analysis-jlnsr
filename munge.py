"""place your code to clean up the data file below."""
#this file contains 45 columns, all of which are NOT neccessary
#this py program will ommit some of the superflous categories (i.e columns)
#hence perform a reduction of fields

with open("data/Tree_data.csv","r") as file:
    all_data = file.readlines()
    all_data = [i.split("\t") for i in all_data]
    all_data = [ [string.strip() for string in line] for line in all_data]
    data_dict = {i[0]:i[1:] for i in all_data} ##SKIP the first line of fields, include only the data, where i[0] is the UNIQUE IDENTIFIER and i[1:] is the actual data

    fields = [field for field in all_data[0]] # list of ALL fields, this program will remove unneccessary fields
    removed_fields = [] #list of REMOVED fields

    for key,record in list(data_dict.items()): #iterate through the VALUES of the dictionary, lists containing the values of each field
        if key == "": #remove empty keys
            del data_dict[key]
        for index,(field,value) in enumerate(zip(fields[1:],record.copy())): #removing irrelevant/unneccessary fields, starting from 'block_id' so the fields allign with the values
            if field == "created_at":
                record[ record.index(value) ] = value[:10] #only keep the DATE (i.e. 2015-09-27), removing everything thereafter
            elif field == "steward":
                record[index] = "---"
                removed_fields += [field]
            elif field == "guards":
                record[index] = "---"
                removed_fields += [field]
            elif field == "user_type":
                record[index] = "---"
                removed_fields += [field]
            elif "root" in field:
                record[index] = "---" 
                removed_fields += [field]
            elif "trnk" in field:
                record[index] = "---" 
                removed_fields += [field]
            elif ("brch" in field) and (field != "brch_shoe"): #remove fields with 'brch' EXCEPT for 'brch_shoe'
                record[index] = "---"
                removed_fields += [field]
            elif "code" in field: #remove 'postcode' AND 'borocode'
                record[index] = "---"
                removed_fields += [field]
            elif field == "cncldist":
                record[index] = "---"
                removed_fields += [field]
            elif (field == "st_assem") or (field == "st_senate"):
                record[index] = "---"
                removed_fields += [field]
            elif "nta" in field:
                record[index] = "---"
                removed_fields += [field]
            elif field == "boro_ct":
                record[index] = "---"
                removed_fields += [field]
            elif field == "state":
                record[index] = "---"
                removed_fields += [field]
            elif "tude" in field:
                record[index] = "---"
                removed_fields += [field]
            elif field == "bbl":
                record[index] = "---"
                removed_fields += [field]
            elif field == "bin":
                record[index] = "---"
                removed_fields += [field]
            elif field == "census tract":
                record[index] = "---"
                removed_fields += [field]
            elif field == "council district":
                record[index] = "---"
                removed_fields += [field]
            elif field == "community board":
                record[index] = "---"
                removed_fields += [field]
            elif field == "zip_city":
                record[index] = "---"
                removed_fields += [field]
            elif field == "y_sp" or field == "x_sp":
                record[index] = "---"
                removed_fields += [field]
    for record in data_dict.values(): #once the irrelevant values are replaced with a string that clearly identifies they should be removed (i.e. "---"), REMOVE them
        for value in record.copy():
            if value == "---":
                record.remove(value)
            elif "," in value:
                record[ record.index(value) ] = value.replace(",","")

    spc_common = [] #a list of all the species of tree in this dataset
    for record in list(data_dict.values())[1:]: #starting at the first instance of data, NOT the field
        if (record[8] not in spc_common) and record[8] != "": #no duplicates, no empty strings
            spc_common += [record[8]]
    print(len(spc_common))

with open("clean_data.csv", "w") as output:
    line = ""
    for key,record in data_dict.items():
        line += key+","
        for value in record:
            if record.index(value) == len(record)-1:
                line += value + "\n"
            else:
                line += value + ","
        output.write(line)
        line = ""   

