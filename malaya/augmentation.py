import random
import inspect
import numpy as np
import string as string_function
from tensorflow.keras.preprocessing.sequence import pad_sequences
from herpetologist import check_type
from typing import List, Dict, Tuple, Callable


def to_ids(string, tokenizer):
    words = []
    for no, word in enumerate(string):
        if word == '[MASK]':
            words.append(word)
        else:
            words.extend(tokenizer.tokenize(word))
    masked_tokens = ['[CLS]'] + words + ['[SEP]']
    masked_ids = tokenizer.convert_tokens_to_ids(masked_tokens)
    return masked_ids, masked_ids.index(tokenizer.vocab['[MASK]'])


def synonym():
    pass


def tfidf():
    pass


@check_type
def wordvector(
    string: str,
    wordvector,
    threshold: float = 0.5,
    top_n: int = 5,
    soft: bool = False,
    cleaning_function: Callable = None,
):
    """
    augmenting a string using wordvector.

    Parameters
    ----------
    string: str
    wordvector: object
        wordvector interface object.
    threshold: float, optional (default=0.5)
        random selection for a word.
    soft: bool, optional (default=False)
        if True, a word not in the dictionary will be replaced with nearest jarowrinkler ratio.
        if False, it will throw an exception if a word not in the dictionary.
    top_n: int, (default=5)
        number of nearest neighbors returned.
    cleaning_function: function, (default=None)
        function to clean text.

    Returns
    -------
    result: list
    """
    if not hasattr(wordvector, 'batch_n_closest'):
        raise ValueError('wordvector must has `batch_n_closest` method')
    if not hasattr(wordvector, '_dictionary'):
        raise ValueError('wordvector must has `_dictionary` attribute')

    original_string = string
    if cleaning_function:
        string = cleaning_function(string)
    string = _tokenizer(string)
    original_string = string[:]
    selected = []
    for no, w in enumerate(string):
        if w in string_function.punctuation:
            continue
        if w[0].isupper():
            continue
        if random.random() > threshold:
            selected.append((no, w))

    if not len(selected):
        raise ValueError(
            'no words can augmented, make sure words available are not punctuation or proper nouns.'
        )

    indices, words = [i[0] for i in selected], [i[1] for i in selected]
    batch_parameters = list(
        inspect.signature(wordvector.batch_n_closest).parameters.keys()
    )
    if 'soft' in batch_parameters:
        results = wordvector.batch_n_closest(
            words, num_closest = top_n, soft = soft
        )
    else:
        results = wordvector.batch_n_closest(words, num_closest = top_n)

    augmented = []
    for i in range(top_n):
        string_ = string[:]
        for no in range(len(results)):
            string_[indices[no]] = results[no][i]
        augmented.append(
            _make_upper(' '.join(string_), ' '.join(original_string))
        )
    return augmented


@check_type
def transformer(
    string: str,
    model,
    threshold: float = 0.5,
    top_p: float = 0.8,
    top_k: int = 100,
    temperature: float = 0.8,
    top_n: int = 5,
    cleaning_function: Callable = None,
):

    """
    augmenting a string using transformer + nucleus sampling / top-k sampling.

    Parameters
    ----------
    string: str
    model: object
        transformer interface object. Right now only supported BERT, ALBERT.
    threshold: float, optional (default=0.5)
        random selection for a word.
    top_p: float, optional (default=0.8)
        cumulative sum of probabilities to sample a word. If top_n bigger than 0, the model will use nucleus sampling, else top-k sampling.
    top_k: int, optional (default=100)
        k for top-k sampling.
    temperature: float, optional (default=0.8)
        logits * temperature.
    top_n: int, (default=5)
        number of nearest neighbors returned.
    cleaning_function: function, (default=None)
        function to clean text.

    Returns
    -------
    result: list
    """

    if not hasattr(model, 'samples'):
        raise ValueError('model must has `samples` attribute')
    if not (threshold > 0 and threshold < 1):
        raise ValueError('threshold must be bigger than 0 and less than 1')
    if not top_p > 0:
        raise ValueError('top_p must be bigger than 0')
    if not top_k > 0:
        raise ValueError('top_k must be bigger than 0')
    if not 0 < temperature <= 1.0:
        raise Exception('temperature must, 0 < temperature <= 1.0')
    if not top_n > 0:
        raise ValueError('top_n must be bigger than 0')
    if top_n > top_k:
        raise ValueError('top_k must be bigger than top_n')

    original_string = string
    if cleaning_function:
        string = cleaning_function(string)
    string = _tokenizer(string)
    results = []
    for token_idx, token in enumerate(string):
        if token in string_function.punctuation:
            continue
        if token[0].isupper():
            continue
        if token.isdigit():
            continue
        if random.random() > threshold:
            results.append(token_idx)

    if not len(results):
        raise ValueError(
            'no words can augmented, make sure words available are not punctuation or proper nouns.'
        )

    maskeds, indices, input_masks = [], [], []
    for index in results:
        new = string[:]
        new[index] = '[MASK]'
        mask, ind = to_ids(new, model._tokenizer)
        maskeds.append(mask)
        indices.append(ind)
        input_masks.append([1] * len(mask))

    masked_padded = pad_sequences(maskeds, padding = 'post')
    input_masks = pad_sequences(input_masks, padding = 'post')
    batch_indices = np.array([np.arange(len(indices)), indices]).T
    samples = model._sess.run(
        model.samples,
        feed_dict = {
            model.X: masked_padded,
            model.MASK: input_masks,
            model.top_p: top_p,
            model.top_k: top_k,
            model.temperature: temperature,
            model.indices: batch_indices,
            model.k: top_n,
        },
    )
    outputs = []
    for i in range(samples.shape[1]):
        sample_i = samples[:, i]
        samples_tokens = model._tokenizer.convert_ids_to_tokens(
            sample_i.tolist()
        )
        new_splitted = ['▁' + w if len(w) > 1 else w for w in string]
        for no, index in enumerate(results):
            new_splitted[index] = samples_tokens[no]
        new = ''.join(model._tokenizer.sp_model.DecodePieces(new_splitted))
        outputs.append(new)
    return outputs
