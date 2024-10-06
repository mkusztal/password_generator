import string
import secrets

def generate_password(length: int = 25) -> str:
    if length < 25:
        raise ValueError("Password length must be at least 25 characters.")
    
    
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password += [secrets.choice(all_characters) for _ in range(length-4)]
    
    secrets.SystemRandom().shuffle(password)
    
    print(f"Pasword: {''.join(password)}")
    return ''.join(password)
    
    
generate_password()
# 27 billion trillion trillion years