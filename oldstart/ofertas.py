import streamlit as st
import requests
from urllib.parse import urlencode
import hashlib
from datetime import datetime
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.api import FacebookAdsApi


# Função para capturar o fbclid da URL
def get_fbclid_from_url():
    query_params = st.experimental_get_query_params()  # Captura os parâmetros da URL
    fbclid = query_params.get("fbclid", [None])[0]  # Obtém o valor do fbclid (caso exista)
    return fbclid

# Defina seu access_token e pixel_id
access_token = 'EAAQtIzSqZANYBO3eNOHhR9OhZBcqlKAZA6MfYKz5behXN0h4VZBKaUfZC444un9BK5k6FgGwBxnsk1ygxAK44ViXtqxsFgjGXygZCFjAyxmsg20zyZCxeg6BfQxOEtxGp2YRSuT8juEfDRNh77sq63o0ovx6btqi8L77h07TBpVxpRUdQG04NnZB8VK45fGdZBo3ogwZDZD'
pixel_id = '1048445737107274'

# Inicialize a API do Facebook com seu token
FacebookAdsApi.init(access_token=access_token)

# Função para enviar evento de conversão para o Facebook
def send_facebook_event(name, phone, value):
    # Hashing do email e telefone para segurança (não utilizado aqui, mas pode ser adaptado)
    user_data = UserData(
        phones=[hashlib.sha256(phone.encode('utf-8')).hexdigest()]
    )

    custom_data = CustomData(
        value=value,
        currency="USD"
    )

    event = Event(
        event_name="Lead",
        event_time=int(datetime.now().timestamp()),
        user_data=user_data,
        custom_data=custom_data,
    )

    events = [event]
    event_request = EventRequest(
        events=events,
        pixel_id=pixel_id
    )

    # Enviando o evento
    event_response = event_request.execute()

    return event_response


# URL da API do AdCombo
API_URL = 'https://api.adcombo.com/api/v2/order/create/'

# Configuração da página Streamlit
st.set_page_config(
    page_title="Um Afiliado no Brasil",
    page_icon=":memo:",
    initial_sidebar_state="collapsed",
)

# Escondendo o menu do Streamlit
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.streamlit-ico {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Exemplo de uso
if __name__ == "__main__":
    fbclid = get_fbclid_from_url()
    if fbclid:
        st.write(f"O fbclid capturado é: {fbclid}")
    else:
        st.write("Não foi encontrado o fbclid na URL.")

# Função para enviar dados para o AdCombo
def send_adcombo_order(name, phone, ip):
    country_code = 'FR'
    offer_id = '40302'
    referrer = 'http://my-click-site.com'
    price = '39'
    base_url = 'http://my-domain.com/'

    params = {
        'api_key': '32c12748901cfea93fe7cc2d175afbac',
        'name': name,
        'phone': phone,
        'ip': ip,
        'country_code': country_code,
        'offer_id': offer_id,
        'referrer': referrer,
        'price': price,
        'base_url': base_url,
        'clickid': fbclid
    }

    response = requests.get(API_URL + '?' + urlencode(params)).json()
    return response

# Layout do formulário no Streamlit
col1, col2 = st.columns(2)

with col1:
    name = st.text_input('Nome', placeholder='Digite seu nome completo', label_visibility='collapsed')
    phone = st.text_input('Telefone', placeholder='Digite seu número de telefone', label_visibility='collapsed')

    if st.button('Pedir'):
        ip_response = requests.get('https://httpbin.org/ip')
        if ip_response.status_code == 200:
            ip_data = ip_response.json()
            ip = ip_data['origin']
        else:
            ip = '127.0.0.1'  # Fallback IP address

        # Enviar pedido para o AdCombo
        adcombo_response = send_adcombo_order(name, phone, ip)

        # Enviar evento de conversão para o Facebook
        facebook_response = send_facebook_event(name, phone, 39.0)  # Enviando o valor do pedido


        if adcombo_response.get('code') == 'ok':
            st.success(f'Agradecemos. Nosso call center já está entrando em contato! ID do pedido: {adcombo_response["order_id"]}')
            # Mostrar resposta do Facebook Pixel (para debug)
            st.write("Evento enviado para o Facebook:", facebook_response)
        else:
            st.error('Tente novamente.')
            # Mostrar resposta do Facebook Pixel (para debug)
            st.write("Evento enviado para o Facebook:", facebook_response)


with col2:
    st.image('pack.png')

# Footer
st.markdown(
    """
    <style>
    .footer {
        padding: 20px;
        text-align: center;
    }
    .footer a {
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Adicionando links de política de privacidade e relatórios
privacy_policy_link = "https://land1.abxyz.info/policy_gdpr/-7EBRQCgQAAAEBA9-WA-yoN2GJAfoHAAMP3BllZhERChEJGhENQhENWgN1cwAAf2FkY29tYm__ZlczRE1rTDYAA3JN"
report_url = "https://ac-feedback.com/report_form/"

footer_text = f"© 2023 All Rights Reserved | [Privacy Policy]({privacy_policy_link}) | [Report]({report_url})"
st.markdown(footer_text, unsafe_allow_html=True)

# Ajuste de estilo do iframe (caso haja)
st.markdown(
    """
    <style>
        iframe[width="220"] {
            position: fixed;
            bottom: 60px;
            right: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
