def decrypt_story():
    story = CiphertextMessage(get_story_string())
    return story.decrypt_message()
    