# File: models.py
# Author: Jocelyn Chan (jchan042@bu.edu) 3/18/2026
# Description: Used to define the DB structure/schema

from django.db import models

# Create your models here.

# Voter model 
class Voter (models.Model):
    '''
    Store/represent the data from one voter in Newton, MA 
    Last Name, First Name, Residential Address - Street Number,
    Residential Address - Street Name, Residential Address - Apartment Number, 
    Residential Address - Zip Code, Date of Birth, Date of Registration, Party Affiliation,
    Precinct Number, v20state, v21town, v21primary, v22general, v23town, voter_score

    '''
    
    # fields for voter model 
    last_name = models.TextField()
    first_name = models.TextField()
    street_number = models.IntegerField()
    street_name = models.TextField()
    apt_number = models.TextField(blank=True) #some have letters at the end 
    zip_code = models.IntegerField()
    dob = models.DateField()
    registration_date = models.DateField()
    party = models.CharField(max_length=2) # 2 chars 
    precinct = models.IntegerField()
    
    # fields needed for voter score 
    v20 = models.BooleanField()
    v21_town = models.BooleanField()
    v21_primary = models.BooleanField()
    v22_general = models.BooleanField()
    v23 = models.BooleanField()
    voter_score = models.IntegerField()
    
    
    # string representation of Voter model 
    def __str__(self):
        '''Return a string representation of this model instance'''
        return f'{self.last_name}, {self.first_name}. Party: {self.party} in precinct {self.precinct}.'


# function to process CSV files and load voters into DB 
def load_data():
    '''
    Function to load data records from CSV file into Django model instance
    '''
    
    # load csv file 
    filename = 'C:/Users/jocel/django/newton_voters.csv'
    f = open(filename, 'r') # open file for reading 
    f.readline()
    
    # read entrie file one line at a time 
    for line in f:
        
        try: 
            fields = line.strip().split(',') # separated by commas
            
            # column positions
            result = Voter(last_name=fields[1], # start at 1 because of voter ID
                            first_name=fields[2],
                            street_number=fields[3],
                            street_name=fields[4],
                            apt_number=fields[5],
                            zip_code=fields[6],
                            dob=fields[7],
                            registration_date=fields[8],
                            party=fields[9].strip(), # 2 char field 
                            precinct=fields[10],
                            
                            v20=fields[11] == 'TRUE',
                            v21_town=fields[12] == 'TRUE',
                            v21_primary=fields[13] == 'TRUE',
                            v22_general=fields[14] == 'TRUE',
                            v23=fields[15] == 'TRUE', 
                            voter_score=fields[16],
                            )
            result.save() # commit this result to DB 
            print('Run complete')
        except:
            # error message
            print('Something went wrong :(')
            print(f'line={line}')
            
    # confirmation
    print(f'Created {len(Voter.objects.all())} results')
    
