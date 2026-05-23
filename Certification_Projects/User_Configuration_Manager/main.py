def add_setting(settings, single_setting):
    single_setting_lower = tuple(map(str.lower, single_setting))
    if single_setting_lower[0] in settings:
        return f"Setting '{single_setting_lower[0]}' already exists! Cannot add a new setting with this name."
    else:
        settings[single_setting_lower[0]] = single_setting_lower[1]
        return f"Setting '{single_setting_lower[0]}' added with value '{single_setting_lower[1]}' successfully!"

def update_setting(settings, single_setting):
    single_setting_lower = tuple(map(str.lower, single_setting))
    if single_setting_lower[0] in settings:
        settings[single_setting_lower[0]] = single_setting_lower[1]
        return f"Setting '{single_setting_lower[0]}' updated to '{single_setting_lower[1]}' successfully!"
    else:
        return f"Setting '{single_setting_lower[0]}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, single_setting_key):
    single_setting_key_lower = single_setting_key.lower()
    if single_setting_key_lower in settings:
        del settings[single_setting_key_lower]
        return f"Setting '{single_setting_key_lower}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    else:
        settings_display = "Current User Settings:\n"
        for setting_key, setting_value in settings.items():
            settings_display += f"{setting_key.capitalize()}: {setting_value}\n"
        return settings_display

test_settings = {
    'color': 'Golden',
    'Volume': 'medium',
    'theme': 'island'
}
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))