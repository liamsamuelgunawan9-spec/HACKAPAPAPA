import streamlit as st
import requests
import phonenumbers
from phonenumbers import geocoder, carrier
import time
import streamlit as st
import streamlit.components.v1 as components

st.title("HackAPP: Visual Pentest Builder")

# Read the HTML file and embed it
with open("templates/blockly.html", "r") as f:
    html_content = f.read()

components.html(html_content, height=500)

if st.button("Run Program"):
    st.write("Executing blocks...")
# 1. Page Configuration (Sets the browser tab title and dark mode)
st.set_page_config(page_title="CyberSuite Alpha", page_icon="🛡️", layout="wide")

# 2. UI Injection (FIXED: unsafe_allow_html)
st.markdown("""
    <style>
    /* Hacker-style terminal aesthetics */
    .stButton>button {
        border: 1px solid #00ff00;
        color: #00ff00;
        background-color: transparent;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #00ff00;
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation
st.sidebar.title("⚡ CyberSuite")
st.sidebar.markdown("---")
menu = st.sidebar.radio("Terminal Modules", ["Command Center", "IP Reconnaissance", "Phone OSINT", "CyberBot AI"])

# 4. Modules Logic

if menu == "Command Center":
    st.title("🛡️ Command Center")
    st.markdown("Welcome to CyberSuite Alpha. Select a module from the sidebar to initialize testing.")
    st.code("System Status: ONLINE\nConnection: SECURE\nModules: LOADED\nTarget: NONE")

elif menu == "IP Reconnaissance":
    st.title("🌐 IP Reconnaissance")
    st.markdown("Map target IP addresses to physical locations and ISPs.")
    
    ip_target = st.text_input("Enter Target IP Address (e.g., 8.8.8.8)")
    
    if st.button("Analyze Infrastructure"):
        if ip_target:
            with st.spinner("Querying global registries..."):
                try:
                    # Using a free public API for IP lookup
                    response = requests.get(f"http://ipapi.co/{ip_target}/json/")
                    data = response.json()
                    
                    if "error" not in data:
                        st.success("Target Locked")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Target IP:** {data.get('ip')}")
                            st.write(f"**City:** {data.get('city')}")
                            st.write(f"**Region:** {data.get('region')}")
                        with col2:
                            st.write(f"**Country:** {data.get('country_name')}")
                            st.write(f"**ISP / Org:** {data.get('org')}")
                    else:
                        st.error("Invalid IP address or local network IP.")
                except Exception as e:
                    st.error("Network routing error. Please try again.")
        else:
            st.warning("Awaiting Target IP input.")

elif menu == "Phone OSINT":
    st.title("📱 OSINT Phone Validator")
    st.markdown("Extract telecom registry metadata from public phone networks.")
    
    phone_input = st.text_input("Enter Phone Number (Include country code, e.g., +14155552671)")
    
    if st.button("Extract Metadata"):
        if phone_input:
            with st.spinner("Querying telecom nodes..."):
                try:
                    parsed_num = phonenumbers.parse(phone_input)
                    if phonenumbers.is_valid_number(parsed_num):
                        region = geocoder.description_for_number(parsed_num, "en")
                        network = carrier.name_for_number(parsed_num, "en")
                        
                        st.success("Data Extraction Complete")
                        st.write(f"**Standardized Format:** {phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
                        st.write(f"**Geographic Registration:** {region if region else 'Data Unavailable'}")
                        st.write(f"**Telecom Carrier:** {network if network else 'Unknown / VoIP / Virtual'}")
                    else:
                        st.error("Number format invalid. Did you include the '+' and country code?")
                except Exception as e:
                    st.error("Failed to parse string. Ensure strict E.164 formatting.")
        else:
            st.warning("Awaiting Phone Number input.")

elif menu == "CyberBot AI":
    st.title("🤖 CyberBot Assistant")
    st.markdown("Educational assistant for command breakdowns and network theory.")
    
    user_query = st.text_input("Terminal Input:")
    
    if st.button("Ask CyberBot"):
        if user_query:
            with st.spinner("Processing query..."):
                time.sleep(1) # Simulated thinking delay
                
                # Hardcoded educational responses for testing
                if "dirb" in user_query.lower():
                    st.info("**CyberBot:** `dirb` is a web content scanner. It looks for hidden directories and files on a web server by launching a dictionary-based attack (testing thousands of common folder names like '/admin' or '/backup') and analyzing the HTTP response codes.")
                elif "ping" in user_query.lower():
                    st.info("**CyberBot:** `ping` is a basic network diagnostic tool. It sends a tiny packet of data (an ICMP Echo Request) to a target IP. If the target is online and not blocking pings, it bounces the packet back, telling you exactly how many milliseconds the round-trip took.")
                else:
                    st.info(f"**CyberBot:** I am currently running in offline simulation mode. You asked about: '{user_query}'. Hook me up to a live LLM API to get real-time dynamic answers!")
        else:
            st.warning("Awaiting query.")