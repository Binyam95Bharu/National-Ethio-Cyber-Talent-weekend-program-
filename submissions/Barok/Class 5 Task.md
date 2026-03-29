Flag 1 : Task 
Hint: “Sometimes secrets travel unencrypted. Inspect the messages your browser asks for.”

![[Pasted image 20260329011630.png]]

here we found the first flag in the packet with http protocol where the browser asks itself 

Flag: FLAG{http_easy_capture}

Flag 2 : Task
Hint: “Even small questions can carry hidden messages. Check what your system is asking the internet.”

![[Pasted image 20260329012029.png]]

here we found the second flag by checking packets where the the system itself asked them for.

Flag: FLAG_dns_exfiltration_examplecom

Flag 3: Task
Hint: “The answer might be broken into pieces across multiple packets. Reassemble to see the whole picture.”

![[Pasted image 20260329012321.png]]

here we found the 3rd flag by combining the fragmented data in the TCP stream.

Flag: FLAG{tcp_stream_reassembly}

Flag 4: Task
Hint: “Some messages arrive encoded. The transport might reveal patterns in the body rather than the headers.”

![[Pasted image 20260329012455.png]]

![[Pasted image 20260329012531.png]]

we found the 4th flag in SMTP packets encrypted using base64 encoding .

Flag: FLAG{ic_icmp}

Flag 5: Task
Hint: “Even simple pings can carry secrets inside them. Don’t just look at the summary—peek at the payload.” 

![[Pasted image 20260329012650.png]]

here we found the last flad in an ICMP protocol packets since we were given the hint that it is in ping requests , as we can see we can find the flag in both the request and response

Flag:  FLAG{smtp_base64}