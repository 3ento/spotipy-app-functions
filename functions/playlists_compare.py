from base.constants import CLIENT_CREDENTIAL_FLOW, get_playlist_tracks

# setup of the authorization needed
spotify = CLIENT_CREDENTIAL_FLOW

# !!! Tracks are being compared by name, which leads to different tracks with shared names to be considered "shared"
# !!! - ex. Instrumentals' Killer from JoJo and Songs' Killer by The Ready Set

def get_playlist_comparison(playlist_one_uri, playlist_two_uri, mode=None):

    """
    :param playlist_one_uri: URI of playlist 1
    :param playlist_two_uri: URI of playlist 2
    :param mode: which comparison to return
    :return: nothing, it prints.
    """

    # vars
    pl1 = {el['track']['name'] for el in get_playlist_tracks(playlist_one_uri)}
    pl2 = {el['track']['name'] for el in get_playlist_tracks(playlist_two_uri)}

    # comparisons (sets have built-in analysis methods like diff, intersection, union etc.)
    pl1_unique = pl1.difference(pl2)
    pl2_unique = pl2.difference(pl1)
    shared = pl1.intersection(pl2)

    if mode is None:
        print(f'{spotify.playlist(playlist_id=playlist_one_uri, fields="name")["name"]} only: \n')
        for el in pl1_unique:
            print(el)

        print(f'\n{spotify.playlist(playlist_id=playlist_two_uri, fields="name")["name"]} only: \n')
        for el in pl2_unique:
            print(el)

        print(f'\nShared: \n')
        for el in shared:
            print(el)

    # ===================================================================================================

    if mode == 'pl1-uni':
        print(f'{spotify.playlist(playlist_id=playlist_one_uri, fields="name")["name"]} only: \n')
        for el in pl1_unique:
            print(el)

    elif mode == 'pl2-uni':
        print(f'\n{spotify.playlist(playlist_id=playlist_two_uri, fields="name")["name"]} only: \n')
        for el in pl2_unique:
            print(el)

    elif mode == 'shared':
        print(f'\nShared: \n')
        for el in shared:
            print(el)
