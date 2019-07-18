# "tracks" here is properly recognized as being a number. Good.
def make_album(artist_name, album_title, tracks = ''):
    if tracks:
        return {'artist_name': artist_name.title(), 'album_title': album_title.title(), 'tracks': tracks-1}
    else:
        return {'artist_name': artist_name.title(), 'album_title': album_title.title()}
    

dark_side = make_album('pink floyd', 'dark side of the moon', 8)
downward_spiral = make_album('nine inch nails', 'the downward spiral', 11)
kid_a = make_album('radiohead', 'kid a')

print(dark_side)
print(downward_spiral)
print(kid_a)