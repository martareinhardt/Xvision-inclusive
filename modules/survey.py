CATEGORIES = ["Ciência", "Tecnologia", "Espaço", "IA", "Cosmologia", "BioMachines", "ScienceNuts"]

def get_user_tier():
    print("Qual seu tier no X? (free/premium/premium_plus)")
    return input().strip().lower()

def collect_interests(tier):
    max_themes = {"free": 20, "premium": 50, "premium_plus": 100}.get(tier, 20)
    print(f"Escolha até {max_themes} categorias (separe por vírgula): {', '.join(CATEGORIES)}")
    selected = input().strip().split(", ")
    return [s.strip() for s in selected if s.strip() in CATEGORIES][:max_themes]
