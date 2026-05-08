
def print_results(state):
    print("="*70)
    print("🎉 MULTI-PLATFORM SOCIAL ENGINE - FINAL OUTPUT")
    print("="*70)

    print("\n📸 INSTAGRAM CAPTION:")
    print("-" * 40)
    print(state.get("instagram_caption", "Not generated"))

    print("\n💼 LINKEDIN POST:")
    print("-" * 40)
    print(state.get("linkedin_post", "Not generated"))

    print("\n📝 LINKEDIN ARTICLE:")
    print("-" * 40)
    article = state.get("linkedin_article", "Not generated")
    print(article[:800] + "..." if len(article) > 800 else article)

    print("\n📢 ANNOUNCEMENT MESSAGE:")
    print("-" * 40)
    print(state.get("announcement_message", "Not generated"))

    print("\n" + "="*70)
