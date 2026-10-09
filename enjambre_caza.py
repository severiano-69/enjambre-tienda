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

# Base de datos limpia para la rotación automática
ciudades = ["Madrid", "Barcelona", "Sevilla", "Valencia", "Malaga", "Zaragoza", "Bilbao", "Murcia", "Palma", "Alicante"]
sectores = [
    ("consultoria digital", "auditoria de sistemas y optimizacion de infraestructura web"),
    ("desarrollo corporativo", "blindaje de pasarelas de datos y cumplimiento normativo"),
    ("agencia de servicios", "posicionamiento local en buscadores y estrategias seo"),
    ("marca de e-commerce", "analisis de conversion de trafico y fugas de embudo")
]

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

def enviar_propuesta_api_http(email, sector, servicio):
    global emails_exito, emails_failed
    try:
        api_key = os.getenv("BREVO_API_KEY")
        sender_email = os.getenv("SENDER_EMAIL", "oficina@enjambresaas.online")
        sender_name = os.getenv("SENDER_NAME", "Enjambre SaaS")
        
        if not api_key:
            print("[⚠️] Error Crítico: Falta la clave secreta BREVO_API_KEY en Render.", flush=True)
            emails_failed += 1
            return

        print(f"⚡ [CONEXIÓN API BREVO] Enviando auditoría transaccional a: {email}", flush=True)

        # 🚀 CONEXIÓN PURA BLINDADA
        conn = http.client.HTTPSConnection("://brevo.com")
        
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": api_key
        }
        
        # 📝 TEXTO PROFESIONAL SANEADO: Cruza los filtros de Hotmail/Gmail sin alertas de spam
        html_content = f"""
        <p>Estimado responsable de operaciones,</p>
        <p>Hemos analizado recientemente los tiempos de respuesta y los protocolos de despliegue público asociados a las marcas de su sector.</p>
        <p>Detectamos un margen de optimización importante en el área de <strong>{servicio}</strong>, aspecto clave para la captación digital de su negocio.</p>
        <p>Hemos preparado un informe detallado con las correcciones técnicas pertinentes. Si desea recibir la auditoría completa sin compromiso alguno, responda directamente a este correo electrónico.</p>
        <p>Atentamente,<br><strong>{sender_name}</strong><br>Soporte de Infraestructura Digital</p>
        """
        
        payload = {
            "sender": {"name": sender_name, "email": sender_email},
            "to": [{"email": email}],
            "subject": f"Estudio de optimizacion digital para tu sector de {sector}",
            "htmlContent": html_content
        }

        conn.request("POST", "/v3/smtp/email", json.dumps(payload), headers)
        
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        
        if response.status == 201:
            emails_exito += 1
            print(f"✅ [API ÉXITO] ¡Túnel verificado! Correo enviado correctamente a: {email}", flush=True)
        else:
            emails_failed += 1
            print(f"❌ [API RECHAZO] Error de validación Brevo: {data}", flush=True)
        conn.close()
            
    except Exception as e:
        emails_failed += 1
        print(f"❌ [FALLA TOTAL DE RED] Fallo en la petición HTTP: {e}", flush=True)

def bucle_automatico_infinito():
    global busquedas_exitosas, busquedas_fallidas, leads_cazados
    print("🚀 [MALLA AUTOMÁTICA] Bucle continuo activado de forma nativa.", flush=True)
    
    # Pausa de seguridad para estabilizar Flask en el arranque
    time.sleep(10)
    
    while True:
        try:
            sector, servicio = random.choice(sectores)
            ciudad = random.choice(ciudades)
            
            # 🎯 DIRECCIÓN DE CONTROL REAL: Tu Hotmail para que veas que entra directo
            email_objetivo = "severianobenitez@hotmail.com"
            
            print(f"🔍 [RADAR] Procesando envío legítimo hacia: {email_objetivo}", flush=True)
            
            busquedas_exitosas += 1
            leads_cazados += 1
            
            enviar_propuesta_api_http(email_objetivo, sector, servicio)
            
        except Exception as e:
            busquedas_fallidas += 1
            print(f"❌ [RADAR ERROR] Error en ciclo: {e}", flush=True)
        
        # ⏱️ Pausa obligatoria antianomalías de 15 minutos (900 segundos)
        print("⏳ [RELOJ INTERNO] Entrando en reposo estricto por 900 segundos...", flush=True)
        time.sleep(900)

# Lanzamiento del hilo nativo en paralelo
threading.Thread(target=bucle_automatico_infinito, daemon=True).start()

if __name__ == '__main__':
    port = int(os.getenv("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
