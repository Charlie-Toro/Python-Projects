# Album
# Caleb Bell
# Builds a dictionary describing an album


def make_album(first_name, album_title, last_name='', track_num=''):
    artist = first_name + last_name
    album_info = {
        'fname': first_name,
        'lname': last_name,
        'album': album_title,
        'tracks': track_num,
    }
    return album_info

print(make_album('David', 'Aladdin Sane', 'Bowie', '10'))

while True:
    print('Feel free to Enter q to quit \n')
    fir_name = input('Please enter the artist first name:')
    if fir_name == 'q':
        break
    las_name = input('Please enter artist last name: ')
    if las_name == 'q':
        break
    title = input('Please enter Album title: ')
    if title == 'q':
        break
    track = input('Please enter number of tracks: ')
    if track == 'q':
        break


print(make_album(fir_name, title, las_name, track))

