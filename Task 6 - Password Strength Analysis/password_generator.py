import random
import string
import json

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Generate a random password with specified characteristics"""
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return ""  # No character types selected
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def analyze_password_strength(password):
    """Analyze password strength metrics"""
    metrics = {
        'length': len(password),
        'uppercase': sum(1 for c in password if c.isupper()),
        'lowercase': sum(1 for c in password if c.islower()),
        'digits': sum(1 for c in password if c.isdigit()),
        'symbols': sum(1 for c in password if c in string.punctuation),
        'unique_chars': len(set(password))
    }
    return metrics

# Generate sample passwords with different characteristics
passwords = {
    'weak': generate_password(length=6, use_upper=False, use_lower=True, use_digits=False, use_symbols=False),
    'medium': generate_password(length=10, use_upper=True, use_lower=True, use_digits=True, use_symbols=False),
    'strong': generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True),
    'very_strong': generate_password(length=20, use_upper=True, use_lower=True, use_digits=True, use_symbols=True)
}

# Analyze each password
analysis_results = {}
for name, password in passwords.items():
    analysis_results[name] = {
        'password': password,
        'metrics': analyze_password_strength(password)
    }

# Save results to JSON file
with open('password_analysis.json', 'w') as f:
    json.dump(analysis_results, f, indent=4)

# Print results
print("Password Analysis Results:")
for name, result in analysis_results.items():
    print(f"\n{name.upper()}: {result['password']}")
    print("Metrics:", result['metrics'])
