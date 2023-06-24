import pandas as pd
import matplotlib.pyplot as plt


def main():
    spotify_playlist = {
        'Every Time I Close My Eyes': 4.56,
        'Talk To Me': 4.54,
        'I Said I Love You': 4.05,
        'When Your Body Gets Weak': 5.39,
        'Simple Days': 4.32,
        'All Day Thinkin\'': 4.23,
        'Seven Seas': 4.01,
        'The Day (That You Gave Me A Son)': 4.29,
        'How Come, How Long': 5.14,
        'This is for the Lover in You': 4.04
    }

    sun_playlist = pd.Series(spotify_playlist)

    print('Sunday Is For Lovers Playlist Songs Length:')
    print('-----------------------------------------------')
    print(sun_playlist)
    print('-----------------------------------------------')
    print('Longest Song In Playlist:\t', sun_playlist.index.max(), '-', sun_playlist.max())
    print('Shortest Song In Playlist:\t', sun_playlist.index.min(), '-', sun_playlist.min())
    print('-----------------------------------------------')

    x = sun_playlist.index
    y = sun_playlist.values

    plt.xticks(rotation=45, size=10)
    plt.barh(x, y, color='blue')

    plt.title('Sunday For Lovers Playlist Songs Length', size=15)
    plt.ylabel('Songs', size=15)
    plt.xlabel('Song Length', size=25)

    plt.show()


main()
