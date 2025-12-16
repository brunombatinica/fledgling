import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader

def create_world_map():
    """
    Creates a world map with black background and highlights USA, Brazil, and UK in yellow.
    Saves the map as world_map.png in the same directory.
    """
    # Create figure with black background
    fig = plt.figure(figsize=(15, 8), facecolor='black')
    ax = plt.axes(projection=ccrs.PlateCarree(), facecolor='black')
    
    # Set extent to exclude Antarctica (limit latitude to -60 degrees)
    ax.set_extent([-180, 180, -60, 90], crs=ccrs.PlateCarree())
    
    # Add coastlines with thicker lines (water borders only, no inland borders)
    ax.add_feature(cfeature.COASTLINE, edgecolor='white', linewidth=1.5)
    
    # Countries to highlight in yellow
    countries_to_highlight = ['United States of America', 'Brazil', 'United Kingdom']
    
    # Load country boundaries from Natural Earth
    try:
        shpfilename = shpreader.natural_earth(resolution='110m',
                                            category='cultural',
                                            name='admin_0_countries')
        reader = shpreader.Reader(shpfilename)
        
        # Create a dictionary of country names and geometries, excluding Antarctica
        countries = {}
        for country in reader.records():
            country_name = country.attributes['NAME']
            # Skip Antarctica
            if country_name != 'Antarctica':
                countries[country_name] = country.geometry
        
        # Highlight specified countries
        for country_name in countries_to_highlight:
            if country_name in countries:
                # USA in white, others in yellow
                if country_name == 'United States of America':
                    color = 'white'
                else:
                    color = '#F4F473'
                ax.add_geometries([countries[country_name]], ccrs.PlateCarree(),
                                facecolor=color, edgecolor=color, 
                                linewidth=1.5)
    except Exception as e:
        print(f"Error loading country data: {e}")
        print("Please ensure cartopy is installed: pip install cartopy")
        return
    
    # Remove axes for cleaner look
    ax.set_frame_on(False)
    
    # Save the figure
    output_path = 'world_map.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='black', 
                edgecolor='none', pad_inches=0)
    print(f"Map saved as {output_path}")
    
    plt.close()

if __name__ == "__main__":
    create_world_map()

