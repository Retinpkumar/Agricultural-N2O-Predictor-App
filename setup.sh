mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"retinpkumar@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
textColor=#262730\n\
" > ~/.streamlit/config.toml