# Image Forensics CTF

## Description

You are given an ordinary image of a toy: `challenge.jpg`. At first glance, it looks normal, but it contains **four hidden flags**.

This challenge helps you practice:

- `strings` – extracting readable text
- `binwalk` – scanning and extracting embedded files
- `steghide` – steganography extraction
- cracker – finding passwords for steghide-protected files

---

## Challenge Goal

Find **all four hidden flags** inside `challenge.jpg`.

---

## Step 1: Find Flag 1 and 2 (using `strings`)

```bash
strings challenge.jpg | grep FLAG
```

**Output:**

```text
FLAG{ALWAYS_Check_Metadata}
FLAG{Strings_leak_information}
```

- These are the first two flags.

---

## Step 2: Find Flag 3 (using `binwalk` and strings)

1. Scan the image for embedded files:

```bash
binwalk challenge.jpg
```

**Output:**

```text
DECIMAL       HEXADECIMAL     DESCRIPTION
0             0x0             JPEG image data, JFIF standard 1.01
75667         0x12793         Zip archive data, at least v1.0 to extract, compressed size: 41, uncompressed size: 41, name: flag4.txt
75854         0x1284E         End of Zip archive, footer length: 22
```

2. Extract embedded files:

```bash
binwalk -e challenge.jpg
```

- This creates a folder `_challenge.jpg.extracted`.

3. Check the extracted file with `strings` to find encoded data:

```bash
strings _challenge.jpg.extracted/flag4.txt
```

**Output (double-encoded data):**

```text
Umt4QlIzdGhjSEJsYm1SbFpGOTZhWEI5Q2c9PQo=
```

4. Decode double-encoded data :

```bash
echo "Umt4QlIzdGhjSEJsYm1SbFpGOTZhWEI5Q2c9PQo=" | base64 -d | base64 -d

```

**Output:**

```text
FLAG{appended_zip}
```

---

## Step 4: Find Flag 4 (using `steghide` and password cracking)

1. Use a password-cracker (like `stegseek` or a custom cracker) to find the passphrase:

```bash
./crack challenge.jpg /usr/share/wordlists/rockyou.txt
```

**Output (cracker result):**

```text
[*] Trying (34086): liberty                                      
[*] Trying (34087): molly1                                       
[*] Trying (34088): ronaldinho                                   
[*] Trying (34089): password123                                  
[+] PASSWORD FOUND: password123 
```

2. Extract the hidden file using the found passphrase:

```bash
steghide extract -sf challenge.jpg -p password123
```

3. View the extracted file:

```bash
cat flag5.txt
```

**Output:**

```text
FLAG{steghide_protected}
```

---

## Therefore the four flags are:

- FLAG{ALWAYS\_Check\_Metadata}

- FLAG{Strings\_leak\_information}

- FLAG{appended\_zip}

- FLAG{steghide\_protected}



