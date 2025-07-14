def define_env(env):
    @env.macro
    def icon(name, alt=None):
        if alt is None:
            alt = name
        return f'<img src="assets/icons/{name}.png" alt="{alt}" class="icon" />'