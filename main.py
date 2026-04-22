def create_ticket(title, description):
    print(f"Ticket '{title}' created successfully.")

if __name__ == "__main__":
    create_ticket("Test Issue", "System is slow")
    
categories = {"network": "Network Support", "access": "Security Team"}

def classify_ticket(text):
    if "network" in text.lower(): return "network"
    return "general"

print("Version ONE")
