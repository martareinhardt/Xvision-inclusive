from modules.survey import get_user_tier, collect_interests

def main():
    tier = get_user_tier()
    interests = collect_interests(tier)
    print(f"Interesses escolhidos: {interests}")

if __name__ == "__main__":
    main()
