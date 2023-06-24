import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def main():
    # Creating gym playlist:
    print("================")
    print("The GYM Playlist")
    print("================")

    # Read in the csv file
    df = pd.read_csv("./spotify_global_2019_most_streamed_tracks_audio_features.csv")

    # Filter the Features:
    our_df = df[['Rank', 'Artist', 'Track Name', 'tempo', 'danceability', 'energy']]

    # Select songs with high danceability and tempo to get that gym pump going:
    dance = our_df[our_df["danceability"] > 0.85]
    gym_playlist = dance[dance["energy"] > 0.8]

    # Display the Gym Playlist:
    print(gym_playlist)

    # Export the playlist:
    gym_playlist.to_excel('gym_pump_playlist.xlsx')
    print("\nPlaylist Exported to Excel Document!")


main()
