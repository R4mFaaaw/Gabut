#!/bin/bash
# ==============================================================================
# Script Peluncur Website Interaktif MINERAPETRO-EXPERT
# Program Studi S1 Teknik Pertambangan FT-UNIKARTA
# Dosen Pengampu: Sundyo, S.T., M.T.
# ==============================================================================

PORT=8080
if [ ! -z "$1" ]; then
  PORT=$1
fi

echo "========================================================================"
echo "  ⛏️  MINERAPETRO-EXPERT: Media Belajar & Hafalan Interaktif Tambang"
echo "  Universitas Kutai Kartanegara (UNIKARTA)"
echo "  Dosen Pengampu: SUNDYO, S.T., M.T."
echo "========================================================================"
echo "Menjalankan web server lokal pada port: $PORT"
echo "Buka browser Anda di: http://localhost:$PORT/"
echo "Tekan CTRL+C untuk menghentikan server."
echo "========================================================================"

python3 -m http.server $PORT
