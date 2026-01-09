def define_env(env):
    """
    Make YAML front-matter fields available as {{ variables }} in Markdown pages.
    Example: front-matter 'code: s1' becomes usable as {{ code }}.
    """
    # env.page is available when rendering pages
    meta = getattr(env, "page", None)
    if meta and hasattr(env.page, "meta") and isinstance(env.page.meta, dict):
        env.variables.update(env.page.meta)
