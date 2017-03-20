### Usage:

wget https://raw.githubusercontent.com/St-Fl/Tutorial/test-branch/performance/bash_test_-a.sh<br/>
wget https://raw.githubusercontent.com/St-Fl/Tutorial/test-branch/performance/bash_test_without_-a.sh

wget https://raw.githubusercontent.com/St-Fl/Tutorial/test-branch/performance/python_test_with_sys_mod.py<br/>
wget https://raw.githubusercontent.com/St-Fl/Tutorial/test-branch/performance/python_test_with_os_mod.py

### Make the files executable

chmod +x bash_test_-a.sh<br/>
chmod +x bash_test_without_-a.sh

chmod +x python_test_with_sys_mod.py<br/>
chmod +x python_test_with_os_mod.py

### Execute the files

time ./bash_test_-a.sh<br/>
time ./bash_test_without_-a.sh

time ./python_test_with_sys_mod.py<br/>
time ./python_test_with_os_mod.py

### Results

#### Bash

`time ./bash_test_without_-a.sh
real	0m41.570s
user	0m35.214s
sys	0m6.318s`

`time ./bash_test_-a.sh
real	0m37.763s
user	0m31.774s
sys	0m5.933s`

--> The execution of bash_test_-a.sh is faster then bash_test_without_-a.sh, because it is only forking one process to compare values.

#### Python

`time ./python_test_with_sys_mod.py
real	0m0.970s
user	0m0.969s
sys	0m0.000s`

`time ./python_test_with_os_mod.py
real	14m53.598s
user	0m36.407s
sys	14m17.296s`

--> The execution of python_test_with_sys_mod.py is faster then python_test_with_os_mod.py, because it leaves the /dev/null writing open instead of opening file for the write operation each time.

##### Overall the python_test_with_sys_mod.py performs much faster then everything else!

### strace analye

strace -cf ./bash_test_-a.sh<br/>
strace -cf ./bash_test_without_-a.sh

strace -cf ./python_test_with_sys_mod.py<br/>
strace -cf ./python_test_with_os_mod.py
