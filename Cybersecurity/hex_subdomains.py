# This is a script I quickly developed while participating in a Blue Team exercise on TryHackMe.
# During the exercise, I encountered a malware that used the subdomain portion of DNS queries
# (in hexadecimal form) to exfiltrate a file. To analyze the malicious activity, I exported the DNS queries
# using tshark and obtained a .txt file containing a list of all the DNS queries, whether legitimate or not.
# I needed a script to open this file, extract only the malicious queries, retrieve the hexadecimal strings
# from the subdomains, and save them in another text file. Later, I would decode the hexadecimal strings
# back to the original .kdbx file.

# At the bottom of the script, you can find an example of the queries present in the dns_queries.txt file.


seen = set()
with open("dns_queries.txt", "r") as f, open("subdomains.txt", "w") as out:
    for line in f:
        # Skip if line contains "addr.arpa"
        if "addr.arpa" in line:
            continue

        # Split on "." to separate the subdomain
        subdomain, _, _ = line.strip().split(".", 2)

        # Skip if this subdomain has been seen before
        if subdomain in seen:
            continue

        # Add this subdomain to the set of seen subdomains
        seen.add(subdomain)

        # Write this subdomain to the output file
        out.write(subdomain + "\n")



# 03D9A29A67FB4BB50100030002100031C1F2E6BF714350BE58.bpakcaging.xyz.eu-west-1.ec2-utilities.amazonaws.com
# 03D9A29A67FB4BB50100030002100031C1F2E6BF714350BE58.bpakcaging.xyz.eu-west-1.ec2-utilities.amazonaws.com
# 03D9A29A67FB4BB50100030002100031C1F2E6BF714350BE58.bpakcaging.xyz.eu-west-1.compute.internal
# 03D9A29A67FB4BB50100030002100031C1F2E6BF714350BE58.bpakcaging.xyz.eu-west-1.compute.internal
# 03D9A29A67FB4BB50100030002100031C1F2E6BF714350BE58.bpakcaging.xyz
# 03D9A29A67FB4BB50100030002100031C1F2E6BF714350BE58.bpakcaging.xyz
# 113.211.71.167.in-addr.arpa
# 113.211.71.167.in-addr.arpa
# 113.211.71.167.in-addr.arpa
# 113.211.71.167.in-addr.arpa
# 05216AFC5AFF03040001000000042000AF4DE7A467FADFBFEB.bpakcaging.xyz.eu-west-1.ec2-utilities.amazonaws.com
# 05216AFC5AFF03040001000000042000AF4DE7A467FADFBFEB.bpakcaging.xyz.eu-west-1.ec2-utilities.amazonaws.com
# 05216AFC5AFF03040001000000042000AF4DE7A467FADFBFEB.bpakcaging.xyz.eu-west-1.compute.internal
# 05216AFC5AFF03040001000000042000AF4DE7A467FADFBFEB.bpakcaging.xyz.eu-west-1.compute.internal
# 05216AFC5AFF03040001000000042000AF4DE7A467FADFBFEB.bpakcaging.xyz
# 05216AFC5AFF03040001000000042000AF4DE7A467FADFBFEB.bpakcaging.xyz
# 113.211.71.167.in-addr.arpa