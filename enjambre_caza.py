import os
import time
import sys
import random
import threading
import json
import http.client
from flask import Flask, jsonify

print("🔥 [NÚCLEO ENJAMBRE] Malla API HTTP Brevo Operativa Real - EN LA CALLE", flush=True)

app = Flask(__name__)

# 🎯 BASE DE DATOS DE CLIENTES REALES (Cambia estos correos por los verdaderos de tus objetivos)
lista_leads_reales = [
    {"email": "severianobenitez@hotmail.com", "sector": "comercio premium", "problema": "fidelizacion de clientes VIP", "cod_stripe": "7sYbJ2ccY3wd0mW3X377O0q", "precio": "147,00 €"},
    {"email": "info@enjambresaas.online", "sector": "agencia de servicios", "problema": "posicionamiento web y SEO", "cod_stripe": "eVq7sM90M7MtedM9hn77O0o", "precio": "47,00 €"}
]

busquedas_exitosas = 0
busquedas_fallidas = 0
leads_cazados = 0
emails_exito = 0
emails_failed = 0
indice_actual = 0

@app.route('/')
def home():
    return jsonify({
        "status": "online", 
        "scans_exitosos": busquedas_exitosas, 
        "scans_fallidos": busquedas_fallidas, 
        "leads_reales_cazados": leads_cazados, 
        "emails_enviados_exito": emails_exito, 
        "emails_failed": emails_failed,
        "proximo_indice_lista": indice_actual
    }), 200

def enviar_propuesta_api_http(email, sector, problema, precio, enlace):
    global emails_exito, emails_failed
    try:
        api_key = os.getenv("BREVO_API_KEY")
        sender_email = os.getenv("SENDER_EMAIL", "oficina@enjambresaas.online")
        sender_name = os.getenv("SENDER_NAME", "Enjambre SaaS")
        
        if not api_key:
            print("[⚠️] Error Crítico: Falta la clave secreta BREVO_API_KEY en Render.", flush=True)
            emails_failed += 1
            return

        print(f"⚡ [CONEXIÓN API BREVO] Enviando propuesta por puerto web seguro a: {email}", flush=True)

        conn = http.client.HTTPSConnection("://brevo.com")
        
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
        
        response = conn.getcall = response = conn.getcall = response = conn.getresponse()
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

def bucle_automatico_infinito():
    global busquedas_exitosas, busquedas_fallidas, leads_cazados, indice_actual
    print("🚀 [MALLA AUTOMÁTICA] Bucle de patrulla secuencial en segundo plano iniciado.", flush=True)
    
    time.sleep(10)
    
    while True:
        try:
            if not lista_leads_reales:
                print("⚠️ [RADAR] La lista de leads está vacía. Esperando...", flush=True)
                time.sleep(60)
                continue
                
            # Coger el cliente actual secuencialmente
            lead = lista_leads_reales[indice_actual]
            email_objetivo = lead["email"]
            sector = lead["sector"]
            problema = lead["problema"]
            precio = lead["precio"]
            enlace_stripe = f"https://stripe.com{lead['cod_stripe']}"
            
            print(f"🔍 [RADAR INTERNO] Procesando objetivo real: {email_objetivo}", flush=True)
            
            busquedas_exitosas += 1
            leads_cazados += 1
            
            enviar_propuesta_api_http(email_objetivo, sector, problema, precio, enlace_stripe)
            
            # Avanzar al siguiente correo de la lista
            indice_actual = (indice_actual + 1) % len(lista_leads_reales)
            
        except Exception as e:
            busquedas_fallidas += 1
            print(f"❌ [RADAR ERROR] Fallo en ciclo automático: {e}", flush=True)
        
        print("⏳ [RELOJ INTERNO] Próxima patrulla en 900 segundos...", flush=True)
        time.sleep(900)

threading.Thread(target=bucle_automatico_infinito, daemon=True).start()

if __name__ == '__main__':
    port = int(os.getenv("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
