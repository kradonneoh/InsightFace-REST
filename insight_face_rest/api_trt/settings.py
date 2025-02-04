from typing import Union, Optional, List

from pydantic import BaseSettings
from pydantic.validators import str_validator


def empty_to_none(v: str) -> Optional[str]:
    if v == '' or v.lower() == "none":
        return None
    return v


def str_to_int_list(v):
    if isinstance(v, str):
        val = list(map(int, v.split(',')))
        return val
    else:
        return v


class StrToIntList(str):
    @classmethod
    def __get_validators__(cls):
        yield str_to_int_list


class EmptyStrToNone(str):
    @classmethod
    def __get_validators__(cls):
        yield str_validator
        yield empty_to_none


class Defaults(BaseSettings):
    return_face_data: bool = False
    return_landmarks: bool = False
    extract_embedding: bool = True
    extract_ga: bool = False
    detect_masks: bool = False
    api_ver: str = "1"

    class Config:
        env_prefix = 'DEF_'


class Models(BaseSettings):
    inference_backend: str = 'onnx'
    det_name: str = 'scrfd_10g_gnkps'
    rec_name: str = 'glintr100'
    det_thresh: float = 0.6
    max_size: Union[StrToIntList, List[int]] = [640, 640]
    ga_name: Union[EmptyStrToNone, None, str] = None
    mask_detector: Union[EmptyStrToNone, None, str] = None
    rec_batch_size: int = 1
    det_batch_size: int = 1
    force_fp16: bool = False
    triton_uri: str = None


class Settings(BaseSettings):
    log_level: str = 'INFO'
    port: int = 18080
    models = Models()
    defaults = Defaults()
