import streamlit as st

# --- CONFIGURATION (CONSTANTES) ---
CONSO_FIXE = 6.0      # L/100km
PRIX_GAZOLE = 1.699   # €/L
PRIX_MINIMUM = 3.00   # Prix plancher par personne

# Configuration de la page
st.set_page_config(page_title="JB's Car", page_icon="🚘", layout="centered")

# --- CSS POUR STYLER L'INTERFACE ---
st.markdown("""
    <style>
        .block-container {padding-top: 2rem; padding-bottom: 2rem;}
        h1 {margin-bottom: 0rem;}
        div[data-testid="stMarkdownContainer"] p {font-size: 1.1em;}
        /* Style personnalisé pour les boites d'info paiement */
        .payment-box {
            border: 1px solid #e0e0e0;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- BARRE LATÉRALE ---
with st.sidebar:
    st.header("🚗 JB'S CAR")
    st.info("**Citroën C4 Cactus**")
    st.write("---")
    st.write("**👤 Conducteur :** Jean-Baptiste VAILLE")
    st.write("**📱 Réseaux :**")
    st.write("📸 Insta : **jb.vlle**")
    st.write("👻 Snap : **jb.vlle**")
    st.write("---")
    st.caption(f"✨ Special Promo : Min {PRIX_MINIMUM}€")

# --- CONTENU PRINCIPAL ---

# Titre
st.markdown("<h2 style='text-align: center; margin: 0;'>🚘 JB's Car Trip</h2>", unsafe_allow_html=True)

# ESPACE INPUTS
st.write("") 
col1, col2 = st.columns(2)

with col1:
    st.markdown("**📍 Distance**")
    distance = st.number_input("km", value=15.0, step=0.1, format="%.1f", label_visibility="collapsed")
    st.caption(f"Conso: {CONSO_FIXE}L/100")

with col2:
    st.markdown("**👥 Passagers**")
    nb_personnes = st.slider("Passagers", min_value=1, max_value=4, value=3, label_visibility="collapsed")
    st.caption("Conducteur inclus")

# FRAIS DE SERVICE / USURE
st.write("")
st.markdown("**🛠️ Frais Service & Usure**")
frais_service = st.slider("Service", min_value=0.0, max_value=20.0, value=2.0, step=0.5, label_visibility="collapsed")
st.caption("Amortissement véhicule + Temps conducteur")


# --- CALCULS ---
# 1. Coût carburant
cout_carburant = (distance * (CONSO_FIXE / 100)) * PRIX_GAZOLE

# 2. Coût TOTAL (Carburant + Service)
cout_total_trajet = cout_carburant + frais_service

# 3. Calcul par personne
if nb_personnes > 0:
    prix_reel_par_tete = cout_total_trajet / nb_personnes
else:
    prix_reel_par_tete = 0

# 4. Logique Prix Minimum
if prix_reel_par_tete < PRIX_MINIMUM:
    prix
