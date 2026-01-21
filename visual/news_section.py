import streamlit as st
from datetime import datetime

def display_news(stock_news):
    st.markdown("### Latest News")
    
    if not stock_news:
        st.write("No recent news found for this ticker.")
        return

    for article in stock_news:
        timestamp = article.get('providerPublishTime')
        
        if timestamp:
            pub_date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')
        else:
            pub_date = "Date unknown"
            
        with st.container():
            col1, col2 = st.columns([1, 4])
            
            # Vérification sécurisée pour l'image
            thumbnail = article.get('thumbnail')
            if thumbnail and 'resolutions' in thumbnail:
                img_url = thumbnail['resolutions'][0]['url']
                col1.image(img_url, use_container_width=True)
            
            with col2:
                # Utilisation de .get() pour le titre et le lien également
                title = article.get('title', 'No Title')
                link = article.get('link', '#')
                publisher = article.get('publisher', 'Unknown Source')
                
                st.markdown(f"**[{title}]({link})**")
                st.caption(f"Source: {publisher} | Published: {pub_date}")
            
            st.markdown("---")