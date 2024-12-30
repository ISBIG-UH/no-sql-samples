import etcd3
from tenacity import retry, wait_fixed, stop_after_attempt, retry_if_exception_type
import random

class ClientWithFailover:
    def __init__(self, host, port):
        self.etcd = etcd3.client(host=host, port=port)
        self.nodes = []
        self.current = (host, port)
        for m in self.etcd.members:
            data = m.peer_urls[0][7:].split(':')
            self.nodes.append((data[0], int(data[1])))
        print(f"Succesfully created etcd client in cluster with nodes {self.nodes} and current write node {self.current}")
        
    def failover(self):
        print('Error: Failover procedure started')
        server = random.choice([n for n in self.nodes if n[0] != self.current[0]])
        print(f'Selected {server[0]}:{server[1]} as the new write node')
        self.etcd = etcd3.client(host=server[0], port=server[1])
        self.current = server
        
    # Decorator to handle retries
    @retry(
        retry=retry_if_exception_type(Exception),
        wait=wait_fixed(2),  # Wait 2 seconds between retries
        stop=stop_after_attempt(5)  # Retry up to 5 times
    )
    def put_with_retry(self, key, value):
        try:
            self.etcd.put(key, value)
        except Exception as e:
            self.failover()
            raise e
    
    @retry(
        retry=retry_if_exception_type(Exception),
        wait=wait_fixed(2),  # Wait 2 seconds between retries
        stop=stop_after_attempt(5)  # Retry up to 5 times
    )
    def delete_with_retry(self, key):
        try:
            self.etcd.delete(key)
        except Exception as e:
            self.failover()
            raise e
    
    
    @retry(
        retry=retry_if_exception_type(Exception),
        wait=wait_fixed(2),  # Wait 2 seconds between retries
        stop=stop_after_attempt(5)  # Retry up to 5 times
    )
    def get_with_retry(self, key):
        try:
            self.etcd.get(key)
        except Exception as e:
            self.failover()
            raise e
        


        