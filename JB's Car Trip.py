import streamlit as st

# --- CONFIGURATION (CONSTANTES) ---
CONSO_FIXE = 5.0      # L/100km
PRIX_GAZOLE = 1.679   # €/L
PRIX_MINIMUM = 3.00   # Prix plancher

# Configuration de la page
st.set_page_config(page_title="JB's Car", page_icon="🚘", layout="centered")

# --- CSS POUR RÉDUIRE LES MARGES (OPTIONNEL MAIS UTILE) ---
st.markdown("""
    <style>
        .block-container {padding-top: 2rem; padding-bottom: 0rem;}
        h1 {margin-bottom: 0rem;}
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

# --- CONTENU PRINCIPAL COMPACT ---

# Titre compact
st.markdown("<h2 style='text-align: center; margin: 0;'>🚘 JB's Car Trip</h2>", unsafe_allow_html=True)

# ESPACE INPUTS (Tout sur une ligne via des colonnes)
st.write("") # Petit espace
col1, col2 = st.columns(2)

with col1:
    st.markdown("**📍 Distance**")
    distance = st.number_input("km", value=5.0, step=0.1, format="%.1f", label_visibility="collapsed")
    st.caption(f"Base: {CONSO_FIXE}L/100 • {PRIX_GAZOLE}€")

with col2:
    st.markdown("**👥 Passagers**")
    nb_personnes = st.slider("Passagers", min_value=1, max_value=5, value=3, label_visibility="collapsed")
    st.caption("Conducteur inclus")

# --- CALCULS ---
cout_reel_total = (distance * (CONSO_FIXE / 100)) * PRIX_GAZOLE

if nb_personnes > 0:
    prix_theorique = cout_reel_total / nb_personnes
    if prix_theorique < PRIX_MINIMUM:
        prix_par_tete = PRIX_MINIMUM
        info_text = "Forfait min. appliqué"
    else:
        prix_par_tete = prix_theorique
        info_text = "Prix réel partagé"
else:
    prix_par_tete = 0
    info_text = ""

# --- AFFICHAGE RÉSULTAT (Compacté) ---
st.markdown("---")

# Zone de prix
st.markdown(
    f"""
    <div style='text-align: center; padding: 10px; background-color: #f0f2f6; border-radius: 10px;'>
        <p style='color: grey; margin:0; font-size: 0.9em;'>PAR PERSONNE</p>
        <h1 style='font-size: 3.5em; margin:0; color: #00C853;'>{prix_par_tete:.2f} €</h1>
        <p style='color: #888; margin:0; font-size: 0.8em;'>{info_text}</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("") # Espace

# Bouton Action
st.link_button("💳 PAYER MAINTENANT (PayPal)", "https://paypal.me/jbvlle?locale.x=fr_FR&country.x=FR", type="primary", use_container_width=True)

# --- NOUVEAU : AUTRES MOYENS DE PAIEMENT ---
st.markdown(
    """
    <div style='text-align: center; margin-top: 15px; color: #666;'>
        <span style='font-size: 0.9em;'>Aussi acceptés à bord :</span><br>
        <span style='font-size: 1.1em; font-weight: bold;'>💶 Espèces &nbsp; • &nbsp; 💳 Carte (SumUp)</span>
    </div>
    """,
    unsafe_allow_html=True
)