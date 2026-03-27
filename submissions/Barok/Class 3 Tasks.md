1.  -rwxr-xr-x  -->  -rw-r----- : the chmod number is 110 100 000 => 640
2.  644 --> +X for everyone while rw are the same => 644 -> -rw-r--r-- let's add +x for all  -rwx-r-xr-x => 755
3.  writable by owner and group but readable for everyone -rwxrwxr-- => 774
4. 110 100 000 => 640
5.  A file only accessible to root , yes
6. ![[Pasted image 20260322005023.png]]
7. touch Audit.txt ; sudo chmod 750 Audit.txt;
![[Pasted image 20260322005206.png]]
8.  741 --> -rwxr----x
9.  500 --> 101 --> r-x
10.  -r-xrw-r-- => 101 110 100 --> 564


Task 2:
![[Pasted image 20260321161009.png]]
 First flag in the Image Meta Data:
	 FLAG{ALWAYS_Check_Metadata}
![[Pasted image 20260321161252.png]]
the second flag was hidden inside the binary file in clear view and found using cat, strings and grep: 
	FLAG{Strings_leak_information}

![[Pasted image 20260321162659.png]]
![[Pasted image 20260321162810.png]]
this is the third flag i found by trying to extract the passphrase from this encrypted file using brute force from rockyou.txt wordlist using cmd stegseek , because we couldn't extract it using steghide :
	FLAG{steghide_protected}
![[Pasted image 20260321164256.png]]
![[Pasted image 20260322004809.png]]
this flag was found embedded in the image file as a zip  and found using the tool binwalk :
	FLAG{appended_zip}

And the last FLAg is :
	FLAG{xor_hidden}
![[Screenshot From 2026-03-22 07-54-29.png]]
 using the python script:
	``` data = open('challenge.jpg', 'rb').read()
for key in range(256):
    decoded = ''.join(chr(b ^ key) if 32 <= (b ^ key) <= 126 else '.' for b in data)
    if 'FLAG' in decoded:
        start = decoded.find('FLAG')
        print(f'Key {hex(key)} found Match: {decoded[start:start+40]}')
	
