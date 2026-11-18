def is_valid_bug_description(description):
    """Return True if the description contains non-whitespace text."""
    return isinstance(description, str) and bool(description.strip())
