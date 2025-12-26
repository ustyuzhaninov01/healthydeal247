import streamlit as st
import requests
import hashlib
import json
from datetime import datetime


# Função para gerar o hash SHA-256
def hash_value(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


# Função para enviar o evento para a API de Conversões do Facebook
def enviar_evento_facebook(access_token, pixel_id, event_name, user_data, custom_data):
    api_url = f'https://graph.facebook.com/v14.0/{pixel_id}/events'

    event_data = {
        'data': [
            {
                'event_name': event_name,
                'event_time': int(datetime.now().timestamp()),  # Timestamp do evento
                'user_data': user_data,
                'custom_data': custom_data,
                'action_source': 'website',  # Fonte da ação (pode ser 'website', 'app', etc.)
            }
        ],
        'access_token': access_token,
    }

    response = requests.post(api_url, json=event_data)

    if response.status_code == 200:
        return 'Evento enviado com sucesso!'
    else:
        return f'Erro ao enviar evento: {response.status_code} - {response.text}'


# Interface Streamlit
st.title('Integração da API de Conversões do Facebook')

# Campos para o usuário preencher
access_token = st.text_input('Access Token do Facebook', type='password')
pixel_id = st.text_input('ID do Pixel', type='password')
event_name = st.selectbox('Escolha o tipo de evento', ['Purchase', 'Lead', 'AddToCart', 'PageView'])

email = st.text_input('Email do cliente')
phone = st.text_input('Telefone do cliente')

valor = st.number_input('Valor do evento', min_value=0.0, format="%.2f")
currency = st.selectbox('Moeda', ['BRL', 'USD', 'EUR'])

# Botão para enviar o evento
if st.button('Enviar Evento'):
    if access_token and pixel_id and event_name:
        # Hash dos dados do usuário
        user_data = {
            'em': [hash_value(email)],  # Hash do e-mail do cliente
            'ph': [hash_value(phone)],  # Hash do telefone do cliente
        }

        custom_data = {
            'currency': currency,
            'value': valor,
        }

        resultado = enviar_evento_facebook(access_token, pixel_id, event_name, user_data, custom_data)
        st.success(resultado)
    else:
        st.error('Preencha todos os campos necessários.')
