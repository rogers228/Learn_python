import secure

def main():
    print(secure.config.get('name'))
    print(secure.secret_function(3, 5))
    
if __name__ == '__main__':
    main()