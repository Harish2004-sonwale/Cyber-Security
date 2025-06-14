# Password Strength Analyzer with Custom Wordlist Generator

A comprehensive tool for analyzing password strength and generating custom wordlists based on user inputs.

## Features

- Password strength analysis using zxcvbn
  - Score from 0 to 4
  - Crack time estimates
  - Feedback suggestions
  - Entropy calculation
- Custom wordlist generation based on:
  - User's name
  - Birthdate
  - Pet name
  - Common patterns
  - Leetspeak variations
  - Special characters
  - Number combinations
- Both GUI and CLI interfaces
- Export wordlists in .txt format
- Real-time password strength feedback
- Automatic wordlist updates
- Support for multiple languages

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### GUI Mode (Default)
Simply run the script:
```bash
python password_analyzer.py
```

The GUI will open, allowing you to:
1. Enter a password for analysis
2. Input personal information for wordlist generation
3. Generate and save wordlists
4. View real-time strength analysis
5. Export wordlists in various formats

### CLI Mode
Run with the --cli flag:
```bash
python password_analyzer.py --cli
```

Follow the prompts to:
1. Enter a password for analysis
2. Provide personal information for wordlist generation
3. Choose output format

## Output

The tool generates:
- Password strength analysis with:
  - Score (0-4)
  - Crack time estimates
  - Feedback suggestions
  - Entropy calculation
- Custom wordlist in `wordlist.txt`
- Analysis report in JSON format

## Usage Examples

### CLI Example
```bash
python password_analyzer.py --cli
Enter password to analyze: MySecurePass123
Enter name (optional): JohnDoe
Enter birthdate (YYYY-MM-DD, optional): 1990-01-01
Enter pet name (optional): Max
```

### GUI Example
1. Open the application
2. Enter password: MySecurePass123
3. Click "Analyze Password"
4. Enter personal info:
   - Name: JohnDoe
   - Birthdate: 1990-01-01
   - Pet: Max
5. Click "Generate Wordlist"

## Security Note

This tool is for educational purposes only. Use the generated wordlists responsibly and only against systems you have permission to test.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Support

For support, please open an issue in the GitHub repository.

## Acknowledgments

- zxcvbn-python for password strength analysis
- NLTK for natural language processing
- tkinter for GUI development
- All contributors who have helped shape this project
