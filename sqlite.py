import sqlite3


class Database(object):

	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute(
			"CREATE TABLE IF NOT EXISTS homes (id INTEGER PRIMARY KEY, Address TEXT, Area REAL, Beds INTEGER, Full Baths INTEGER, Half Baths INTEGER, Locality TEXT, Lot Size Text, Price TEXT)"
		)
		self.conn.commit()

	def insert(self, address, area, beds, baths, half_baths, locality, lot_size, price):
		self.cur.execute(
			"INSERT INTO homes VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (
				address, area,
				beds, baths,
				half_baths, locality,
				lot_size, price
			)
		)
		self.conn.commit()

	def __del__(self):
		self.conn.close()