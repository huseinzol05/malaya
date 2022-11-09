from herpetologist import check_type
from malaya.supervised import huggingface as load_huggingface
from malaya.function import describe_availability
import logging

logger = logging.getLogger(__name__)

_huggingface_availability = {
    'mesolitica/finetune-zeroshot-ner-t5-tiny-standard-bahasa-cased': {
        'Size (MB)': 139,
        'WER': 0,
        'CER': 0,
    },
    'mesolitica/finetune-zeroshot-ner-t5-small-standard-bahasa-cased': {
        'Size (MB)': 242,
        'WER': 0,
        'CER': 0,
    },
    'mesolitica/finetune-zeroshot-ner-t5-base-standard-bahasa-cased': {
        'Size (MB)': 892,
        'WER': 0,
        'CER': 0,
    },
}


def available_huggingface():
    """
    List available huggingface models.
    """

    logger.info('tested on test set, https://huggingface.co/datasets/mesolitica/zeroshot-NER')
    return describe_availability(_huggingface_availability)


def huggingface(model: str = 'mesolitica/finetune-zeroshot-ner-t5-small-standard-bahasa-cased', **kwargs):
    """
    Load HuggingFace model to zeroshot NER.

    Parameters
    ----------
    model: str, optional (default='mesolitica/finetune-zeroshot-ner-t5-small-standard-bahasa-cased')
        Check available models at `malaya.zero_shot.entity.available_huggingface()`.

    Returns
    -------
    result: malaya.torch_model.huggingface.ZeroShotNER
    """

    if model not in _huggingface_availability:
        raise ValueError(
            'model not supported, please check supported models from `malaya.zero_shot.entity.available_huggingface()`.'
        )
    return load_huggingface.load_zeroshot_ner(model=model, **kwargs)