# https://github.com/reachmehasy/random_data_generator
import csv
import random
from random import randint

def datagenerate():

    with open("hunthousand.csv", 'w', newline='\n') as csvFile1:
        writer = csv.writer(csvFile1, delimiter='|')
        data_list=[]
        dl=[]
        for i in range(records):
#            
            c0 = 'A'
            c1 = 37
            c2 = randint(1, 5)
            c3 = randint(1, 10000000)
            c4 = '    ' 
            c5 = randint(1, 5)
            c6 = random.choice(r_code)
            c7 = '0'
            c8 = '            '
            c9 = ' '
            c10 = ' '
            c11 = '          '
            c12 = ' '
            c13 = '  '
            c14 = random.choice(ran_bgn_dt)
            c15 = ''
            c16 = ''
            c17 = '     '
            c18 = ' '
            c19 = '0'
            c20 = '0.00'
            c21 = ''
            c22 = '0'
            c23 = ' '
            c24 = '0'
            c25 = '0'
            c26 = '0'
            c27 = '0'
            c28 = ' '
            c29 = random.choice(ran_c29)
            c30 = '                        '
            c31 = '                        '
            c32 = '                        '
            c33 = '                        '
            c34 = '                        '
            c35 = ' '
            c36 = ' '
            c37 = '  '
            c38 = random.choice(ran_p_ids)
            c39 = random.choice(ran_a_ids)
            c40 = ' '
            c41 = '    '
            c42 = '    '
            c43 = 'N'
            c44 = 'N'
            c45 = 'Y'
            c46 = random.choice(ran_CDE)
            c47 = '         '
            c48 = '                          '
            c49 = random.choice(ran_o_p_cd)
            c50 = '   '
            c51 = ' '
            c52 = '0'
            c53 = ''
            c54 = '0.00000'
            c55 = ' '
            c56 = randint(1111111111111111111111,9999999999999999999999)
            c57 = ' '
            c58 = ' '
            c59 = randint(1111111111111111111111,9999999999999999999999)
            
#             
            dl=[str(c0),str(c1),str(c2),str(c3),str(c4),str(c5),str(c6),str(c7),str(c8),str(c9),str(c10),str(c11),str(c12),str(c13),str(c14),str(c15),str(c16),str(c17),str(c18),str(c19),str(c20),str(c21),str(c22),str(c23),str(c24),str(c25),str(c26),str(c27),str(c28),str(c29),str(c30),str(c31),str(c32),str(c33),str(c34),str(c35),str(c36),str(c37),str(c38),str(c39),str(c40),str(c41),str(c42),str(c43),str(c44),str(c45),str(c46),str(c47),str(c48),str(c49),str(c50),str(c51),str(c52),str(c53),str(c54),str(c55),str(c56),str(c57),str(c58),str(c59)]
            data_list.append(dl)
            writer.writerow(dl)

            
if __name__ == '__main__':
    
# Total records count    
    records = 10
    
# Random values in list    
    r_code = ['CORS','TEST','COLA','MENT','CORA','ISLA']
    ran_o_p_cd = ['FEM ','FIC ','LAS ','ISA ','SAQ ','ROL ']
    ran_act_st_cd = ['ARIM','CFRA','CGRA','CDBS','CRAR','DBOD','BPSD','BSCS','BPM5']
    ran_bgn_dt = ['2013-06-23','2001-07-31','2012-09-16','1981-09-14','1971-04-19','2010-09-04','2019-02-14','2011-01-16']   
    ran_p_ids = ['721048399','596228913','402311738','477445201','264045163','509973900','894636599','885715239','669530249','669530249','390317118','625054547','552669937','171509076']
    ran_a_ids = ['14520','22008','13062','22202']
    ran_CDE = ['C','D','E']
    ran_c29 = ['P & G CHG CLS 1         ','P & G CHG CLS 2         ','P & G CHG CLS 3         ','P & G CHG CLS 4         ','P & G CHG CLS 5         ']
    datagenerate()
    print("CSV generation complete!")
