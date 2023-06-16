from split_settings.tools import include
base_settings = [
    'components/*.py',
    # 'development/*.py',
    'production/*.py'
]
include(*base_settings)