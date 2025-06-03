# Password Strength Metrics Documentation

## Password Strength Factors

### 1. Length
- Minimum recommended: 12 characters
- Longer passwords are exponentially harder to crack
- Each additional character increases security significantly

### 2. Character Variety
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Numbers (0-9)
- Special characters (!@#$%^&*)
- More variety = higher entropy

### 3. Complexity Metrics

#### Length
- Short (<8): Very weak
- 8-11: Weak
- 12-15: Moderate
- 16+: Strong

#### Character Types
- Single type: Very weak
- Two types: Weak
- Three types: Moderate
- Four types: Strong

### 4. Common Strength Indicators

#### Entropy
- Measures randomness
- Higher entropy = stronger password
- Calculated based on character set size and length

#### Pattern Avoidance
- Avoid common patterns (123456, qwerty)
- Avoid dictionary words
- Avoid personal information

### 5. Attack Resistance

#### Brute Force
- Time to crack increases exponentially with length
- Additional character types increase difficulty

#### Dictionary Attacks
- Avoid common words and patterns
- Use random combinations
- Include special characters

### 6. Best Practices

1. **Length First**
   - Start with minimum 12 characters
   - Longer is always better

2. **Character Variety**
   - Use all four character types
   - Avoid predictable patterns

3. **Avoid Common Elements**
   - No dictionary words
   - No personal info
   - No common patterns

4. **Regular Updates**
   - Change passwords periodically
   - Use different passwords for different accounts

5. **Password Managers**
   - Use for generating and storing complex passwords
   - Enables use of very long, random passwords

## Strength Evaluation Tools

### Recommended Tools
1. Passwordmeter.com
   - Comprehensive strength analysis
   - Visual feedback
   - Detailed metrics

2. HowSecureIsMyPassword.net
   - Estimates cracking time
   - Shows password entropy
   - Provides improvement suggestions

### What to Look For
- Time to crack estimates
- Entropy score
- Character variety analysis
- Pattern detection
- Dictionary word detection
