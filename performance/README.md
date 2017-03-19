Usage:

wget https://raw.githubusercontent.com/St-Fl/Tutorial/test-branch/performance/bash_test_-a.sh<br/>
wget https://raw.githubusercontent.com/St-Fl/Tutorial/test-branch/performance/bash_test_without_-a.sh

### Make the files executable

chmod +x bash_test_-a.sh<br/>
chmod +x bash_test_without_-a.sh

### Execute the files

time bash_test_-a.sh<br/>
time bash_test_without_-a.sh

### Results

`time ./bash_test_without_-a.sh<br/>
real	0m41.570s<br/>
user	0m35.214s<br/>
sys	0m6.318s`

`time ./bash_test_-a.sh<br/>
real	0m37.763s<br/>
user	0m31.774s<br/>
sys	0m5.933s`

--> The execution of bash_test_-a.sh should be quicker, because it is only forking one process to compare values.
