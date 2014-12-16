#!/bin/sh

echo "Packet size:"; read Size;
echo "Number of ping instances:"; read Ping;
echo "Size:"; read Site;

for i in `seq $Ping`;
do
osascript<<EOF
tell application "System Events"
tell process "Terminal" to keystroke "t" using command down
end
tell application "Terminal"
activate
do script with command "ping -s $Size $Site" in window 1
end tell
EOF
done




