import re
def get_mood_emoji(text):
    # Dictionary mapping keywords to emojis
    mood_emojis = {
        # Happy emotions
        r'\b(happy|joy|joyful|delighted|ecstatic)\b': '😊',
        r'\b(love|adore|affection|romance)\b': '❤️',
        r'\b(excited|enthusiastic|thrilled)\b': '🤩',
        r'\b(laugh|funny|hilarious|joke)\b': '😂',
        r'\b(party|celebrate|celebration)\b': '🎉',  
        # Sad emotions
        r'\b(sad|sorrow|unhappy|depressed)\b': '😢',
        r'\b(cry|crying|tears|weep)\b': '😭',
        r'\b(lonely|alone|isolated)\b': '😔', 
        # Angry emotions
        r'\b(angry|mad|furious|rage)\b': '😠',
        r'\b(annoyed|irritated|frustrated)\b': '😤',
        # Surprised emotions
        r'\b(surprise|surprised|shocked|amazed)\b': '😲',
        r'\b(wow|awesome|impressive)\b': '😮',
        # Fearful emotions
        r'\b(scared|afraid|fear|terrified)\b': '😨',
        r'\b(nervous|anxious|worried)\b': '😰',
        # Tired/sleepy
        r'\b(tired|exhausted|fatigued)\b': '😫',
        r'\b(sleepy|drowsy|zzz)\b': '😴',
        # Neutral/other
        r'\b(okay|ok|fine|alright)\b': '😐',
        r'\b(cool|awesome|great)\b': '😎',
        r'\b(hungry|starving|food)\b': '🍕',
        r'\b(sick|ill|unwell)\b': '🤒',
        r'\b(confused|puzzled)\b': '😕',
        r'\b(thinking|ponder|consider)\b': '🤔',
        r'\b(shy|bashful|embarrassed)\b': '😳',
        r'\b(music|song|sing|dance)\b': '🎵',
        r'\b(rain|raining|storm)\b': '🌧️',
        r'\b(sun|sunny|bright)\b': '☀️',
        r'\b(work|busy|stressed)\b': '💼',
        r'\b(exercise|workout|gym)\b': '💪',
        r'\b(study|learn|read|book)\b': '📚',
        r'\b(game|play|fun)\b': '🎮',
    }    
    text = text.lower() 
    # Check for matches in the dictionary
    for pattern, emoji in mood_emojis.items():
        if re.search(pattern, text):
            return emoji
    # Default emoji if no match found
    return '🤷'
# Get user input and display result
user_input = input("Type a word or phrase to get a matching mood emoji: ")
matched_emoji = get_mood_emoji(user_input)
print(f"\nYour mood emoji is: {matched_emoji}")
