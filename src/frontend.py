import tkinter as tk

root = tk.Tk()
root.title("PLAYLIST MIGRATOR")
root.geometry("300x300")

source_playlist_label = tk.Label(root, text="Playlist origem")
source_playlist_label.pack(pady=5)
source_playlist_entry = tk.Entry(root)
source_playlist_entry.pack(pady=5)

destination_playlist_label = tk.Label(root, text="Playlist destino")
destination_playlist_label.pack(pady=5)
destination_playlist_entry = tk.Entry(root)
destination_playlist_entry.pack(pady=5)

spotify_token_label = tk.Label(root, text="Token Bearer Spotify")
spotify_token_label.pack(pady=5)
spotify_token_entry = tk.Entry(root)
spotify_token_entry.pack(pady=5)

ytm_token1_label = tk.Label(root, text="Token SAPISIDHASH YouTube")
ytm_token1_label.pack(pady=5)
ytm_token1_entry = tk.Entry(root)
ytm_token1_entry.pack(pady=5)

ytm_token2_label = tk.Label(root, text="Token SAPISID YouTube")
ytm_token2_label.pack(pady=5)
ytm_token2_entry = tk.Entry(root)
ytm_token2_entry.pack(pady=5)

ytm_token3_label = tk.Label(root, text="Token PSID YouTube")
ytm_token3_label.pack(pady=5)
ytm_token3_entry = tk.Entry(root)
ytm_token3_entry.pack(pady=5)

ytm_token4_label = tk.Label(root, text="Token PSIDTS YouTube")
ytm_token4_label.pack(pady=5)
ytm_token4_entry = tk.Entry(root)
ytm_token4_entry.pack(pady=5)
