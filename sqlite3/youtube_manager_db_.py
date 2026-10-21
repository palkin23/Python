import sqlite3

connection=sqlite3.connect("youtube.db")

cursor=connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
   cursor.execute("SELECT * FROM videos")   #* means select all columns
   for row in cursor.fetchall():       #fetchall() selects all data of rows
      print(row)

def add_video(name,time):
   cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
   connection.commit() #this is used to save the changes permanently in your database

def update_video(video_id,new_name,new_time):
   cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(new_name, new_time, video_id))
   connection.commit()

def delete_video(video_id):
   cursor.execute("DELETE FROM videos WHERE id=?",(video_id))
   connection.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ")
        
        #here instead of match , we have take if elif else(do any)
        
        if choice=='1':
           list_videos()
        
        elif choice=='2':
           #you can take input here also
           #i/p can be taken in function also
           name=input("Enter the video name: ")
           time=input("Enter the video time: ")
           add_video(name,time)
        
        elif choice=='3':
           video_id=input("Enter the video id to update")
           name=input("Enter the video name: ")
           time=input("Enter the video time: ")
           update_video(video_id,name,time)
       
        elif choice=='4':
           video_id=input("Enter video id to delete: ")
           delete_video(video_id)
       
        elif choice=='5':
           break
        
        else:
           print("InVAlid OPtiON")
    
    #good for memory to close the connection after finshing work in the while loop
    connection.close()
if __name__==("__main__"):
      main()