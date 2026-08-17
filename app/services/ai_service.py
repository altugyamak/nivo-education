import re
import requests

from config import Config


class AIServiceError(Exception):
    pass


class AIService:
    def _get_system_prompt(self):
        return Config.BUSINESS_CONTEXT

    def yanit_uret(self, mesaj, gecmis=None):
        gecmis = gecmis or []

        api_key = Config.GROQ_API_KEY

        if not api_key:
            return (
                "Demo modu aktif. NIVO Education olarak eğitim ve kariyer "
                "seçenekleri hakkında genel yönlendirme sağlayabilirim. "
                "Daha detaylı destek için iletişim bilgilerinizi bırakabilirsiniz."
            )

        messages = [
            {
                "role": "system",
                "content": self._get_system_prompt()
            }
        ]

        messages.extend(gecmis)

        messages.append(
            {
                "role": "user",
                "content": mesaj
            }
        )

        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "qwen/qwen3.6-27b",
                    "messages": messages
                },
                timeout=30
            )

            response.raise_for_status()
            data = response.json()

            cevap = data["choices"][0]["message"]["content"]

            # Kullanıcıya modelin iç düşünme bölümünü göstermemek için temizler.
            cevap = re.sub(
                r"<think>.*?</think>",
                "",
                cevap,
                flags=re.DOTALL
            ).strip()

            return cevap

        except requests.RequestException as exc:
            raise AIServiceError(
                "Yapay zeka servisine ulaşılamadı."
            ) from exc

        except (KeyError, IndexError, TypeError) as exc:
            raise AIServiceError(
                "Yapay zeka servisinden beklenmeyen bir yanıt alındı."
            ) from exc


ai_service = AIService()