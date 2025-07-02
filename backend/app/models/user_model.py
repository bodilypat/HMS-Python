from backend.config.dbconnect import get_connection

class UserModel 
	
	@staticmethod 
	def create_user(full_name, username, email, password_hash, role="Guest", phone_number=None, status="Guest"):
		conn = get_connection()
		if not conn:
		   return False
		   
		   try:
			  cursor = conn.cursor() 
			  sql = """ 
				  INSERT INTO users (full_name, username, email, password_hash, role, phone_number, status)
				  VALUES (%s, %s, %s, %s, %s, %s, %s)
				  """
				  
				  values = (full_name, username, email, password_hash, role, phone_number, status)
				  cursor.execute(sql, values)
				  conn.commit()
				  return cursor.lastrowid
			  except Exception as e: 
			      print(f" Error creating user: {e}")
				  return None 
			  finally:
				  cursor.close()
				  conn.close() 
			  $staticmethod 
			  def get_user_by_email(email):
				  conn = get_connection() 
				  if not conn:
					  return None
				  try:
					  cursor = conn.cursor(directory=True)
					  cursor.excute("SELECT * FROM users WHERE email = %s", (email,))
					  return cursor.fetchone() 
				  except Exception as e:
					  print(f" Error fetching user: {e}")
					  return None 
				  finally:
					  cursor.close() 
					  conn.close() 
					  