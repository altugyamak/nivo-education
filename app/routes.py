from flask import Blueprint, jsonify, render_template, request, current_app

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError


pages_bp = Blueprint("pages", __name__)
api_bp = Blueprint("api", __name__)


@pages_bp.route("/")
def index():
    return render_template("index.html")


@pages_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@api_bp.route("/sohbet", methods=["POST"])
def sohbet():
    data = request.get_json(silent=True) or {}

    mesaj = data.get("mesaj", "").strip()
    gecmis = data.get("gecmis", [])

    if not mesaj:
        return jsonify({
            "basari": False,
            "hata": "Mesaj alanı zorunludur."
        }), 400

    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)

        return jsonify({
            "basari": True,
            "cevap": cevap
        })

    except AIServiceError:
        return jsonify({
            "basari": False,
            "hata": "Yapay zeka servisine şu anda ulaşılamıyor."
        }), 503


@api_bp.route("/leads", methods=["POST"])
def yeni_lead():
    data = request.get_json(silent=True) or {}

    isim = data.get("isim", "").strip()
    email = data.get("email", "").strip()
    telefon = data.get("telefon", "").strip()
    mesaj = data.get("mesaj", "").strip()

    if not isim or not email or not telefon:
        return jsonify({
            "basari": False,
            "hata": "İsim, e-posta ve telefon alanları zorunludur."
        }), 400

    try:
        lead_id = lead_ekle(
            isim,
            email,
            telefon,
            mesaj
        )

        return jsonify({
            "basari": True,
            "id": lead_id
        }), 201

    except Exception as exc:
        print("Lead kayıt hatası:", exc)

        return jsonify({
            "basari": False,
            "hata": "Kayıt sırasında bir hata oluştu."
        }), 500


@api_bp.route("/leads", methods=["GET"])
def leadleri_listele():
    admin_password = request.headers.get("X-Admin-Password")
    expected_password = current_app.config.get("ADMIN_PASSWORD")

    if not expected_password or admin_password != expected_password:
        return jsonify({
            "basari": False,
            "hata": "Yetkisiz erişim."
        }), 401

    try:
        leadler = tum_leadler()

        return jsonify({
            "basari": True,
            "leadler": leadler
        })

    except Exception:
        return jsonify({
            "basari": False,
            "hata": "Kayıtlar alınırken bir hata oluştu."
        }), 500