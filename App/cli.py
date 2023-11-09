from app import signup, signin, get_user_profile
from scripts.food_distro import get_food_data, calculate_distribution, send_notifications

def main():
    while True:
        command = input('Enter command (signup, signin, profile, get_food_data, calculate_distribution, send_notifications, quit): ')
        try:
            if command == 'signup':
                username = input('Enter username: ')
                password = input('Enter password: ')
                if not username or not password:
                    print('Username and password cannot be empty')
                else:
                    signup(username, password)
            elif command == 'signin':
                username = input('Enter username: ')
                password = input('Enter password: ')
                if not username or not password:
                    print('Username and password cannot be empty')
                else:
                    signin(username, password)
            elif command == 'profile':
                username = input('Enter username: ')
                if not username:
                    print('Username cannot be empty')
                else:
                    get_user_profile(username)
            elif command == 'get_food_data':
                get_food_data()
            elif command == 'calculate_distribution':
                calculate_distribution()
            elif command == 'send_notifications':
                send_notifications()
            elif command == 'quit':
                break
            else:
                print('Invalid command')
        except Exception as e:
            print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()