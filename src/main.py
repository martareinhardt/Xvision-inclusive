import uuid
from modules.survey import get_user_tier, collect_interests
from modules.storage import init_db, save_interests, get_interests
from modules.grok_feed import fetch_x_posts
from modules.ranking import rank_posts

def main():
    init_db()
    user_id = str(uuid.uuid4())  # Simula X ID
    tier = get_user_tier()
    interests = collect_interests(tier)
    save_interests(user_id, tier, interests)
    
    print("\nSeu Feed Interativo (by Grok):")
    posts = fetch_x_posts(interests)
    feed = rank_posts(posts, interests, user_id, tier)
    for post in feed:
        print(f"Post: {post['text']}\nMotivo: {post['reason']}\n---")

if __name__ == "__main__":
    main()
