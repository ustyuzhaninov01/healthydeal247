import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Um afiliado no Brasil", page_icon=":memo:", initial_sidebar_state="collapsed",)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .streamlit-ico {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def enable_indexability():
    meta_tags = {
        'robots': 'index,follow',
        'googlebot': 'index,follow',
        'description': 'Bootcamp - Um afiliado no Brasil',
        'keywords': 'afiliado, marketing, dicas, ofersas, nutra',
        'google-site-verification': 'sJbVjLAelpAAjiePKc8Monk8R4V1ppa-ytXMAzYBCUk'
    }

    for name, content in meta_tags.items():
        st.write(f"<meta name='{name}' content='{content}'>", unsafe_allow_html=True)

    st.write("<link rel='canonical' href='https://umafiliadonobrasil.onrender.com/bootcamp' />", unsafe_allow_html=True)



def main():
    st.title("Bootcamp AdCombo.com")
    st.write("Bem-vindo ao Bootcamp AdCombo.com! Selecione o dia abaixo para ver o desafio correspondente.")

    # Lista de desafios
    challenges = [

        {
            "day": "Dia 1",
            "content": "Familiarize-se com a plataforma AdCombo.com e explore as diferentes ofertas disponíveis.",
            "video": "https://www.youtube.com/watch?v=yXIOh90lleY",
            "text": """Desvendando a Plataforma Adcombo: Seu Guia Essencial para o Sucesso!\
           
            Neste vídeo, vamos explorar as abas ocultas e poderosas ferramentas que farão suas campanhas decolarem.\\
            Prepare-se para colher os frutos do conhecimento AdCombo!\\
            Dê um mergulho profundo na plataforma AdCombo e desbloqueie as ferramentas para dominar o mundo das campanhas lucrativas!\\
            Descubra tudo o que a AdCombo tem reservado para você.\\
            Descubra por que a AdCombo é o parceiro perfeito para o seu sucesso no marketing de afiliados.\\
            Junte-se a nós enquanto mergulhamos nas riquezas das abas da plataforma AdCombo e desvendamos o caminho para campanhas altamente lucrativas!"""
        }

        ,
        {
            "day": "Dia 2",
            "content": "Domine o AdCombo: Escolha, Configure e Conecte Ofertas com API do Zero",
            "video": "https://youtu.be/ihm23EEpYeQ?si=wj_FxqZHP14475-3",
            "text": """No mundo do marketing de afiliados, encontrar a oferta perfeita é como encontrar o tesouro escondido!\
            
            🗺️💎 E é exatamente isso que você vai aprender no nosso novo vídeo.\\
            🔍 Estratégias de Seleção: Vou mostrar-lhe as táticas para identificar a oferta que não só chama a atenção, mas converte! \\
            🛠 Configuração Detalhada: Aprenda a personalizar suas ofertas com flexibilidade e precisão. Configurar nunca foi tão fácil! \\
            🔐 Conexão Segura com API: E para aquele detalhe técnico que faz toda a diferença - vou te ensinar a criar um código API do zero para uma conexão segura e confiável com o AdCombo. \\
            📈 Maximize seus Lucros: Equipado com esses conhecimentos, você estará pronto para elevar suas campanhas a um novo nível.  """
        },
        {
            "day": "Dia 3",
            "content": "Decifrando o Call Center: Explorando os Status nas Ofertas COD e Suas Razões",
            "video": "https://www.youtube.com/watch?v=y0m5ukXK27g",
            "text": """Embarque conosco nesta jornada reveladora pelos enredos do call center nas ofertas Cash on Delivery. \
            
            🗣 Este vídeo explora minuciosamente os diversos status que atravessam o processo, desde a confirmação do pedido até a entrega na sua porta do seu lead. \\
            Vamos desvendar:\\
            ➡️ Os mistérios por trás de cada status, mergulhando nas razões que os impulsionam, proporcionando uma compreensão profunda de como o atendimento ao cliente nesse contexto é dinâmico e eficiente \\
            ➡️ Os segredos dos status e entender as razões por trás de cada etapa \\
            Aguardamos seus comentários e esperamos que esses dias que antecedem as festas de Natal sejam inesquecíveis! 🎉🎉🎉 \\
            Não perca tempo!\\
            ➡️ Cantar em AdCombo - https://adcombo.com/\\
            📱 Siga-nos para se manter atualizado: \\
            Telegram - https://t.me/adcombo_brasil\\
            Instagram - adcombo_brazil  \\
            Facebook -  adcombobrasil\\ """
        },
        {
            "day": "Dia 4",
            "content": "Analise os dados das suas campanhas e faça relatórios sobre o desempenho.",
            "video": "https://www.youtube.com/watch?v=456789012",
            "photo": "https://example.com/day4_photo.jpg",
            "text": "No quarto dia do bootcamp, é hora de analisar os dados das suas campanhas."
                    "Assista ao vídeo abaixo para aprender a interpretar os dados"
                    "e confira a foto relacionada ao desafio de hoje. "
                    "Faça relatórios sobre o desempenho das suas campanhas"
                    " e identifique áreas para melhorias!"
        },
        {
            "day": "Dia 5",
            "content": "Explore diferentes fontes de tráfego e encontre novas oportunidades.",
            "video": "https://www.youtube.com/watch?v=567890123",
            "photo": "https://example.com/day5_photo.jpg",
            "text": "No quinto dia do bootcamp, é hora de explorar diferentes fontes de tráfego."
                    "Assista ao vídeo abaixo para descobrirnovas oportunidades de tráfego"
                    "e confira a foto relacionada ao desafio de hoje. "
                    "Expanda suas opções de tráfego e descubra novas maneiras de alcançar seu público-alvo!"
        },
        {
            "day": "Dia 6",
            "content": "Aprenda sobre segmentação de público e aplique técnicas para melhorar sua campanha.",
            "video": "https://www.youtube.com/watch?v=678901234",
            "photo": "https://example.com/day6_photo.jpg",
            "text": "No sexto dia do bootcamp, é hora de aprimorar suas habilidades de segmentação de público. "
                    "Assista ao vídeo abaixo para aprender técnicas avançadas de segmentação"
                    "e confira a foto relacionada ao desafio de hoje. "
                    "Aplique essas técnicas à sua campanha para melhorar sua eficácia!"
        },
        {
            "day": "Dia 7",
            "content": "Realize testes A/B para melhorar seus anúncios e páginas de destino.",
            "video": "https://www.youtube.com/watch?v=789012345",
            "photo": "https://example.com/day7_photo.jpg",
            "text": "No sétimo dia do bootcamp, é hora de realizar testes A/B"
                    "para otimizar seus anúncios e páginas de destino. "
                    "Assista ao vídeo abaixo para entender como realizar testes eficazes"
                    "e confira a foto relacionada ao desafio de hoje. "
                    "Teste diferentes variações e descubra o que funciona melhor para seu público!"
        },
        {
            "day": "Dia 8",
            "content": "Aprenda sobre a retenção de clientes e aplique estratégias para aumentá-la.",
            "video": "https://www.youtube.com/watch?v=890123456",
            "photo": "https://example.com/day8_photo.jpg",
            "text": "No oitavo dia do bootcamp, é hora de focar na retenção de clientes. "
                    "Assista ao vídeo abaixo para aprender estratégias eficazes de retenção"
                    "e confira a foto relacionada ao desafio de hoje. "
                    "Implemente essas estratégias para aumentar a fidelidade dos seus clientes"
                    " e maximizar o valor do seu negócio!"
        },
        {
            "day": "Dia 9",
            "content": "Participe da comunidade da AdCombo.com e compartilhe suas experiências.",
            "video": "https://www.youtube.com/watch?v=901234567",
            "photo": "https://example.com/day9_photo.jpg",
            "text": "No nono dia do bootcamp, é hora de se envolver com a comunidade da AdCombo.com. "
                    "Assista ao vídeo abaixo para descobrir como participar ativamente da comunidade"
                    "e confira a foto relacionada ao desafio de hoje. Compartilhe suas experiências, "
                    "aprenda com outros afiliados e construa uma rede de apoio!"
        },
    {
        "day": "Dia 10",
        "content": "Conclua o bootcamp e reflita sobre o que aprendeu.",
        "video": "https://www.youtube.com/watch?v=1234567890",
        "photo": "https://example.com/day10_photo.jpg",
        "text": "No décimo e último dia do bootcamp, é hora de concluir sua jornada. "
                "Assista ao vídeo para refletir sobre tudo o que aprendeu durante o bootcamp"
                "e confira afoto relacionada ao desafio de hoje. "
                "Celebre suas conquistas, reveja seus aprendizados e planeje os próximos passos"
                " para continuar crescendo como afiliado da AdCombo.com!"
        },
    ]

    # Menu de seleção de dia
    selected_day = st.selectbox("Selecione o dia:", list(range(1, 11)))

    # Exibir desafio correspondente
    challenge = challenges[selected_day - 1]
    st.write(f"\n**{challenge['day']}:**")
    st.write(challenge['content'])
    st.video(challenge['video'])
    st.write(challenge['text'])






if __name__ == "__main__":
    main()

