import streamlit as st

# --- CONFIGURATION (CONSTANTES) ---
CONSO_FIXE = 6.0      # L/100km
PRIX_GAZOLE = 1.699   # €/L
PRIX_MINIMUM = 3.00   # Prix plancher par personne

# Configuration de la page
st.set_page_config(page_title="JB's Car", page_icon="🚘", layout="centered")

# --- CSS POUR RÉDUIRE LES MARGES ET STYLER ---
st.markdown("""
    <style>
        .block-container {padding-top: 2rem; padding-bottom: 0rem;}
        h1 {margin-bottom: 0rem;}
        div[data-testid="stMarkdownContainer"] p {font-size: 1.1em;}
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

# Titre compact
st.markdown("<h2 style='text-align: center; margin: 0;'>🚘 JB's Car Trip</h2>", unsafe_allow_html=True)

# ESPACE INPUTS (Distance & Passagers)
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

# --- NOUVELLE SECTION : FRAIS DE SERVICE ---
st.write("")
st.markdown("**🛠️ Frais Service & Usure**")
# J'ai mis un max à 20€, c'est suffisant pour des trajets "standards"
frais_service = st.slider("Service", min_value=0.0, max_value=20.0, value=2.0, step=0.5, label_visibility="collapsed")
st.caption("Amortissement véhicule + Temps conducteur")


# --- LE COEUR DU PROBLÈME (CALCULS) ---
# 1. Calcul du coût carburant pur
cout_carburant = (distance * (CONSO_FIXE / 100)) * PRIX_GAZOLE

# 2. Calcul du coût TOTAL (Carburant + Tes services)
cout_total_trajet = cout_carburant + frais_service

# 3. Calcul par personne
if nb_personnes > 0:
    prix_reel_par_tete = cout_total_trajet / nb_personnes
else:
    prix_reel_par_tete = 0

# 4. Application du forfait minimum
if prix_reel_par_tete < PRIX_MINIMUM:
    prix_final = PRIX_MINIMUM
    info_text = "⚠️ Forfait minimum appliqué"
    color_price = "#FF9800" # Orange si c'est le prix min
else:
    prix_final = prix_reel_par_tete
    info_text = "✅ Prix ajusté (Carburant + Service)"
    color_price = "#00C853" # Vert si c'est le prix réel

# --- AFFICHAGE RÉSULTAT ---
st.markdown("---")

st.markdown(
    f"""
    <div style='text-align: center; padding: 15px; background-color: #f0f2f6; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <p style='color: grey; margin:0; font-size: 0.8em; text-transform: uppercase; letter-spacing: 1px;'>PRIX PAR PERSONNE</p>
        <h1 style='font-size: 3.8em; margin: 5px 0; color: {color_price}; font-weight: 800;'>{prix_final:.2f} €</h1>
        <p style='color: #555; margin:0; font-size: 0.85em;'>{info_text}</p>
        <p style='color: #aaa; margin-top:5px; font-size: 0.7em;'>(Coût total trajet : {cout_total_trajet:.2f}€)</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# Bouton Action
st.link_button("💳 PAYER MAINTENANT (PayPal)", "https://paypal.me/jbvlle?locale.x=fr_FR&country.x=FR", type="primary", use_container_width=True)
