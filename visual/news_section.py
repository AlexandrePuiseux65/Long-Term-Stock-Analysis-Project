import streamlit as st
from datetime import datetime

def display_news(stock_news):
    st.markdown("### Latest News")
    
    if not stock_news:
        st.info("No news articles available for this stock at the moment.")
        return

    for article in stock_news:
        content = article.get('content', {})

        title = content.get('title', "Headline not available")

        link_data = content.get('canonicalUrl', {})
        link = link_data.get('url', "#")
        raw_date = content.get('pubDate')
        if raw_date:
            try:
                date_obj = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%SZ")
                pub_date = date_obj.strftime('%Y-%m-%d %H:%M')
            except:
                pub_date = raw_date
        else:
            pub_date = "Date unknown"

        provider = content.get('provider', {})
        publisher = provider.get('displayName', "Unknown Source")

        if title != "Headline not available":
            st.markdown(f"**[{title}]({link})**")
            st.caption(f"Source: {publisher} | Published: {pub_date}")
            
            summary = content.get('summary', "")
            if summary:
                st.write(f"{summary[:200]}...")
                
            st.markdown("---")