import csv

def rating_category(rating):
    rating = int(rating)
    if rating <=3:
         category = 'bad one'
    elif rating <=4:
         category = "decent one"
    else:
         category = 'good one'
    return category

modified_rating_categories = []
with open("jokes.csv", "r") as f:
     csv_reader = csv.reader(f)
     headers = next(csv_reader) # ignore the headers for the file 
     headers.append('rating_category')
     for row in csv_reader:
          print(rating_category(row[2])) 
          modified_rating_categories.append(row)


with open("modified_rating_categories.csv", "w", newline="") as new_csv:
    csv_writer = csv.writer(new_csv)
    csv_writer.writerow(modified_rating_categories)