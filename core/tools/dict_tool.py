def dict_slice_by_keys(d, start_key, end_key, inclusive=True):
    keys = list(d.keys())
    try:
        start_idx = keys.index(start_key)
        end_idx = keys.index(end_key)
    except ValueError:
        raise KeyError("One of keys not found")

    if start_idx > end_idx:
        raise ValueError("start_key must go before end_key")

    if inclusive:
        end_idx += 1

    sliced_items = list(d.items())[start_idx:end_idx]

    return [value for key, value in sliced_items]
