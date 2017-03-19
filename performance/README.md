Usage:

wget https://raw.githubusercontent.com/St-Fl/Tutorial/test-branch/performance/bash_test_-a.sh<br/>
wget https://raw.githubusercontent.com/St-Fl/Tutorial/test-branch/performance/bash_test_without_-a.sh

# Make the files executable

chmod +x bash_test_-a.sh
chmod +x bash_test_without_-a.sh

# Execute the files

time bash_test_-a.sh
time bash_test_without_-a.sh
