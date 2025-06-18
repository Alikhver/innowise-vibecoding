import requests
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

def seed_database():
    """Seed the database with initial user data from JSONPlaceholder"""
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_users = db.query(User).count()
        if existing_users > 0:
            print(f"Database already contains {existing_users} users. Skipping seed.")
            return
        
        # Fetch data from JSONPlaceholder API
        print("Fetching user data from JSONPlaceholder...")
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()
        users_data = response.json()
        
        # Create user objects and add to database
        for user_data in users_data:
            db_user = User(
                id=user_data["id"],
                name=user_data["name"],
                username=user_data["username"],
                email=user_data["email"],
                address=user_data["address"],
                phone=user_data["phone"],
                website=user_data["website"],
                company=user_data["company"]
            )
            db.add(db_user)
        
        db.commit()
        print(f"Successfully seeded database with {len(users_data)} users.")
        
    except requests.RequestException as e:
        print(f"Error fetching data from JSONPlaceholder: {e}")
        # Fallback to hardcoded data
        seed_with_fallback_data(db)
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

def seed_with_fallback_data(db: Session):
    """Seed database with fallback data if API is unavailable"""
    fallback_users = [
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        },
        {
            "id": 2,
            "name": "Ervin Howell",
            "username": "Antonette",
            "email": "Shanna@melissa.tv",
            "address": {
                "street": "Victor Plains",
                "suite": "Suite 879",
                "city": "Wisokyburgh",
                "zipcode": "90566-7771",
                "geo": {
                    "lat": "-43.9509",
                    "lng": "-34.4618"
                }
            },
            "phone": "010-692-6593 x09125",
            "website": "anastasia.net",
            "company": {
                "name": "Deckow-Crist",
                "catchPhrase": "Proactive didactic contingency",
                "bs": "synergize scalable supply-chains"
            }
        },
        {
            "id": 3,
            "name": "Clementine Bauch",
            "username": "Samantha",
            "email": "Nathan@yesenia.net",
            "address": {
                "street": "Douglas Extension",
                "suite": "Suite 847",
                "city": "McKenziehaven",
                "zipcode": "59590-4157",
                "geo": {
                    "lat": "-68.6102",
                    "lng": "-47.0653"
                }
            },
            "phone": "1-463-123-4447",
            "website": "ramiro.info",
            "company": {
                "name": "Romaguera-Jacobson",
                "catchPhrase": "Face to face bifurcated interface",
                "bs": "e-enable strategic applications"
            }
        }
    ]
    
    for user_data in fallback_users:
        db_user = User(**user_data)
        db.add(db_user)
    
    db.commit()
    print(f"Successfully seeded database with {len(fallback_users)} fallback users.")
