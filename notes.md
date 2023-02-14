## Tech Questions:






































#### Troubleshoot networking issue on linux?
- To troubleshoot a network issue in Linux, you can use tools such as ping, traceroute, netstat, and tcpdump to check network connectivity, routing, and traffic. You can also check log files in /var/log for error messages.


#### Difference between TLS version 1.2 and 1.3. Explain the DNS flow when any website is accessed on browser. Python coding question on bucket sort algorithm. How to search for a target string from a network command output (using regex)
1. Improved security: stronger encryption 
2. Faster performance 
3. Enhanced privacy: TLS 1.3 encrypts more of the data in transit

#### Describe what happens when you hit "enter" on a browser URL.
1. resolves DNS.
2. creates an HTTP request with dns address. The request includes the URL you entered, any headers, and any data that should be sent to the server.
3. establishes a connection (TCP).
4. sends the HTTP request
5. Web server receives the request 
6. Web server generates an HTTP response
7. Web server sends HTTP response back
8. browser receives the response

#### SSL termination at proxy level
1. initiates an SSL connection to the proxy by sending a request to webserver
2. proxy decrypts the SSL connection, revealing the plaintext traffic.
3. The proxy inspects and possibly modifies the plaintext traffic before forwarding it to the server.
4. The proxy re-encrypts the traffic using a new SSL connection to the server.
5. The server receives the encrypted traffic, processes the request, and sends a response back to the proxy.
6. The proxy decrypts the response from the server, inspects it
7. The proxy re-encrypts the response and sends it back to the client.

#### Explain the OSI model
1. Physical layer: physical aspects of data transmission
2. Data Link Layer: reliable delivery of data frames between devices connected to the same network.
3. Network Layer: routing of data packets
4. Transport Layer: ensures end-to-end data integrity.
5. Session Layer: establishment and maintenance of communication sessions between applications.
6. Presentation Layer: converts data into a standardized format for transmission.
7. Application Layer: application-specific processes and services

#### What are cgroups in linux?
Control groups (cgroups) are a Linux kernel feature that allows you to allocate and manage system resources, such as CPU time, memory, and I/O bandwidth, for a group of processes. This allows you to control the resource usage of individual processes or groups of processes to ensure that they do not interfere with each other or with the overall stability of the system.

#### SystemD
1. Replaces init levels
2. manage system processes and services
3. systemd uses a unit-based configuration system, where each service or process is defined in a separate unit file.
4. logging 
`journalctl -u ssh.service`
`journalctl --priority=err`
5. services `systemctl status ssh.service`

## iops testin linux
utility for testing `fio` 
show device mb/S `iostat -md` 
shows avg I/O `vmstat`
show mounts `lsblk` or `fstab -l`

# Ansible
1. task
2. module
3. play/playbook
4. role
5. inventory - file

## Aws
alb (application) - L7
    best suited for http/https and
nlb (network) - L4 static ips
    bet suited for tcp/udp

## kafka (Broker)
Topic – Kafka Topic is the bunch or a collection of messages.
Producer – In Kafka, Producers issue communications as well as publishes messages to a Kafka topic.
Consumer – Kafka Consumers subscribes to a topic(s) and also reads and processes messages from the topic(s).
Brokers – While it comes to manage storage of messages in the topic(s) we use Kafka Brokers. For detailed understanding of Kafka components, go through,
Zookeeper - main role here is to build coordination between different nodes in a cluster
#### Apis
Producer API
Consumer API
Streams API
Connector API

## Explain paging, Deadlock, ROM, RAM, Bankers algorithm

Paging:
Paging is a memory management scheme used by operating systems to manage and allocate memory. In paging, the memory is divided into equal sized blocks called pages. The operating system uses a page table to keep track of the location of each page in physical memory. When a program needs to access a particular page, the operating system translates the virtual address of the page into a physical address, using the page table.

Deadlock:
Deadlock is a situation in computer science where two or more processes are unable to continue executing because they are waiting for each other to release resources. This can happen when two processes are waiting for each other to release a shared resource, such as a file or a piece of memory. Deadlock can cause a system to freeze or become unresponsive.

ROM:
ROM stands for Read-Only Memory. It is a type of memory that is used to store permanent data that cannot be changed. ROM is used in computer systems to store firmware and other system-level software that needs to be permanently stored in the computer's memory. ROM is non-volatile memory, which means that it retains its data even when the power is turned off.

RAM:
RAM stands for Random Access Memory. It is a type of memory that is used by the computer to temporarily store data that the computer is currently using. RAM is volatile memory, which means that it loses its data when the power is turned off. RAM is used by the computer to store the operating system, applications, and user data.

Banker's Algorithm:
The Banker's algorithm is a resource allocation and deadlock avoidance algorithm. It is used by operating systems to manage resource allocation in a system. The Banker's algorithm ensures that the system can avoid deadlock by checking the safe state before allocating resources to a process. In the Banker's algorithm, the system keeps track of the available resources and the maximum resources that each process can request. When a process requests resources, the system checks if the request can be granted without causing a deadlock. If the request can be granted, the resources are allocated to the process. If the request cannot be granted, the process is forced to wait until the required resources become available.