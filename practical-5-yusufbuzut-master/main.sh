# PART 1
sleep 100
control+z
sleep 13m &
nohup sleep 1.7h &
fg %1
control+c

kill -HUP %2  #"(its status will change hangup,after a while it be gone from list of jobs)"
kill -HUP %3   #(it will continue running because we started with nohup)

kill %3 #(this can kill remaining job)

# PART 2
cd ~   #we will change directory to home 
mkdir docsforcomp100_1
mkdir docsforcomp100_2
mkdir docsforcomp100_3 # we created 3 directory under home folder
alias section1="cd /home/runner/docsforcomp100_1"
alias section2="cd /home/runner/docsforcomp100_2"
alias section3="cd /home/runner/docsforcomp100_3"

# PART 3
touch .bash_aliases
alias dc=cd
echo alias dc=cd > ~/.bash_aliases
source ~/.bash_aliases
dc docsforcomp100_1


# PART 4
ssh-keygen
type C:\Users\yusuf/\.ssh\id_rsa.pub | ssh ybuzut19@linuxpool.ku.edu.tr "cat >> .ssh/authorized_keys"
#then enter password
ssh ybuzut19@linuxpool.ku.edu.tr
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa.pub ybuzut19@linux01

#then we will try
ssh linux01 



# PART 5

vi ticker.py #we will write our code now
:wq #for save and quit ticker.py
tmux new -s session1 #we create a new session1
python ticker.py --interval 10 #enter   it will echo the date and time every 10 seconds
control b then d # to detach from that section
tmux list-sessions #lists sessions
tmux new -s session2 #we createanother session
python ticker.py --interval 5
control b then d
tmux list-sessions
tmux attach -t session2 #to attach session2
control b then d 
tmux attach -t session1
control b then d  # I finished control sessions. They are still running.
tmux kill-session -t session1
tmux kill-session -t session2 # sessions are killed
tmux list-sessions # there are no sessions

