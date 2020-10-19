import csv
from ayeApp.models import Invitation

with open('users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=">")
    for row in csv_reader:
        #print(f"owner {row[0]}, names {row[1]}, tel {row[2]} email {row[3]} inv {row[4]} \n")
        I = Invitation(invitation_owner_name=row[0], email=row[3], telephone=row[2],guest_names=row[1], number_of_guests=row[4])
        I.save()
