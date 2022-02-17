mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[theme]\n\
 textColor='#000000'\n\
 secondaryBackgroundColor='#C7DDBE'\n\
 font='sans serif'\n\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml