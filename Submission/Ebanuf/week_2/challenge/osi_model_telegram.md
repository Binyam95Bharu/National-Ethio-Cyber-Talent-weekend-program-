# OSI Model Explained Using Telegram

The OSI model has 7 layers. They are arranged in a stack with the **Physical Layer** at the bottom and the **Application Layer** at the top.

---

## 1. Physical Layer
**What it does:**  
Manages the actual hardware used to transmit information – cables, Wi-Fi, fiber optic cables – that carries bits of information (0s and 1s) between two devices.  
**Telegram example:**  
When you hit “Send” on Telegram, your message's information is changed into electrical impulses via your Wi-Fi network.

---

## 2. Data Link Layer
**What it does:**  
Makes sure information can travel over a network. Adds information about where the message is coming from and checks for errors.  
**Telegram example:**  
Your router and phone work together to make sure your Telegram message is sent out correctly over your Wi-Fi connection, even if it drops for a few seconds.

---

## 3. Network Layer
**What it does:**  
Figures out where your message is going across networks. Uses IP addresses.  
**Telegram example:**  
Telegram knows your phone's IP address. Your message goes across multiple networks to get to its final destination. These networks include your ISP's network, the backbone of the internet, and Telegram's network.

---

## 4. Transport Layer
**What it does:**  
Ensures that data is delivered. It divides data into segments, tracks delivery, and retransmits segments that are lost in transit, or sends data quickly without checking for errors.  
**Telegram example:**  
Telegram uses TCP for messages. This ensures that your message is delivered in its entirety. If a segment of your message is lost in transit, TCP retransmits it.

---

## 5. Session Layer
**What it does:**  
Manages communication sessions among devices. It ensures that a connection is maintained.  
**Telegram example:**  
When you launch a chat on Telegram, a session is established. You remain logged in until you log out.

---

## 6. Presentation Layer
**What it does:**  
Translates data into a format that is easily understood by the application.  
**Telegram example:**  
Telegram encrypts your messages, similar to end-to-end encryption for secret chats. It translates emojis, stickers, and other formats so that they may be easily understood by the receiving device.

---

## 7. Application Layer
**What it does:**  
This is what you interact with. It is usually email clients, apps, or a web browser.  
**Telegram example:**  
The Telegram app is where you send messages, send images, look at stickers, and receive notifications.

