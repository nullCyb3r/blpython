import dns.resolver

def dns_enumerate(domain):
    record_types = ['A','AAAA','NS','MX','TXT']

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain,record_type)
            print(f" {record_type} Records: ")
            for rdata in answers:
                print(f" {rdata}")
        except dns.resolver.NoAnswer:
            print(f"No {record_type} record Found!")

        except dns.resolver.MXDOMAIN:
            print(f"Domain {domain} does not exit")
        except Exception as e:
            print(f"Error {e} ")
def main():
    domain_name = input("Enter Domain name : ")

    result = dns_enumerate(domain_name)
if __name__ == "__main__":
    main()