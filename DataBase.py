import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect('todo.db')
        self.cursor = self.con.cursor()
        self.create_task_table() #create the tasks table

    def create_task_table(self):
        """Create tasks table"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id integer PRIMARY KEY AUTOINCREMENT, task varchar(50) NOT NULL, value integer, completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)), day TEXT)")
        self.con.commit()

    def create_task(self, task, value=None, day='monday'):
        """Create a task"""
        self.cursor.execute("INSERT INTO tasks(task, value, completed, day) VALUES(?, ?, ?, ?)", (task, value, 0, day))
        self.con.commit()

        # GETTING THE LAST ENTERED ITEM SO WE CAN ADD IT TO THE TASK LIST
        created_task = self.cursor.execute("SELECT id, task, value FROM tasks WHERE task = ? and completed = 0", (task,)).fetchall()
        return created_task[-1]

    def get_tasks(self):
        """Get all completed and uncomplete tasks"""
        tasks = self.cursor.execute("SELECT id, task, value, day, completed FROM tasks").fetchall()
        # return the tasks to be added to the list when the application starts
        return tasks



    def mark_task_as_complete(self, taskid):
        """Mark tasks as complete"""
        self.cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (taskid,))
        self.con.commit()

    def mark_task_as_incomplete(self, taskid):
        """Mark task as uncomplete"""
        self.cursor.execute("UPDATE tasks SET completed=0 WHERE id=?", (taskid,))
        self.con.commit()

        # return the task text
        task_text = self.cursor.execute("SELECT task FROM tasks WHERE id=?", (taskid,)).fetchall()
        return task_text[0][0]

    def delete_task(self, taskid):
        """Delete a task"""
        self.cursor.execute("DELETE FROM tasks WHERE id=?", (taskid,))
        self.con.commit()

    def close_db_connection(self):
        self.con.close()

    def delete_db(self):
        self.cursor.execute("DROP TABLE tasks")


class Database2:
    def __init__(self):
        self.con = sqlite3.connect('quest.db')
        self.cursor = self.con.cursor()
        self.create_quest_table() #create the tasks table

    def create_quest_table(self):
        """Create tasks table"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS quests(id integer PRIMARY KEY AUTOINCREMENT, quest varchar(50) NOT NULL, value integer, date TEXT)")
        self.con.commit()

    def create_quest(self, quest, value=None, date=''):
        """Create a task"""
        self.cursor.execute("INSERT INTO quests(quest, value, date) VALUES(?, ?, ?)", (quest, value, date))
        self.con.commit()

        # GETTING THE LAST ENTERED ITEM SO WE CAN ADD IT TO THE TASK LIST
        created_task = self.cursor.execute("SELECT id, quest, value FROM quests WHERE quest = ?", (quest,)).fetchall()
        return created_task[-1]

    def get_quests(self):
        """Get all completed and uncomplete tasks"""
        quests = self.cursor.execute("SELECT id, quest, value, date FROM quests").fetchall()
        # return the tasks to be added to the list when the application starts
        return quests



    def delete_quest(self, taskid):
        """Delete a task"""
        self.cursor.execute("DELETE FROM quests WHERE id=?", (taskid,))
        self.con.commit()

    def close_db_connection(self):
        self.con.close()

    def delete_db(self):
        self.cursor.execute("DROP TABLE quests")


class Database3:
    def __init__(self):
        self.con = sqlite3.connect('profile.db')
        self.cursor = self.con.cursor()
        self.create_profile_table() #create the tasks table

    def create_profile_table(self):
        """Create tasks table"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS profile(id integer PRIMARY KEY AUTOINCREMENT, name TEXT, title TEXT, grl TEXT, job TEXT, goal TEXT, law1 TEXT, law2 TEXT, law3 TEXT, law4 TEXT, law5 TEXT, law6 TEXT, law7 TEXT)")
        self.con.commit()

    def create_profile(self, name, title, grl, job, goal, law1, law2, law3, law4, law5, law6, law7):
        """Create a task"""
        self.cursor.execute("INSERT INTO profile(name, title, grl, job, goal, law1, law2, law3, law4, law5, law6, law7) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, title, grl, job, goal, law1, law2, law3, law4, law5, law6, law7))
        self.con.commit()

    def get_profile(self):
        """Get all completed and uncomplete tasks"""
        profile = self.cursor.execute("SELECT name, title, grl, job, goal, law1, law2, law3, law4, law5, law6, law7 FROM profile").fetchall()
        # return the tasks to be added to the list when the application starts
        return profile

    def close_db_connection(self):
        self.con.close()

    def delete_db(self):
        self.cursor.execute("DROP TABLE profile")



class Database4:
    def __init__(self):
        self.con = sqlite3.connect('level.db')
        self.cursor = self.con.cursor()
        self.create_level_table() #create the tasks table

    def create_level_table(self):
        """Create tasks table"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS level(lvl TEXT DEFAULT 1, value INTEGER DEFAULT 0, max INTEGER DEFAULT 1000)")
        self.con.commit()

    def create_level(self, lvl, value, max):
        """Create a task"""
        self.cursor.execute("INSERT INTO level(lvl, value, max) VALUES(?, ?, ?)", (lvl, value, max))
        self.con.commit()

    def get_lvl(self):
        """Get all completed and uncomplete tasks"""
        profile = self.cursor.execute("SELECT lvl, value, max FROM level").fetchall()
        # return the tasks to be added to the list when the application starts
        return profile

    def close_db_connection(self):
        self.con.close()

    def delete_db(self):
        self.cursor.execute("DROP TABLE level")


class Database5:
    def __init__(self):
        self.con = sqlite3.connect('data1.db')
        self.cursor = self.con.cursor()
        self.create_data_table() #create the tasks table

    def create_data_table(self):
        """Create tasks table"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data(id integer PRIMARY KEY AUTOINCREMENT, date INTEGER)")
        self.con.commit()

    def create_data(self, date):
        """Create a task"""
        self.cursor.execute("INSERT INTO data(date) VALUES(?)", (date,))
        self.con.commit()

    def get_data(self):
        """Get all completed and uncomplete tasks"""
        data = self.cursor.execute("SELECT id, date FROM data").fetchall()
        # return the tasks to be added to the list when the application starts
        return data

    def delete_date(self, taskid):
        """Delete a task"""
        self.cursor.execute("DELETE FROM data WHERE id=?", (taskid,))
        self.con.commit()

    def close_db_connection(self):
        self.con.close()

    def delete_db(self):
        self.cursor.execute("DROP TABLE data")