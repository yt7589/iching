# 应用系统注册表

class SopRegistry(object):
    PARAMS = {}

    @classmethod
    def put(cls, key, val):
        SopRegistry.PARAMS[key] = val

    @classmethod
    def get(cls, key):
        if key in SopRegistry.PARAMS:
            return SopRegistry.PARAMS[key]
        else:
            return None

    K_POSITION = 'position'
    K_OPTION_CODES = 'option_codes'
    K_OC_TO_IDX = 'oc_to_idx'