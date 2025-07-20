#  DAY10 Q1
'''
Name:Jyotisman Kirti Prakash
ID:31261
Email:jyotismankirtiprakash11@gmail.com
Date:19-July-2025
Purpose:Static Method
'''

class PasswordUtils:
    @staticmethod
    def isstrong(password):
        return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password)
        )

if __name__ == '__main__':
    password = "testone"
    print(f"password: {password} is {'Strong' if PasswordUtils.isstrong(password) else 'Weak'}")

    password = "testOne#$" 
    password = "testOne1#" 

    print(f"password: {password} is {'Strong' if PasswordUtils.isstrong(password) else 'Weak'}")