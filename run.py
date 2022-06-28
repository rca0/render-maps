from audioop import add
import folium


def _create_map(location, tiles="Stamen Terrain", zoom_start=16):
    return folium.Map(
        location=location,
        tiles=tiles,
        zoom_start=zoom_start
    )
    

def _add_mark(location, popup, obj_map):
    return folium.Marker(
        location,
        popup=popup,
        tooltop="Click here!"
    ).add_to(obj_map)


if __name__ == '__main__':
    lon = input("Type the longitude: ")
    lat = input("Type the latitude: ")
    address_description = input("Type the address description: ")
    
    location = [lon, lat]
    popup = "<i>{}</i>".format(address_description)
    
    obj_map = _create_map(
        location=location,
    )
    _add_mark(location, popup, obj_map)
    obj_map.save(r'map_rendered.html')
