import os
import time
import sys
import random
import threading
import json
import http.client
from flask import Flask, jsonify

print("🔥 [NÚCLEO ENJAMBRE] Malla API HTTP Brevo Unificada Activa", flush=True)

app = Flask(__name__)

ciudades = ["Asuncion", "Madrid", "Barcelona", "New York", "Los Angeles", "Ciudad de Mexico", "Monterrey", "Bogota", "Medellin", "Sydney", "Melbourne", "Rome", "Milan", "Tokyo", "Osaka", "Singapore", "Seul", "Busan", "London", "Paris", "Berlin", "Frankfurt", "Amsterdam", "Zurich", "Miami", "San Francisco", "Toronto", "Sao Paulo", "Buenos Aires", "Santiago", "Lima", "Dubai", "Hong Kong", "Shanghai", "Bangkok", "Mumbai", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "Indianapolis", "Seattle", "Denver", "Washington", "Boston", "El Paso", "Nashville", "Oklahoma City", "Las Vegas", "Portland", "Valencia", "Sevilla", "Zaragoza", "Malaga", "Murcia", "Palma de Mallorca", "Las Palmas", "Bilbao", "Guadalajara", "Puebla", "Tijuana", "Leon", "Juarez", "Zapopan", "Cali", "Barranquilla", "Cartagena", "Cucuta", "Guayaquil", "Quito", "Caracas", "Maracaibo", "Valencia Venezuela", "Montevideo", "La Paz", "Santa Cruz", "Manchester", "Birmingham", "Leeds", "Glasgow", "Munich", "Hamburg", "Cologne", "Stuttgart", "Lyon", "Marseille", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier"]

sectores = [
    ("tienda online", "19,00 €", "fugas de carritos abandonados", "fZuaEY1ykgiZedM0KR77O0u"),
    ("restaurante", "24,00 €", "mesas vacías en días laborables", "14AdRaccY4Ah3z865b77O0t"),
    ("clinica dental", "29,00 €", "perdida de posicionamiento local en mapas", "6oU14occY7Mt3z8gJP77O0s"),
    ("negocio local", "97,00 €", "optimizacion de captacion digital", "dRm14o1yk9UB6Lk2SZ77O0r"),
    ("comercio premium", "147,00 €", "fidelizacion de clientes VIP", "7sYbJ2ccY3wd0mW3X377O0q"),
    ("plataforma financiera", "197,00 €", "integracion de activos digitales", "4gMdRab8UaYF3z851777O0p"),
    ("agencia de servicios", "47,00 €", "posicionamiento web y SEO", "eVq7sM90M7MtedM9hn77O0o"),
    ("vendedor amazon", "127,00 €", "análisis de trends de mercado", "3cIeVe90M1o50mWeBH77O0n"),
    ("marca de e-commerce", "297,00 €", "inteligencia y optimizacion de anuncios", "cNifZi7WId6N2v479f77O0m"),
    ("establecimiento comercial", "87,00 €", "gestion de reputacion y resenas de Google", "dRm5kE1ykfeV7Po51777O0l"),
    ("gran empresa", "997,00 €", "estrategias de omnipresencia corporativa", "3cI4gAccY0k19Xw9hn77O0k"),
    ("empresa tecnologica", "497,00 €", "auditoria de seguridad y cyber-shield", "14AeVe4Kwd6Nc5E1OV77O0j"),
    ("corporacion", "49,00 €", "cumplimiento normativo e inteligencia artificial", "fZudRa90M4Ah4Dcalr77O0i"),
    ("creador de contenido", "99,00 €", "conversion de catalogo a video vertical", "cNi28sdh22s9glU8dj77O0h"),
    ("centro de atencion", "199,00 €", "cierre de ventas automatizado por WhatsApp", "fZu4gAfpagiZglU51777O0g")
]

correos_historico = set()
busquedas_exitosas = 0
busquedas_fallidas = 0
leads_cazados = 0
emails_exito = 0
emails_failed = 0

@app.route('/')
def home():
    return jsonify({
        "status": "online", 
        "scans_exitosos": busquedas_exitosas, 
        "scans_fallidos": busquedas_fallidas, 
        "leads_reales_cazados": leads_cazados, 
        "emails_enviados_exito": emails_exito, 
        "emails_failed": emails_failed
    }), 200

@app.route('/ejecutar')
def forzar_ciclo():
    threading.Thread(target=ejecutar_un_ciclo_cibernetico).start()
    return jsonify({"status": "ciclo_forzado_malla_api"}), 200

def enviar_propuesta_api_http(email, sector, problema, precio, enlace):
    global emails_exito, emails_failed
    try:
        api_key = os.getenv("BREVO_API_KEY")
        sender_email = os.getenv("SENDER_EMAIL", "info@enjambresaas.online")
        sender_name = "Enjambre SaaS"
        
        if not api_key:
            print("[⚠️] Error Crítico: Falta la clave secreta BREVO_API_KEY en Render.", flush=True)
            emails_failed += 1
            return

        print(f"⚡ [CONEXIÓN API BREVO] Enviando propuesta por puerto web seguro a: {email}", flush=True)

        # 🚀 CORRECCIÓN ABSOLUTA: Host limpio directo de la API sin barras corruptas
        conn = http.client.HTTPSConnection("api.brevo.com")
        
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": api_key
        }
        
        html_content = f"<p>Hola,</p><p>Detectamos que has registrado recientemente la infraestructura digital de tu marca. Analizando los protocolos estandar de despliegue, prevemos riesgos criticos con <strong>{problema}</strong>.</p><p>Implementamos una Malla Blindada con IA para asegurar tu entorno por <strong>{precio} al mes (pago adelantado)</strong>.</p><p>Puedes activar tu protección y revisar los entregables de forma segura en nuestra pasarela aquí:</p><p><a href='{enlace}' style='background:#6772e5;color:#fff;padding:12px 20px;text-decoration:none;border-radius:5px;display:inline-block;font-weight:bold;'>Activar Malla Blindada (Stripe Checkout)</a></p><p><em>Nota: El soporte 24/7 y la infraestructura en la nube inician tras completarse el pago seguro. Sin versiones de prueba.</em></p>"
        
        payload = {
            "sender": {"name": sender_name, "email": sender_email},
            "to": [{"email": email}],
            "subject": f"Solucion urgente para {problema} en tu {sector}",
            "htmlContent": html_content
        }

        conn.request("POST", "/v3/smtp/email", json.dumps(payload), headers)
        
        # Lectura de respuesta limpia directa del servidor de Brevo
        response = conn.getcall = response = conn.getresponse()
        data = response.read().decode("utf-8")
        
        if response.status == 201:
            emails_exito += 1
            print(f"✅ [API ÉXITO] ¡Túnel abierto en Brevo! Correo entregado a: {email}", flush=True)
        else:
            emails_failed += 1
            print(f"❌ [API RECHAZO] Código {response.status} de la central de Brevo: {data}", flush=True)
        conn.close()
            
    except Exception as e:
        emails_failed += 1
        print(f"❌ [FALLA TOTAL DE RED] Error en conexión pura a {email}: {e}", flush=True)

def ejecutar_un_ciclo_cibernetico():
    global busquedas_exitosas, busquedas_fallidas, leads_cazados
    try:
        ciudad = random.choice(ciudades)
        sector, precio, problema, cod_stripe = random.choice(sectores)
        enlace_stripe = f"https://stripe.com{cod_stripe}"
        
        print(f"🔍 [RADAR INTERNO] Ejecutando escaneo de prueba directa...", flush=True)
        
        # Objetivo directo a tu propio Hotmail para comprobar el impacto en segundos
        email_objetivo = "severianobenitez@hotmail.com"
        
        busquedas_exitosas += 1
        if email_objetivo not in correos_historico:
            leads_cazados += 1
            enviar_propuesta_api_http(email_objetivo, sector, problema, precio, enlace_stripe)
            
    except Exception as e:
        busquedas_fallidas += 1
        print(f"❌ [FALLA INTERNA] Error de rastreo: {e}", flush=True)

def inicio_automatico():
    time.sleep(10)
    while True:
        print("🚀 [MALLA OPERATIVA 24/7] Escaneando registros...", flush=True)
        ejecutar_un_ciclo_cibernetico()
        # Pausa de seguridad humana de 20 a 30 minutos
        espera = random.randint(1200, 1800)
        print(f"⏳ [RELOJ INTERNO] Próxima patrulla en {espera} segundos...", flush=True)
        time.sleep(espera)

if __name__ == '__main__':
    threading.Thread(target=inicio_automatico, daemon=True).start()
    puerto = int(os.environ.get("PORT", 10000))
    print(f"🌐 Servidor Flask arrancando en puerto {puerto}...", flush=True)
    app.run(host='0.0.0.0', port=puerto, debug=False, use_reloader=False)
