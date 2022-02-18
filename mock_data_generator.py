import csv
import random

def datagenerate(headers1,headers2,headers3):

    with open("brkg.csv", 'wt') as csvFile,open('pos_brkg.csv','wt') as posFile,open('pos_sec_loc.csv','wt') as posSecFile:
        writer1 = csv.DictWriter(csvFile, fieldnames=headers1)
        writer2 = csv.DictWriter(posFile, fieldnames=headers2)
        writer3 = csv.DictWriter(posSecFile, fieldnames=headers3)
        writer1.writeheader()
        writer2.writeheader()
        writer3.writeheader()
        
        for i in range(records):
# brkg_id            
            account_id = randint(1, 1000000000)
            brkg_acct_no =  randint(1, 1000000000)
            rep_cd = random.choice(rep_code)
            opt_eff_bgn_dt = random.choice(ran_bgn_dt)
            ser_acct_stat_cd = random.choice(ran_act_st_cd)            
            opt_perm_cd = random.choice(ran_opt_prem_cd)
            
# post_brkg  
            pos_id = random.choice(ran_pos_ids)
            quantity = randint(1,1000)
            inst_id = randint(1, 1000000000)
            post_dt = random.choice(ran_bgn_dt)

# post_sec_lock         
            lock_box_cd = random.choice(ran_loc_box_cd)
            shr_qty = randint(1, 1000)
            
            writer1.writerow({
                    "acct_id" : account_id,
                    "brkg_acct_no" : brkg_acct_no,
                    "rep_cd" : rep_cd,
                    "opt_eff_bgn_dt" : opt_eff_bgn_dt,                
                    "ser_acct_stat_cd" : ser_acct_stat_cd,
                    "opt_perm_cd": opt_perm_cd
                    })

            writer2.writerow({
                    "acct_id" : account_id,
                    "acct_post_id" : pos_id,
                    "qty" : quantity,
                    "inst_id" : inst_id,                
                    "post_dt" : post_dt
                    })
            
            writer3.writerow({
                    "acct_post_id" : pos_id,
                    "box_loc_cd" : lock_box_cd,
                    "loc_shr_qty" : shr_qty
                    })            
            
            
    
if __name__ == '__main__':
    
# Total records count    
    records = 10
    
# Output file headers
    headers1 = ["acct_id", "brkg_acct_no","rep_cd","opt_eff_bgn_dt","ser_acct_stat_cd","opt_perm_cd"]
    headers2 = ["acct_id", "acct_post_id","qty","inst_id","post_dt"]
    headers3 = ["acct_post_id", "box_loc_cd","loc_shr_qty"]

# Random values in list    
    rep_code = ['CORS','TEST','COLA','MENT','CORA','ISLA']
    ran_opt_prem_cd = ['FEMA','FICCI','FLAS','VISA','MESA','ISRO']
    ran_act_st_cd = ['ARIM','CFRA','CGRA','CDBS','CRAR','DBOD','BPSD','BSCS','BPM5']
    ran_bgn_dt = ['2013-06-23','2001-07-31','2012-09-16','1981-09-14','1971-04-19','2010-09-04','2019-02-14','2011-01-16']   
    ran_pos_ids = ['721048399','596228913','402311738','477445201','264045163','509973900','894636599','885715239','669530249','669530249','390317118','625054547','552669937','171509076']
    ran_loc_box_cd = ['XfPuf33nxqGBIJpIU7RCZsQh36fpAgWJzkK91i2v','ObArl18XuDcfXzaOjLml3VVkSoTzMQrx9QzQAFE1','UuGywETZAYn13TgvSGuE4yCrWiH6GHjkQIg54iYq','JfhlRxbE9ii7gtWKFXjGjd41j9MwpItSaehPLhsI','rWz5fleWsFbZ2Gf1Uoin3MKmP4wWZzKBbQOq7Jca','20iqQMGnFfdZlXKGh0CC098IIFIaDW5oEpflJcjn']
    
    datagenerate(headers1,headers2,headers3)
    
    print("CSV generation complete!")
