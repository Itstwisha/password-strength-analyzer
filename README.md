
# Password Strength Analyzer

A Python-based tool that evaluates password strength using entropy, pattern checks, and a dictionary of common weak passwords.  
This project demonstrates basic cybersecurity logic, pattern detection, and secure password analysis.

---

## Features

- Calculates **entropy** of the password  
- Detects weak structures:
  - Too short (< 8 characters)
  - Only letters / only numbers  
  - Appears in the common passwords list  
- Provides a final rating: **Weak / Medium / Strong**  
- Easy to extend with more rules

---

## Project Structure

```

password-strength-analyzer/
│── analyzer.py
│── data/
│     └── common_passwords.txt
│── samples/
│     └── sample_inputs.txt
│── README.md

````

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/Itstwisha/password-strength-analyzer.git
cd password-strength-analyzer
````

Run the script:

```bash
python3 analyzer.py
```

Enter any password when prompted:

```
Enter password to analyze:
```

---

## Sample Output

```
Enter password to analyze: Tr0ub4dor&3

Password Strength: Strong
Entropy Score: 58.23
Issues Found:
No major issues detected.
```

Another example:

```
Enter password to analyze: password123

Password Strength: Weak
Entropy Score: 25.59
Issues Found:
- Common password found in the dictionary
```

---

## Sample Inputs

Inside `samples/sample_inputs.txt`:

```
123456
password
HelloWorld123
H3lloW0rld!
Tr0ub4dor&3
SuperStrongP@ssw0rd!!!
```

---

## Future Enhancements

* Add a GUI interface
* Build a live web version
* Implement password breach checking via HaveIBeenPwned API
* Add unit tests
* Add complexity scoring visualization

---

## Author

**Twisha**
Cybersecurity Analyst & MS Cybersecurity Student
GitHub: [@Itstwisha](https://github.com/Itstwisha)

---

## License

MIT License

