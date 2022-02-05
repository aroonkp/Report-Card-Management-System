import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def Admin():
    while True:
        print('Enter the choice')
        print('1.Whole class Rankings')
        print('2.Enter New Record')
        print('3.Edit Existing Record')
        ch = input()
        if(ch == '1'):
            class_ranking()
        elif(ch == '2'):
            new_rec()
        elif(ch == '3'):
            edit_rec()
        else:
            print('Wrong choice')



def Student():
    while True:
        print('Enter the choice')
        print('1.View your detailed marks')
        print('2.Whole class Rankings')
        ch = input()
        if(ch == '1'):
            detailed_marks()
        elif(ch == '2'):
            class_ranking()
        else:
            print('Wrong choice')


def detailed_marks():
    sem = input('Enter your semester')
    file_name = 'student' +sem +'.csv'
    data = pd.read_csv(file_name , index_col= 'usn')
    usn = input('Enter your USN')
    if usn in data.index:
        marks = np.array(data.loc[usn])
        sub_file = 'SEM'+sem+'.csv'
        subject = pd.read_csv(sub_file , delimiter = ',' , index_col = 'INDEX')
        subject['Marks'] = marks[1:]
        print(subject)
    else:
        print('Record not found')
 
def class_ranking():
    sem = input('Enter your semester')
    file_name = 'student' +sem +'.csv'
    data = pd.read_csv(file_name , index_col= 'usn')
    rank = data.sort_values('Total' , ascending=False)
    print(rank[['Total' , 's1',  's2',  's3',  's4' , 's5',  's6' , 's7',  's8']])
def new_rec(): 
    sem = input('Please enter the semester')
    usn = input('Please enter the usn')
    rec_file = 'student' +sem +'.csv'
    sub_file = 'SEM'+sem+'.csv'
    rec_df = pd.read_csv(rec_file )
    sub_df = pd.read_csv(sub_file)
    if usn in rec_df.index:
        print('Data is already present')
        return
    else:
        print('Enter the marks of student')
        marks = []
        
        for subject in sub_df.SUB_CODE:
            print(subject)
            marks.append(int(input()))
        marks.append(sum(marks))
        sub_df['Marks'] = np.array(marks[:-1])
        print(sub_df)
        marks.insert(0,usn)
        dictt = {'usn':[marks[0]], 's1':[marks[1], ], 's2':[marks[2],],  's3':[marks[3] , ], 's4':[marks[4],],  's5':[marks[5],],
                        's6':[marks[6],], 's7':[marks[7],], 's8':[marks[8],] , 'Total':[marks[-1],]}

        new_data = pd.DataFrame.from_dict(dictt)
        rec_df = rec_df.append(new_data)
        rec_df.reset_index(inplace=True)
        rec_df = rec_df[['Total' , 's1',  's2',  's3',  's4' , 's5',  's6' , 's7',  's8'  , 'usn']]
        rec_df.to_csv(rec_file , index=False )

def edit_rec(): 
    sem = input('Please enter the semester')
    usn = input('Please enter the usn')
    rec_file = 'student' +sem +'.csv'
    sub_file = 'SEM'+sem+'.csv'
    rec_df = pd.read_csv(rec_file , index_col= 'usn' )
    rec_df.index =  rec_df.index.map(str)
    sub_df = pd.read_csv(sub_file)
    if usn not in rec_df.index:
        print('Data not present')
        return
    else:
        print('Enter the marks of the student')
        marks = []
        
        for subject in sub_df.SUB_CODE:
            print(subject)
            marks.append(int(input()))
        marks.append(sum(marks))
        sub_df['Marks'] = np.array(marks[:-1])
        print(sub_df)
        marks.insert(0,usn)

        rec_df.loc[usn , 's1'] = marks[1]
        rec_df.loc[usn , 's2'] = marks[2]
        rec_df.loc[usn , 's3'] = marks[3]
        rec_df.loc[usn , 's4'] = marks[4]
        rec_df.loc[usn , 's5'] = marks[5]
        rec_df.loc[usn , 's6'] = marks[6]
        rec_df.loc[usn , 's7'] = marks[7]
        rec_df.loc[usn , 's8'] = marks[8]
        rec_df.loc[usn , 'Total'] = marks[-1]
        rec_df.reset_index(inplace=True)
        rec_df = rec_df[['Total' , 's1',  's2',  's3',  's4' , 's5',  's6' , 's7',  's8' , 'usn']]
        rec_df.to_csv(rec_file , index=False )


print('\n\t\t\t\tWELCOME\t')
print('\t\tStudnt Report Card Management System \t\t')
print()
print()
print('Enter you choice\n1.Admin\n2.Student')
user = input()
if(user == '2'):
    while True:
        Student()
else:
    while True:
        print('Enter your password')
        pw = input()
        if(pw == 'Admin'):   
            Admin()
        else:
            print('Wrong password try again')

    

