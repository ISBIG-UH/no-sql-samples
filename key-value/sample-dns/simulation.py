import random


# Operations
CREATE = "CREATE" 
DELETE= "DELETE"
RETRIEVE = "RETRIEVE"

# Some random names
names_pool = [
    "Liam", "Olivia", "Noah", "Emma", "Oliver", "Charlotte", "Elijah", "Amelia", 
    "James", "Ava", "William", "Sophia", "Benjamin", "Isabella", "Lucas", "Mia", 
    "Henry", "Evelyn", "Alexander", "Harper", "Mason", "Ella", "Michael", "Luna", 
    "Ethan", "Camila", "Daniel", "Gianna", "Jacob", "Elizabeth", "Logan", "Sofia", 
    "Jackson", "Emily", "Levi", "Scarlett", "Sebastian", "Madison", "Mateo", 
    "Abigail", "Jack", "Avery", "Owen", "Ella", "Theodore", "Grace", "Aiden", 
    "Chloe", "Samuel", "Victoria", "Joseph", "Riley", "John", "Aria", "David", 
    "Lillian", "Wyatt", "Nora", "Matthew", "Zoey", "Luke", "Hannah", "Asher", 
    "Hazel", "Carter", "Lily", "Julian", "Ellie", "Grayson", "Violet", "Leo", 
    "Aurora", "Jayden", "Savannah", "Gabriel", "Audrey", "Isaac", "Brooklyn", 
    "Lincoln", "Bella", "Anthony", "Claire", "Hudson", "Skylar", "Dylan", 
    "Lucy", "Ezra", "Paisley", "Thomas", "Everly", "Charles", "Anna", "Christopher", 
    "Caroline", "Jaxon", "Nova", "Maverick", "Genesis", "Josiah", "Emilia", 
    "Isaiah", "Kennedy", "Andrew", "Samantha", "Elias", "Maya", "Joshua", 
    "Willow", "Nathan", "Kinsley", "Caleb", "Naomi", "Ryan", "Aaliyah", "Adrian", 
    "Elena", "Miles", "Sarah", "Eli", "Ariana", "Nolan", "Allison", "Christian", 
    "Gabriella", "Aaron", "Alice", "Cameron", "Madelyn", "Ezekiel", "Cora", 
    "Colton", "Ruby", "Luca", "Eva", "Landon", "Serenity", "Hunter", "Autumn", 
    "Jonathan", "Adeline", "Santiago", "Hailey", "Axel", "Gianna", "Easton", 
    "Isla", "Cooper", "Freya", "Jeremiah", "Ivy", "Angel", "Josephine", "Roman", 
    "Emery", "Connor", "Piper", "Jameson", "Raelynn", "Robert", "Athena", "Greyson", 
    "Eleanor", "Jordan", "Everleigh", "Ian", "Melody", "Carson", "Leah"
]

# Some pc synonyms
device_pool = [
    "computer", "PC", "workstation", "laptop", "desktop", "notebook", 
    "machine", "device", "workstation"
]


def get_random_ip():
    """
    Generate a random IPv4 address.

    Returns:
        str: A random IP address in the format 'X.X.X.X'.
    """
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def create_simulation(iterations, seed):
    """
    Simulates a series of operations (CREATE, RETRIEVE, DELETE) on a collection of IPs and devices.

    Args:
        iterations (int): The number of iterations for the simulation.
        seed (int): The seed for the random number generator.

    Returns:
        list: A list of tuples representing the simulation actions and their arguments.
    """

    ips = dict() # ip -> device
    ips_inv = dict() # device -> ip
    simulation = []

    random.seed(seed)

    for _ in range(iterations):
        
        if len(ips) > 0 and random.random() <= 0.6: # groups DELETE and RETRIEVE because they need a non empty collection
            
            key, value = random.choice(list(ips.items()))
            
            if random.random() <= 0.3: # 0.2 chance of deletion
                del ips[key]
                del ips_inv[value]
                simulation.append((DELETE, value)) 
            else: # 0.4 chance of retrieve
                simulation.append((RETRIEVE, value))

        else: # 0.4 chance of create
            
            # get a random device to join the network
            ip = get_random_ip()

            while True:
                device_name = f"{random.choice(names_pool)}{random.randint(0,10000)} {random.choice(device_pool)}"
                if not ips_inv.get(device_name):
                    break
            
            # if the ip already exists delete it first
            if ips.get(ip):
                simulation.append((DELETE, ips[ip]))
            
            ips[ip] = device_name
            ips_inv[device_name] = ip
            simulation.append((CREATE, device_name, ip))

    return simulation
