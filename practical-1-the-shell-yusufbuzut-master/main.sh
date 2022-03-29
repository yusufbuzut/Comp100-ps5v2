
$shell

mkdir practicals
touch --help 
touch semester
echo '#!/bin/sh' > semester
echo 'curl --head --silent https://missing.csail.mit.edu' >> semester
sh semester
./semester
chmod --help
chmod +x semester

./semester | grep -i last > last-modified.tx