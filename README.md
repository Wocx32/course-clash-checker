# Course Clash Checker
Check if course timings clash with other courses

**Note: You must have firefox installed**

# Install
Clone this repository
```
git clone https://github.com/Wocx32/course-clash-checker.git
```

Cd to the repository

```
cd course-clash-checker
```

Install requirements

```
pip install -r requirements.txt
```

# Download Geckodriver
Download latest release of geckodriver from [here](https://github.com/mozilla/geckodriver/releases)

Then move the executable file inside the cloned repository 

# Usage
Run
```
python main.py
```

Enter your courses and comma seperate them

```
Enter courses: comp 113 a, comp 451 a, comp 206 c, econ 101 a
```

It will give the output
```
COMP 206 C clashes with COMP 113 A
```

# Update Database
To update database
```
python database.py