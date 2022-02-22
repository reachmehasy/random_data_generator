# https://github.com/reachmehasy/random_data_generator
import json
import random
from random import randint

def datagenerate():
    parsed = []
    with open("dynamodb_data.json", 'wt', newline='') as jsonFile1:
        for i in range(records):
# brkg_id            
            account_id = i+1000
            brkg_acct_no =  randint(1, 1000000000)
            rep_cd = random.choice(rep_code)
            opt_eff_bgn_dt = random.choice(ran_bgn_dt)
            ser_acct_stat_cd = random.choice(ran_act_st_cd)            
            opt_perm_cd = random.choice(ran_opt_prem_cd)
#position data            
            pos_id = random.choice(ran_pos_ids) 
            quantity = randint(1,1000)
            inst_id = randint(1, 1000000000)
            post_dt = random.choice(ran_bgn_dt)
# post_sec_lock         
            lock_box_cd = random.choice(ran_loc_box_cd)
            shr_qty = randint(1, 1000)
            final_ref = {
                    "act_id" : account_id,
                    "b_act_no" : brkg_acct_no,
                    "reppy_cd" : rep_cd,
                    "opt_eff_bgn_dt" : opt_eff_bgn_dt,                
                    "ser_stat_cd" : ser_acct_stat_cd,
                    "opt_perm_cd": opt_perm_cd,
                    "pos_id" : pos_id,
                    "qty" : quantity,
                    "inst_id" : inst_id,                
                    "pos_dt" : post_dt,
                    "M": 
                        {
                            "locx":random.choice(ran_loc_box_cd),
                            "shr_qty":random.choice(ran_loc_box_cd)
                        }
                    }
            parsed.append(final_ref)
        jsonFile1.write(str(parsed))
            

            
    
if __name__ == '__main__':
    
# Total records count    
    records = 20
    
# Random values in list    
    rep_code = ['CORS','TEST','COLA','MENT','CORA','ISLA']
    ran_opt_prem_cd = ['FEMA','FICCI','FLAS','VISA','MESA','ISRO']
    ran_act_st_cd = ['ARIM','CFRA','CGRA','CDBS','CRAR','DBOD','BPSD','BSCS','BPM5']
    ran_bgn_dt = ['2013-06-23','2001-07-31','2012-09-16','1981-09-14','1971-04-19','2010-09-04','2019-02-14','2011-01-16']   
    ran_pos_ids = ['721048399','596228913','402311738','477445201','264045163','509973900','894636599','885715239','669530249','669530249','390317118','625054547','552669937','171509076']
    ran_loc_box_cd = ['XfPuf33nxqGBIJpIU7RCZsQh36fpAgWJzkK91i2v','ObArl18XuDcfXzaOjLml3VVkSoTzMQrx9QzQAFE1','UuGywETZAYn13TgvSGuE4yCrWiH6GHjkQIg54iYq','JfhlRxbE9ii7gtWKFXjGjd41j9MwpItSaehPLhsI','rWz5fleWsFbZ2Gf1Uoin3MKmP4wWZzKBbQOq7Jca','20iqQMGnFfdZlXKGh0CC098IIFIaDW5oEpflJcjn']
    
    datagenerate()
    
    
    print("JSON generation complete!")
