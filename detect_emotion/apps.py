from django.apps import AppConfig
from detect_emotion.utils.calma_model import CalmaModel


class DetectEmotionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'detect_emotion'
    detect_model = CalmaModel()

    def ready(self):
        self.detect_model.load_model()
    
    
    