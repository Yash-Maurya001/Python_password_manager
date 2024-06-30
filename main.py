import fire
from cryptography.fernet import Fernet


def main():
    fire.Fire({
        "-help": how_to_use,
        "-a": add,
        "-v": view,
        "--gen-key": gen_key,

    })


def how_to_use():
    print("""
     -a: To add passwords formate - UserName/Email Password Website
     -v: to View password 
     --gen-key: To generate the key <- use this first before running the -a or -v
    """)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# Generate Key For Encryption
def gen_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as File:
        File.write(key)
        File.close()


def add(username: str, password:str, website: str):
    key = load_key()
    fer = Fernet(key)

    with open("password.txt", "a") as File:
        File.write((fer.encrypt(username.encode())).decode() + "|" + fer.encrypt(
            password.encode()).decode() + "|" + fer.encrypt(website.encode()).decode() + "\n")
        File.close()
        print("Information Saved")


def view():
    with open("password.txt", "r") as File:
        for lines in File.readlines():
            key = load_key()
            fer = Fernet(key)
            data = lines.rstrip()
            user, pwd, website = data.split("|")
            user = fer.decrypt(user.encode()).decode()
            pwd = fer.decrypt(pwd.encode()).decode()
            website = fer.decrypt(website.encode()).decode()
            print(f"{user} : {pwd} : {website}")


if __name__ == '__main__':
    main()
