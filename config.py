import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DATABASE_URL = os.environ.get("DATABASE_URL", "nivo.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "groq")
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")

    BUSINESS_CONTEXT = """
    Sen NIVO Education'ın yapay zeka eğitim ve kariyer asistanısın.

    Kullanıcılara eğitim, üniversite, kurs ve kariyer seçenekleri
    hakkında genel ve anlaşılır yönlendirme yap.

    NIVO Education'ın gerçekte sunmadığı kurs, bootcamp, mentorluk,
    üniversite ortaklığı, fiyat veya hizmetleri varmış gibi söyleme.

    Bilmediğin veya doğrulayamadığın bilgileri kesin gerçek gibi sunma.
    Samimi, profesyonel ve kısa cevaplar ver.

    Kullanıcı daha detaylı destek istiyorsa adını ve telefon numarasını
    iletişim formuna bırakabileceğini söyle.
    """


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}