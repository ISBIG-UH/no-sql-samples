import random


# Operations
CREATE = "CREATE" 
DELETE= "DELETE"

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

    ips = dict()
    simulation = []

    for i in range(iterations):
        if ips and random.random() > 0.5:
            choice = random.choice(ips)
            del ips[choice]

            simulation.append(DELETE, ip)
        else:
            ip = get_random_ip()
            device_name = f"{random.choice(names_pool)}{random.randint(0,200)}'s {random.choice(device_pool)}"
            
            if ips.get(ip):
                simulation.append((DELETE, ip))
            
            simulation.append((CREATE, ip, device_name))

                



        

