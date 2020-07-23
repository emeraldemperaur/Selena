# Set WebDriver of choice: chrome, gecko, opera, msedge, ie
# Set Legion Mode: enabled or disabled
# Set Headless Mode: enabled or disabled
# Set Narrator: enabled or disabled

core_preferences = {
    "x_driver": "msedge",
    "narrator": "enabled",
    "legion_mode": "enabled",
    "headless": "disabled",
    "ops_objective": "Sanctum"
}


def fetch_core_preferences():
    return core_preferences

