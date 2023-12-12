import mysql.connector
conn_obj=mysql.connector.connect(host='localhost',
                         user='root',
                         password='shubhu@123',
                         database='mydata')
if conn_obj:
    print("Connection established")
else:
    print("Please try again")
#cursor object
cur_object=conn_obj.cursor()
def create_table():
    cur_object.execute("create table if not exists taskstable(task Text,task_status Text,task_due_date Date)")
conn_obj.commit()
def add_data(task,task_status,task_due_date):
    cur_object.execute('INSERT INTO taskstable(task,task_status,task_due_date)VALUES (%s,%s,%s)',(task,task_status,task_due_date))
    conn_obj.commit()

def view_all_data():
    cur_object.execute('select * from taskstable')
    data = cur_object.fetchall()
    return data

def view_unique_task():
    cur_object.execute('SELECT DISTINCT task FROM taskstable')
    data = cur_object.fetchall()
    return data

def get_task(task):
    cur_object.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
    data = cur_object.fetchall()
    return data
def edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date):
    cur_object.execute("UPDATE taskstable SET task =%s,task_status=%s,task_due_date=%s WHERE task=%s and task_status=%s and task_due_date=%s",(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date))
    conn_obj.commit()
    data = cur_object.fetchall()
    return data

def delete_data(task):
    cur_object.execute('DELETE FROM taskstable WHERE task = "{}"'.format(task))
    conn_obj.commit()
    

    