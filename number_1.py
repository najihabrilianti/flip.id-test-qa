db_transaction = [['011','Smith','BCA','BRI',1000000],['100','John','BRI','BCA',1000000],['101','Fulan','Mandiri','BCA',4333011],['110','Sri','BNI','BSI',3000000],['111','Bambang','BCA','BSI',1500000]]
dash_admin = [['001','Smith','BCA','BRI',1000000],['100','John','BRI','BCA',None],['101','Fulan','Mandiri','BCA',4000000],['110','Sri','BNI','BSI',3000000],['111','Bambang','BCA','BSI',1500000]]

for data in db_transaction :
    dash_index = db_transaction.index(data)
    if data == dash_admin[dash_index] :
        print ('pass')
    else :
        print ('failed')