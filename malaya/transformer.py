from herpetologist import check_type

_availability = [
    'bert',
    'tiny-bert',
    'albert',
    'tiny-albert',
    'xlnet',
    'alxlnet',
    'small-electra',
    'electra',
]


def available_model():
    """
    List available transformer models.
    """
    return _availability


@check_type
def load(model: str = 'electra', pool_mode: str = 'last', **kwargs):

    """
    Load transformer model.

    Parameters
    ----------
    model : str, optional (default='bert')
        Model architecture supported. Allowed values:

        * ``'bert'`` - BERT architecture from google.
        * ``'tiny-bert'`` - BERT architecture from google with smaller parameters.
        * ``'albert'`` - ALBERT architecture from google.
        * ``'tiny-albert'`` - ALBERT architecture from google with smaller parameters.
        * ``'xlnet'`` - XLNET architecture from google.
        * ``'alxlnet'`` - XLNET architecture from google + Malaya.
        * ``'small-electra'`` - ELECTRA architecture from google with smaller parameters
        * ``'electra'`` - ELECTRA architecture from google.


    pool_mode : str, optional (default='last')
        Model logits architecture supported. Only usable if model in ['xlnet', 'alxlnet']. Allowed values:

        * ``'last'`` - last of the sequence.
        * ``'first'`` - first of the sequence.
        * ``'mean'`` - mean of the sequence.
        * ``'attn'`` - attention of the sequence.

    Returns
    -------
    TRANSFORMER: malaya.transformers.* class
    """

    model = model.lower()
    if model not in _availability:
        raise Exception(
            'model not supported, please check supported models from malaya.transformer.available_model()'
        )
    if model in ['bert', 'tiny-bert']:
        from malaya.transformers.bert import load

        return load(model = model, **kwargs)
    if model in ['albert', 'tiny-albert']:
        from malaya.transformers.albert import load

        return load(model = model, **kwargs)
    if model in ['xlnet']:
        from malaya.transformers.xlnet import load

        return load(model = model, pool_mode = pool_mode, **kwargs)

    if model in ['alxlnet']:
        from malaya.transformers.alxlnet import load

        return load(model = model, pool_mode = pool_mode, **kwargs)

    if model in ['electra', 'small-electra']:
        from malaya.transformers.electra import load

        return load(model = model, **kwargs)
