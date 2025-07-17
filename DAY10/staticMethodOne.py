'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
   Date:17-July-2025
   Purpose:Static Method 
'''
class PasswordUtils:
    @staticmethod
    def isStrong(password):
        return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password)
        )
       
if __name__ == '__main__':
    password = 'testone'
    print(f"password: {password} is {'Strong' if PasswordUtils.isStrong(password) else 'Weak'}")
 
 
    password = 'test1One#$'
    print(f"password: {password} is {'Strong' if PasswordUtils.isStrong(password) else 'Weak'}")