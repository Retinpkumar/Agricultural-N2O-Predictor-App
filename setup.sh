mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[theme]\n\
 textColor='#000000'\n\
 backgroundColor='#D3ECDB'\n\
 font='sans serif'\n\
" > ~/.streamlit/config.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml