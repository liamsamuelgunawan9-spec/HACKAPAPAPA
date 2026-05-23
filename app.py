import streamlit as st
import phonenumbers
from phonenumbers import geocoder, carrier
import requests

# 1. Page Configuration & Custom Theme Styling
st.set_page_config(page_title="CyberSuite Dashboard", page_icon="⚡", layout="wide")

# Custom CSS to make it look like a sleek terminal/hacker app
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2, h3 { color: #00ff66 !important; font-family: 'Courier New', monospace; }
    .stButton>button { background-color: #1f2937; color: #00ff66; border: 1px solid #00ff66; font-family: 'Courier New', monospace; }
    .stButton>button:hover { background-color: #00ff66; color: #1e293b; }
    </style>
    """, unsafe_allowed_html=True)

# 2. Sidebar Navigation Area
st.sidebar.title("⚡ CyberSuite v1.0")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Select Utility:", 
    ["🏠 Main Dashboard", "🔍 Infrastructure Tracker", "📞 Phone Metadata Lookup", "🤖 CyberBot AI Assistant"]
)
st.sidebar.markdown("---")
st.sidebar.info("Designed safely for educational cybersecurity workflows.")

# 🏠 SCREEN 1: Main Dashboard
if menu == "🏠 Main Dashboard":
    st.title("📟 Core Security Terminal")
    st.write("Welcome to your unified workspace. Choose a pipeline utility from the sidebar menu.")
    
    # Grid layout for metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="App Framework", value="Streamlit Engine")
    with col2:
        st.metric(label="Core Logic Status", value="Active / Secure")
    with col3:
        st.metric(label="Local API Access", value="Online")
        
    st.markdown("### 📋 Session Logs")
    st.code("[INFO] 12-Year-Old Developer initialized engine.\n[SUCCESS] Web socket bound to port 8501.\n[READY] Awaiting target data strings...")

# 🔍 SCREEN 2: Infrastructure Tracker (IP Lookup)
elif menu == "🔍 Infrastructure Tracker":
    st.title("🔍 Target Network Registry Lookup")
    st.write("Extract public server hosting data from global internet registries safely.")
    
    # Using an expansive container layout to keep it organized
    with st.container():
        ip_input = st.text_input("Input Target Public IP Address:", placeholder="e.g., 8.8.8.8")
        
        if st.button("Query Registry"):
            if ip_input:
                with st.spinner("Decoding infrastructure packets..."):
                    try:
                        response = requests.get(f"https://ipapi.co/{ip_input}/json/", timeout=5)
                        data = response.json()
                        
                        if "error" in data:
                            st.error(f"Registry Refusal: {data.get('reason')}")
                        else:
                            st.markdown("### 📊 Extracted Target Matrix")
                            c1, c2 = st.columns(2)
                            with c1:
                                st.info(f"**ISP Engine:** {data.get('org')}")
                                st.success(f"**Target City:** {data.get('city')}, {data.get('region')}")
                            with c2:
                                st.warning(f"**Geographic Sovereign:** {data.get('country_name')}")
                                st.error(f"**System ASN Block:** {data.get('asn')}")
                    except Exception as e:
                        st.error(f"Connection timed out: {e}")
            else:
                st.warning("Data input register empty. Please type an IP address.")

# 📞 SCREEN 3: Phone Metadata Lookup
elif menu == "📞 Phone Metadata Lookup":
    st.title("📞 Telecom Block Analyzer")
    st.write("Query international telecommunication structures for validation metrics.")
    
    with st.container():
        user_input = st.text_input("Input Target Phone String:", placeholder="Must include country code, e.g., +14155552671")
        
        if st.button("Parse Telecom Record"):
            if user_input:
                try:
                    parsed_num = phonenumbers.parse(user_input, None)
                    if phonenumbers.is_valid_number(parsed_num):
                        loc = geocoder.description_for_number(parsed_num, "en")
                        comp = carrier.name_for_number(parsed_num, "en")
                        
                        st.markdown("### 📡 Telecom Metrics")
                        res_col1, res_col2 = st.columns(2)
                        with res_col1:
                            st.success(f"**Registration Block Location:** {loc if loc else 'Unknown Subnet'}")
                        with res_col2:
                            st.info(f"**Carrier Route Assignment:** {comp if comp else 'Virtual/VoIP Entity'}")
                    else:
                        st.error("Syntax Error: Phone number structure is invalid.")
                except Exception as e:
                    st.error(f"Failed to load dataset frame: {e}")
            else:
                st.warning("Data input register empty. Input numeric string.")

# 🤖 SCREEN 4: AI CyberBot Assistant
elif menu == "🤖 CyberBot AI Assistant":
    st.title("🤖 CyberBot Command Intelligence")
    st.write("Ask questions about complex commands, flags, or status logs.")
    
    # Setting up localized chatbot conversation boxes
    user_query = st.text_input("Ask CyberBot (e.g., 'What is dirb?', 'What is an IP?'):", placeholder="Type educational request...")
    
    if st.button("Execute AI Context Query"):
        if user_query:
            query_lower = user_query.lower()
            st.markdown("### 💬 System Response Terminal")
            
            # Simulated AI "Brain" Logic matching user questions
            with st.spinner("Processing language tokens..."):
                if "dirb" in query_lower:
                    st.code("🤖 CyberBot Engine Response:\n\n"
                            "DIRB (Directory Buster) is a reconnaissance web scanner.\n"
                            "It tries to discover hidden files or directories on a website.\n"
                            "Mechanism: It takes a list of common names (like /admin, /backup, /login) "
                            "and appends them to the end of the URL to see if the server says 'Yes, this page exists!'.\n"
                            "Safe Practice: Never run this on websites you do not own or have written permission to test.")
                elif "ip" in query_lower or "address" in query_lower:
                    st.code("🤖 CyberBot Engine Response:\n\n"
                            "An IP (Internet Protocol) Address is like a mailing address for computers.\n"
                            "Just like a mailman needs your house address to deliver a package, your router "
                            "needs an IP address to know where to send video streams, web pages, and data packets.")
                elif "ping" in query_lower:
                    st.code("🤖 CyberBot Engine Response:\n\n"
                            "The 'ping' command checks if a target computer or server is awake and responsive.\n"
                            "It sends a tiny 'Hello!' packet and measures exactly how many milliseconds it takes "
                            "for the target to shout 'I am here!' back to you. Excellent for network troubleshooting.")
                else:
                    st.code(f"🤖 CyberBot Engine Response:\n\n"
                            f"Acknowledged query: '{user_query}'\n"
                            f"I am running on your local engine. I am ready to explain security terminology.\n"
                            f"Try asking specifically about commands like 'dirb', 'ping', or 'IP addresses'!")
        else:
            st.warning("Input request buffer empty.")