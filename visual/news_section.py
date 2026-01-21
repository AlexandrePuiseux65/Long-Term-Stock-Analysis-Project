import streamlit as st
from datetime import datetime

def display_news(stock_news):
    """
    Affiche les actualités récupérées de Yahoo Finance.
    """
    st.markdown("### Latest News")
    
    if not stock_news:
        st.write("ERRROR: No recent news found for this ticker.")
        return

    for article in stock_news:
        pub_date = datetime.fromtimestamp(article['providerPublishTime']).strftime('%Y-%m-%d %H:%M')
        
        with st.container():
            col1, col2 = st.columns([1, 4])
            
            if 'thumbnail' in article and 'resolutions' in article['thumbnail']:
                img_url = article['thumbnail']['resolutions'][0]['url']
                col1.image(img_url, use_container_width=True)
            
            with col2:
                st.markdown(f"**[{article['title']}]({article['link']})**")
                st.caption(f"Source: {article['publisher']} | Published: {pub_date}")
            
            st.markdown("---")