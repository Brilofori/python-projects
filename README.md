**Port Scanning Demo (Python Automation)**

As I’ve been progressing further into my networking knowledge during my degree, I’ve also been actively developing my Python skills. I decided to combine both of these by building a port scanning tool within a networking-focused scope.

The purpose of this project is to strengthen my understanding of how network services operate at the socket level, how ports behave when they are open, closed, or filtered, and how Python can be used for practical network automation. Rather than relying on full-featured tools, this project focuses on building the core scanning logic from first principles to reinforce foundational concepts.

This project is still a work in progress and is being iterated on as my networking and automation knowledge continues to grow.

**What I Learned**

At first, I wanted to scan all ports like tools such as Nmap, but after learning more about performance and how slow a basic Python scanner can be, I decided to scale it down to focus on a few common ports instead. This helped me understand how real tools prioritise targets rather than brute-forcing everything. I learned how to use the socket module to create sockets and connect them to IPv4 addresses, which made networking concepts feel way more practical. Overall, this project helped me shift into thinking in terms of objects, processes, and structure, and gave me a much better understanding of execution order and when to properly use try, except, and finally. Using the socket module  helped connect my Python skills with what I’m learning in networking and my degree.
